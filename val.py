import os
import json


base_path = './'
# 读取 POSCAR 文件第 6 行（下标5）得到元素列表
with open(os.path.join(base_path, 'POSCAR'), 'r') as f:
    lines = f.readlines()
    elements = lines[5].split()
# 读取 POTCAR 文件，提取 ZVAL 行
with open(os.path.join(base_path, 'POTCAR'), 'r') as f:
    zval_lines = [line for line in f if 'ZVAL' in line]
# 将元素与ZVAL对应起来
zval_dict = {}
for idx, elem in enumerate(elements):
    # 提取该行的 ZVAL 数字部分
    zval_line = zval_lines[idx]
    zval_str = zval_line.split('=')[-1].strip().split()[0]
    zval_value = float(zval_str)
    zval_dict[elem] = zval_value
# 写入 JSON 文件
with open(os.path.join(base_path, 'zval.json'), 'w') as f:
    json.dump(zval_dict, f, indent=2)
