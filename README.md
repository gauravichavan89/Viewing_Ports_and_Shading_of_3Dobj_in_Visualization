# Viewing Ports and Shading of 3D object in Visualization


The aim of this short assignment is to create multiple view ports to compare different types of representation of objects, namely, wireframe, surface, surface with texture map and texture mapping with Phong shading.


## Getting Started


The following instructions shall ensure that the assignment is up and running on your local machine for
development and testing purposes. See ‘Running the tests’ section to know how to run the assignment.


## Prerequisites


Software Required: Python 2.7 (Anaconda3 2018.12 64 bit) for Windows 10 as IDE
Package Required : vtk


## Installation


* Follow the instructions in the documentation https://docs.anaconda.com/anaconda/install/windows/
for downloading Python version 2.7 for Anaconda 2018.12 for Windows Installer.
* After launching the Anaconda Navigator, create a new environment for running vtk programs
by referring to the following documentation:
https://docs.anaconda.com/anaconda/navigator/tutorials/manage-environments/#creating-a-new-environ
ment
* Import vtk, numpy and scipy packages into this newly created environment by following the
guidelines specified in:
https://docs.anaconda.com/anaconda/navigator/tutorials/manage-packages/#installing-a-package
* In the Anaconda Navigator, click ‘Home’ on the left panel, then choose the newly created
environment for running the vtk programs from the drop down provided under ‘Applications on’ located
on the top most section of the navigator.
* Click on the ‘Install’ button under Spyder. On completing the installation click the ‘Launch’ button
under it.


## Running the tests


Upon launching the spyder application, copy paste the code from code.py file and save it on your local
machine. The code.py file is provided in the zip file of the submitted assignment. Now run the code by
clicking the green play button provided in the title bar of the application.


## Expected Successful Test Results: 


You would see a visualization pop up window with black background and four different representations of 3D apple objects. The first view port shall have a wireframe without any shading and texture, second view port will have the texture read from texture.jpg
mapped on the apple object, third view port will have just the surface without any texture or shading and
the fourth one will have the texture with Phong shading mapped on the object. All 4 objects can be
rotated in this window to see the effect from all sides especially the fourth one which includes shading
and lighting. A jpg file of the rendered scene will also be saved in the same location as the python file.


## Explanation of what and how the test performs


* View Port 1: A wireframe of apple object is displayed without shading or texture (what is displayed)
Significant classes/methods used: SetRepresentationToWireframe() (how is it displayed)

* View Port 2: Mapping of texture from jpg file on the object from .obj file without shading
Significant classes used: vtkJPEGReader(), SetTexture()

* View Port 3: Surface representation without shading and texture
Significant classes used: vtkOBJReader()

* View Port 4: Texture mapping with Phong shading
Significant classes used: vtkPolyDataNormals(), SetInterpolationToPhong()

* Exporting JPG format of the rendered scene
Significant classes used: vtkWindowToImageFilter(), vtkJPEGWriter()


## References
[1] https://vtk.org/doc/nightly/html/annotated.html
[2] https://github.com/Kitware/VTK
