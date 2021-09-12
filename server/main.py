from flask import Flask,request
from flask_restful import Resource, Api
import trimesh
app = Flask(__name__)
api = Api(app)

class task (Resource):

    def post (self, name):
        data = request.get_json()
        mesh = trimesh.load('turbine_optimized.stl')
        volume = mesh.volume
        surface_area = mesh.area
        bounding_box_parameters = mesh.bounding_box.extents
        bounding_cylinder_parameters = mesh.bounding_cylinder.extents
        return {"bounding_box" : bounding_box_parameters, "bounding_cylinder": bounding_cylinder_parameters, "volume":volume , "surface_area":surface_area}









api.add_resource(task,'/stl_file/<int:name>')
app.run(port= 5000,debug=True)
