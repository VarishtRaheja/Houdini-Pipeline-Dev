import os,hou

def backup_sel_nodes(hda_nodes):
    nodes = hda_nodes.parm("nodes_to_backup").evalAsString()
    list_nodes = nodes.split(" ")
    
    # Backing up the directory
    dir = hda_nodes.parm("backup_dir").evalAsString()
    backup_name = hda_nodes.parm("backup_name").evalAsString()
    
    dir_name = "{}/{}.py".format(dir,backup_name)
    
    # Check if path exists
    if os.path.exists(dir_name):
        hou.ui.displayMessage("Directory exists: {}".format(dir_name))
    else:
        for nodes in list_nodes:
            main_node = hou.node(nodes)
            if main_node != None and os.path.exists(dir):
                with open(dir_name,"a+") as f:
                    f.write(main_node.asCode(recurse=True))
                    
        # Displaying confirmation message            
        message = "Assets have been backed up to {}".format(dir_name)
        hda_nodes.parm("nodes_to_backup").set("")
        hou.ui.displayMessage(message)
        
        # changing color of node to showcase written to disk.
        c = hou.Color((1,1,1))
        hda_nodes.setColor(c)
    # print(dir_name)
    
# Function to read the .py nodes back in.
def read_backup(hda_nodes):
    filename = hda_nodes.parm("backup_file").evalAsString()
    if os.path.exists(filename):
        exec(open(filename).read())
        c = hou.Color((0,0,0))
        hda_nodes.setColor(c)