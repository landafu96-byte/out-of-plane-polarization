# Out-of-Plane Polarization

A Python program for calculating out-of-plane polarization in two-dimensional ferroelectric materials.

## Required Files

To calculate the out-of-plane polarization, the following four files are required:

- `POSCAR`
- `zval.json`
- `NGZF.txt`
- `PLANAR_AVERAGE.dat`

---

## Preparing Required Files

### 1. POSCAR
`POSCAR` is the structure file of the material.  
Please ensure that the structure is correct.

### 2. PLANAR_AVERAGE.dat
During the VASP calculation, please set:

```bash
LCHARG = T
```
`PLANAR_AVERAGE.dat` is generated based on the resulting `CHGCAR`. It contains the charge density averaged over the x–y plane along the z-direction.

You can obtain this file using `VASPKIT` under your working directory:

```
(echo 316;echo 1;echo 3)|vaspkit
```

### 3. NGZF.txt
`NGZF.txt` contains the NGZF value, which represents the number of grid divisions along the z-direction in the VASP calculation.
It can be extracted from `OUTCAR` using:
```
grep NGZF OUTCAR | head -n 1 | awk '{print $8}' > NGZF.txt
```

### 4. val.json
`zval.json` contains the number of valence electrons for each element in the structure.  
It can be generated using the `val.py` script under your working directory:

```
python val.py
```
---
## Usage
Your data should be organized in the following directory structure:

```
base path/
├──material_1  
│├──POSCAR  
│├──NGZF.txt  
│├──val.json  
│├──PLANAR_AVERAGE.dat  
├──material_2  
│├──...  
├──material_3  
│├──...  
├──...
```

Before running polar.py, please ensure that the following Python packages are installed:
-numpy
-pymatgen
-pandas
-argparse

Run the script with:
```
python polar.py your\base\path
```

The output file `polar.csv` will be generated under the base path.  

Output Format


|material | polar|
| ----------- | ----------- |
|material_1 | polar_1  |
|material_2 | polar_2  |
|... | ...|


  








