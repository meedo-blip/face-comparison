# Face Recognition and Comparison in Python
This is a repo that can compare two images of people 
to see whether or not they are the same person.

## Requirements 
1. Windows (Not tested on other platforms)
2. You must have *python 3.10* installed for compatibility
with certain packages.

You can check if you have it in the terminal with:
```
python3.10 --version
```

If an error occurs, install it [here](https://www.python.org/downloads/release/python-31011/)

## Setup and run (for windows)

1. Download this repo as a zip file and unzip it.

2. Go to start menu and search `powershell`, right click on the 
`Windows Powershell` and click *Run as administrator*
3. In the powershell type or paste the command:
```
Set-ExecutionPolicy Unrestricted
```
then press Enter. It will then ask you for permission
so type A and enter.

5. Go back to the unzipped folder and open it, then right click in the empty space under the files and click Open in Terminal.

6. In the terminal paste this
```
python3.10 -m venv face_env
```

7. Then do 
```
source face_env\Scripts\activate
```

This will activate the virtual enviroment.
8. do both commands (u can copy and paste this into terminal), 
```
pip install numpy==1.23.5
pip install cmake
```

9. Relax a bit : ), then install the prebuilt wheel files for dlib
for your windows arcitechures, for windows x64 click [here](https://github.com/z-mahmud22/Dlib_Windows_Python3.x/blob/main/dlib-19.22.99-cp310-cp310-win_amd64.whl)

10. Rename the file if it has a space and then right click on the file and click Copy ast Path.

11. Go back to the terminal and type `pip install *paste path to wheel file here*`
```
pip install "path/to/wheel/file"
```

12. Finally, do 
```
pip install face-recognition
```

13. To run example script do 
```
python recognise.py
```

14. Once youre done running the face_env eniroment,
 (Optional) go back to the administrator powershell and run:
```
Set-ExecutionPolicy Restricted
```

This is done for safety reasons but you cant source the venv in this mode.

Thank you for reading this and feel free to report any errors in issues, have a good day : )