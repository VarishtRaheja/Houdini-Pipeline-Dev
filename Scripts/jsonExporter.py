# Importing the libs
import os,json, hou
from pxr import Usd, UsdGeom 

def get_transform(obj,time):
    """ This function extracts the translation and rotation data
        using matrix4. """
    obj = hou.node(obj)
    transformation_data = obj.worldTransformAtTime(time)
    translate = transformation_data.extractTranslates()
    rots = transformation_data.extractRotates()
    scales = transformation_data.extractScales()
    return translate,rots,scales
    

# Function to create JSON
def export_json(time):
    hda_node = hou.pwd()
    objs = hda_node.parm("object_list").eval().split()
    json_data = {
        "time": time, 
        "objects":[] 
    }
    for obj in objs:
        translate, rot, scales = get_transform(obj,time)
        data = {
            "name":hou.node(obj).name(),
            "translate":list(translate),
            "rotate":list(rot),
            "scale":list(scales)
        }
        json_data["objects"].append(data)
        json_string = json.dumps(json_data,indent=4)
        save_file = os.getenv("HIP")+"/scripts"
        destination_path = "{}/transform_to_json.json".format(save_file)
        with open(destination_path,"w+") as f:
            f.write(json_string)
        # print(json_string)
        
        
def import_usd():
    """ Function to create a USD file and import directly into Houdini. This is WIP..."""
    # Load JSON data
    des_path = os.getenv("HIP")+"/scripts/transform_to_json.json"
    with open(des_path, "r") as file:
        scene_data = json.load(file)

    # Create a new USD stage
    stage = Usd.Stage.CreateNew("output1.usd")

    # Iterate through JSON and add objects
    for obj in scene_data["objects"]:
        if obj["name"] == "box_object1":
            usd_object = UsdGeom.Cube.Define(stage, f'/{obj["name"]}')
            print(usd_object)
    
            # Set object position
            # usd_object.AddTranslateOp().Set(obj)

    # Save the USD file
    stage.GetRootLayer().Save()

    print("USD scene successfully created!")
