# Out-of-Plane Polarization

A Python program for calculating out-of-plane polarization in two-dimensional ferroelectric materials.

## Required Files

To calculate the out-of-plane polarization, the following four files are required:

- `POSCAR`
- `zval.json`
- `NGZF.txt`
- `PLANAR_AVERAGE.dat`

### POSCAR

`POSCAR` is the structure file of the material.  
Please ensure that the structure is correct.

---

## Preparing Required Files

### 1. CHGCAR generation

During the VASP calculation, please set:

```bash
LCHARG = T
```

PLANAR_AVERAGE.dat are generated based on the resulting CHGCAR.

### 2. PLANAR_AVERAGE.dat generation
PLANAR_AVERAGE.dat is a charge file being processed by VASPKIT. The charge density of x-y plane is intergated. Ensure that you have a CHGCAR, and obtain the file with 
```
(echo 316;echo 1;echo 3)|vaspkit
```

### 3. NGZF generation
NGZF.txt contains the NGZF value, which represents the number of grid divisions along the z-direction in the VASP calculation.

It can be extracted from OUTCAR using:
```
grep NGZF OUTCAR | head -n 1 | awk '{print $8}' > NGZF.txt
```

### 4. val.json generation
val.json is a file including elements and corresponding valance electrons. val.py can be use to obtain it with 
```
python val.py
```
### 4. PLANAR_AVERAGE.dat generation
PLANAR_AVERAGE.dat is a charge file being processed by VASPKIT. The charge density of x-y plane is intergated. Ensure that you have a CHGCAR, and obtain the file with 
```
(echo 316;echo 1;echo 3)|vaspkit
```

## Usage
Your data should be arranged in the following structure:
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

The output file polar.csv will be generated under the base path.
Output Format

|material | polar|
|material_1 | polar_1  |
|material_2 | polar_2  |
|... | ...|

  








