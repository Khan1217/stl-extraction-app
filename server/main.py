from flask import Flask,request
from flask_restful import Resource, Api
from flask_cors import CORS
import trimesh
import base64
import io
app = Flask(__name__)
CORS(app)
api = Api(app)



class task (Resource):

    def post (self):
        mesh = trimesh.load(io.BytesIO(request.data),"stl")
        volume = mesh.volume
        print(volume)
        surface_area = mesh.area
        width, length , height  = mesh.bounding_box.extents

        length_of_cylinder = height
        diameter_of_bounding_cylinder = max (width, length)

        return {"volume":volume,"surface_area":surface_area,"length":length,"width":width,"height" :height , "length_of_cylinder":length_of_cylinder, "diameter_of_cylinder":diameter_of_bounding_cylinder}









api.add_resource(task,'/stl_file')
app.run(port= 5000,debug=True)
