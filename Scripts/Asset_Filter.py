import os
import re

node = hou.pwd()
geo = node.geometry()

# Created the path attribute
geo.addAttrib(hou.attribType.Point,"path","")
folder = hou.parm("root").eval()

# Recursively going through all dirs and sub-dirs. Created a generator function to optimise
# efficiency for large directory. 

# path = []
def generator_recursive_search(folder):
    """ Generator function to lazily search for files in directory to optimise efficiency. """

    for root,dir,files in os.walk(folder):
        replaced_root = root.replace(os.sep,"/")  #Escaping the backslash
        # yield files
        if len(files)>0:
            for f in files:
                # I am adding a .tif file here just for checking purposes.
                match = re.search(".bgeo.*|.OBJ|.abc|.fbx|.usd.*|.tif",f,re.M) #re.M = multiline
                if match:
                    yield "{}/{}".format(replaced_root,f)

for path_name in generator_recursive_search(folder):
    pt = geo.createPoint()
    pt.setAttribValue("path",path_name)