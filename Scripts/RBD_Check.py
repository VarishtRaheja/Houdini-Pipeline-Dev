node = hou.pwd()
geo = node.geometry()

# Add code to modify contents of geo.
# Use drop down menu to select examples.

hda = hou.node("../")
list_names = geo.attribValue("name_lst")
num_names = len(list_names)
unique_vals = len(set(list_names))

# Checking to see how many duplicates exist.
names_freq = {}

# Get the parameter value from the source node. This will tell us which point number has the duplicate.
param_value = hou.node("/obj/RBD_CHECKER/creating_a_duplicate").parm("any_point_num").evalAsString() #Grabs the node from which the duplicate has been created.
repeated_names = ["{}".format(param_value)]
geo.addAttrib(hou.attribType.Global,"repeated_names",repeated_names)

# Check for duplicates
if num_names != unique_vals:
    for name in list_names:
        names_freq[name] = names_freq.get(name,0)+1
        
for names, freq in names_freq.items():
    if freq>1:
        repeated_names.append(names)
repeated_names.pop(0)
# print(repeated_names)

# Set the color of the node depending if duplicate exists or not.
if len(repeated_names) > 0:
    geo.setGlobalAttribValue("repeated_names",repeated_names)
    hda.setColor(hou.Color(1,0,0))
else:
    hda.setColor(hou.Color(0,1,0))