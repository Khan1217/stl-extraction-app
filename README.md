# stl-extraction-app
Stl-extraction app
This app takes an stl file as an input and extract the following details and show them on front end web page.
surface area of stl mesh 
volume 
bounding box and bounding cylinder parameters
Server-end
Library trimesh is used to extract these details. 
It converts stl 3d diagram into triangular meshed. then sum of surface areas of every mesh is calculated to calculate the overall surface area. 
The mesh is watertight .
The bounding cylinder is considered as round shape enclosing our object.
These details are then extracted and displayed on front end web interface. 
