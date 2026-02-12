import argparse
import os
import json
import numpy as np
import pandas as pd
from pymatgen.analysis.ferroelectricity.polarization import get_total_ionic_dipole
from pymatgen.core.structure import Structure


# 得到 NGZF
def get_NGZF(path: str) -> float:
    return float(np.loadtxt(path))


# 电极化
def polarization(structure: Structure, ngzf: float, charge_path: str, zval_path: str) -> float:
    slab = structure.lattice.c
    area = structure.volume * 1e-20 / slab  # 二维材料面积（m^2）
    c = 1.602e-29  # 单位换算常数，将 e·Å 换成 C·m

    dz = slab / ngzf  # slab 厚度/NGZF

    # 电子极化（PLANAR_AVERAGE.dat: 第一列z, 第二列密度/电荷）
    a = np.loadtxt(charge_path)
    p_e = -np.sum(a[:, 0] * a[:, 1] * dz)

    # 离子极化（点电荷模型）
    with open(zval_path, "r", encoding="utf-8") as f:
        zval_dict = json.load(f)

    p_ion_vec = -get_total_ionic_dipole(structure, zval_dict)
    p_ion = p_ion_vec[2]  # z方向离子极化

    return (p_e + p_ion) * c / area


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Calculate out-of-plane polarization for 2D materials from VASP outputs."
    )
    parser.add_argument(
        "--base_path",
        type=str,
        required=True,
        help="Path to the data directory containing subfolders for each material.",
    )
    parser.add_argument(
        "--output",
        type=str,
        default="./polar.csv",
        help="Output csv file path. Default: ./polar.csv",
    )

    args = parser.parse_args()
    base_path = args.base_path

    results = {}

    for material in os.listdir(base_path):
        material_dir = os.path.join(base_path, material)
        if not os.path.isdir(material_dir):
            continue

        # 定义文件路径
        vasp_path = os.path.join(material_dir, "POSCAR")
        charge_path = os.path.join(material_dir, "PLANAR_AVERAGE.dat")  # vaspkit 316 from CHGCAR
        ngzf_path = os.path.join(material_dir, "NGZF.txt")
        zval_path = os.path.join(material_dir, "zval.json")  # from POTCAR

        # 基本存在性检查（防止中断整个批处理）
        needed = [vasp_path, charge_path, ngzf_path, zval_path]
        if not all(os.path.exists(p) for p in needed):
            # 缺文件就跳过，记录为 NaN
            results[material] = [material, np.nan]
            continue

        try:
            structure = Structure.from_file(vasp_path)
            ngzf = get_NGZF(ngzf_path)
            total_p = polarization(structure, ngzf, charge_path, zval_path)
            results[material] = [material, total_p]
        except Exception:
            # 某个材料出错不影响其他材料
            results[material] = [material, np.nan]

    df = pd.DataFrame.from_dict(results, orient="index", columns=["material", "polarization"])
    df.to_csv(args.output, index=False)


if __name__ == "__main__":
    main()
