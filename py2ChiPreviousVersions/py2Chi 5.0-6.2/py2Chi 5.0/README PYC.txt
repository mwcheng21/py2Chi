py2Chi version 1.0 7/19/2017

------------------------
I. CONTENTS OF THIS FILE
------------------------
 *Introduction
 *General Usage Notes
 *Using the Program
 *Troubleshooting/FAQ
 *Sources/Documentaion
 *Developer

----------------
II. INTRODUCTION
----------------
 A. ProtCid is a database of similar protein-protein interfaces in crystal structures of homologous proteins. Its main goal is to identify and cluster homodimeric and heterodimeric interfaces observed in multiple crystal forms of homologous proteins. 
 B. Currently ProtCID generates .pml files which can only be read in the open-source modeling software pyMol
 C. This program allows the user to convert ProtCID pyMol scripts (.pml) to scripts that can be read by UCSF Chimera in the form of .py scripts.

------------------------
III. GENERAL USAGE NOTES
------------------------
 *Must have Python 2.7 installed
 *Scripts and software tested and confirmed on Windows 7 using Chimera 1.11.2
 *In some cases, the alignments are not working very well, manual adjustment is necessary. For more details, see http://dunbrack2.fccc.edu/ProtCiD/Default.aspx
---------------------
IV. USING THE PROGRAM
---------------------
 A. Running the Program
   1. Run the cooresponding py2Chi executible by double clicking the py2Chi.exe for your system. py2Chi32 for a 32 bit machine and py2Chi64 for a 64 bit machine
   2. Select the pml file(s) you would like to convert
   3. The file will be opened with Chimera
   4. A .py file will be created in the same folder as the pyMol file
   5. To open again, right click this .py and select open with, chimera

 B. Limitations
   1. Unlike pyMol, Chimera does not allow a subset of a chain to be colored. In pyMol, some scripts will rainbow a chain by domain. In chimera, the cooresponding representation is coloring the domain by a random color. Rainbowing can be done manually with "rainbow [atomspec]"
   2. ProtCID pyMol scripts select ligands as separate objects. Chimera cannot select certain groups of ligands and place them in the model panel so the converted Chimera scripts place them as separate selectable objects. Run the command namesel to see the list of specified Ligands.
----------------------
V. TROUBLESHOOTING/FAQ
----------------------
 Q. Chimera won't load the script or isn't responding
 A. Depending on the size and complexity of the protein being loaded, Chimera can handle the loading and aligning in the script approximately 1 protein per second. Check the bottom left corner of the Chimera window to see if it is running the script. 

 Q. I get an error with "from chimera import runCommand"
 A. Try right clicking the .py file and select open with -> Chimera

 Q. I get an error "Cannot find chimera" or a "WindowsError"
 A. Make sure you have a chimera version 1.10.1 - 1.11.2. Make sure it is installed in C:\Program Files

 Q. I can't select open with -> Chimera
 A. Right click, select open with -> choose program -> Browze -> Chimera 1.(11.2) -> bin -> Chimera
 
 Q. Type selection window pops up or I get a "No such file or directory"
 A. The ProtCID folder/ the scripts to be converted must be in the C:/ directory

 Q. I dont see Chimera 1.XX.XX
 A. Assuming it is installed in the default area, go to C:\Program Files

 Q. Chimera is the now the default for opening .py files or I don't want it to be default
 A. Open the .py file with chimera then right click -> open with -> choose default program -> python(.exe). Your system should now open .py files with python. There should also be an option under the "open with" to open them one time with chimera
 
 Q. I don't see python(.exe)
 A. The default location of python(.exe) is in C:\Python27

 Q. I get a "MemoryError: not enough memory"
 A. Get a better system


-------------------------
VI. SOURCES/DOCUMENTATION
-------------------------
http://dunbrack2.fccc.edu/ProtCiD/Default.aspx
---------------
VIII. DEVELOPER
---------------
 * Bugs, requests, missing features, questions, and comments can be reported to Micah Cheng at Micah.Cheng21@gmail.com
 *Please use the correct [TAG] and a detailed description in the subject line (i.e [Bug]-bug info)