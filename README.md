# out-of-plane-polarization
A python program used for out-of-plane polarization in two-dimensional ferroelectrics

To calculate out-of-plane polarization, four files are needed, including POSCAR, zval.json, NGZF.txt and PLANAR_AVERAGE.dat.

POSCAR is the structure file of the material to be calculated. Please ensure that your POSCAR is correct. 

While performing VASP calculation, you need to set LCHARG = T. NGZF.txt and PLANAR_AVERAGE.dat are gained based on the resulting CHGCAR.

NGZF.txt contains the number of NGZF which means how many proportions the z direction length are divided into while VASP calculation. The file can be obtained in OUTCAR with following command.

<pre>''' grep NGZF OUTCAR | head -n 1 | awk '{print $8}' '''<pre>

PLANAR_AVERAGE.dat is a file processed from CHGCAR with VASPKIT. The charge density of x-y plane should be integrated. The following canmand helps you get the correct file.

<pre>'''(echo 316;echo 1;echo 3)|vaspkit'''<pre>

val.json includes the information of valence electrons of the elements in POSCAR. The val.py program can output the correct file with the following command.
<pre>'''python val.py'''<pre>

The data should be arranged in the tructure.
<pre> ## Directory Structure ```base_path/ ├── material1 │ ├── POSCAR │ ├── val.json │ ├── NGZF.txt │ ├── PLANAR_AVERAGE.dat ├── material1 ├── ... ``` </pre>







