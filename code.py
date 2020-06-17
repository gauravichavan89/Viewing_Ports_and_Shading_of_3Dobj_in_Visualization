# -*- coding: utf-8 -*-
"""
Created on Mon Feb  4 06:58:47 2019

@author: gauravi
"""

import vtk

# Setting the background color as black for all ports
ColorBackground = [0.0, 0.0, 0.0]

#### Logic for View Port 1: Illustrating a wireframe representation with no texture or shading ####

# Importing and Reading .obj file from a location where I saved it on my system
# Please put the path of .obj file located on your system
FirstobjPath = r"apple_obj.obj"
reader = vtk.vtkOBJReader()
reader.SetFileName(FirstobjPath)
reader.Update()

# Creating view port 1
mapper = vtk.vtkPolyDataMapper()
mapper.SetInputConnection(reader.GetOutputPort())

# Mapping of the mapper to the actor
actor = vtk.vtkActor()
actor.SetMapper(mapper)

# Demonstrating the wireframe representation of the object
actor.GetProperty().SetRepresentationToWireframe()
#### end of core logic of view port 1 ####



#### Logic for View Port 3: Illustrating a surface representation of the object without shading or texture ####
actor2 = vtk.vtkActor()
actor2.SetMapper(mapper)
#### end of core logic of view port 3 ####



#### Logic for View Port 2: Displaying surface representaion with texture map but without shading ####
# Reading the texture image
jpegfile = r"apple_texture.jpg"

# Read the jpg image data from a file
reader1 = vtk.vtkJPEGReader()
reader1.SetFileName(jpegfile)
 
# Create texture object
texture = vtk.vtkTexture()
texture.SetInputConnection(reader1.GetOutputPort())

# Create mapper and view port
mapper = vtk.vtkPolyDataMapper()
mapper.SetInputConnection(reader.GetOutputPort())
 
# Create actor and set the mapper and mapped texture as input
actor1 = vtk.vtkActor()
actor1.SetMapper(mapper)
actor1.SetTexture(texture)
#### end of core logic of view port 2 ####



#### Logic for View Port 4: Displaying a Surface with texture map and Phong shading  ####
# Introducing an actor
actor3 = vtk.vtkActor()

# Compute normals
normals = vtk.vtkPolyDataNormals()
normals.SetInputConnection(reader.GetOutputPort())

# VTK pipeline for mapper and actor
mapper.SetInputConnection(normals.GetOutputPort())
actor3.SetMapper(mapper)
actor3.SetTexture(texture)

# Set object properties
prop = actor3.GetProperty()
prop.SetInterpolationToPhong() # Set shading to Phong
prop.ShadingOn()
prop.SetColor(1, 1, 0)
prop.SetDiffuse(0.8) # 0.8
prop.SetAmbient(0.3) # 0.3
prop.SetSpecular(1.0) # 1.0
prop.SetSpecularPower(100.0)

# Define light
light = vtk.vtkLight ()
light.SetLightTypeToSceneLight()
light.SetAmbientColor(1, 1, 1)
light.SetDiffuseColor(1, 1, 1)
light.SetSpecularColor(1, 1, 1)
light.SetPosition(-100, 100, 25)
light.SetFocalPoint(0,0,0)
light.SetIntensity(0.8)
#### End of core logic of view port 4 ####



# Rendering first view port 
ren1 = vtk.vtkRenderer()
ren1.SetViewport(0, 0.5, 0.5, 1)
ren1.AddActor(actor)
ren1.SetBackground(ColorBackground)

# Rendering second view port
ren2 = vtk.vtkRenderer()
ren2.SetViewport(0.5, 0.5, 1, 1)
ren2.AddActor(actor1)

# Rendering third view port
ren = vtk.vtkRenderer()
ren.SetBackground(ColorBackground)
ren.SetViewport(0, 0, 0.5, 0.5)
ren.AddActor(actor2)

# Rendering fourth view port
ren3 = vtk.vtkRenderer()
# Add the light to the renderer;
ren3.AddLight(light)
ren3.SetViewport(0.5, 0, 1, 0.5)
ren3.AddActor(actor3)

# Defining a rendering window
renWin = vtk.vtkRenderWindow()
renWin.SetSize(700, 700)

# Adding rendering elements to the window
renWin.AddRenderer(ren1)
renWin.AddRenderer(ren2)
renWin.AddRenderer(ren)
renWin.AddRenderer(ren3)
renWin.Render()



# Setting up an user interface interactor and passing it a rendering window as input
iren = vtk.vtkRenderWindowInteractor()
iren.SetRenderWindow(renWin)



# Exporting the rendered scene to a JPG ﬁle
w2i = vtk.vtkWindowToImageFilter()
w2i.SetInput(renWin)
w2i.Update()
writer = vtk.vtkJPEGWriter()
writer.SetInputConnection(w2i.GetOutputPort())
# Note: This file will be saved in the same location where you place the .py file
writer.SetFileName("JPG_of_Rendered_Scene.jpg")
renWin.Render()
writer.Write()



# finally enable user interface interactor
iren.Initialize()
iren.Start()
