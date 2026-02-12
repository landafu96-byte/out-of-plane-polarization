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

'''bash
LCHARG = T
'''

Both NGZF.txt and PLANAR_AVERAGE.dat are generated based on the resulting CHGCAR.

### 2. NGZF generation
NGZF.txt contains the NGZF value, which represents the number of grid divisions along the z-direction in the VASP calculation.

It can be extracted from OUTCAR using:
'''
grep NGZF OUTCAR | head -n 1 | awk '{print $8}'
'''






