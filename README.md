# Houdini HDA and Python Scripts

Welcome to the Houdini HDA and Python Scripts repository! This project contains various Houdini Digital Assets (HDA) and Python scripts to streamline workflows, automate tasks, and enhance functionality within Houdini.

## Features
- Custom Houdini Digital Assets (HDA) for procedural workflows.
- Python scripts to extend Houdini functionality.
- Automation tools for simplifying repetitive tasks.
- Well-documented code for ease of use and integration.

<break>

### Projects:
1. [Backup Tool](#backupTool)
2. [Json Exporter](#jsonExporter)
3. [RBD Attributes Checker](#rbd-checker)



### Documentation
<a id="backupTool">1. In this hda you can create a backup tool of any node by using the operator list to select the nodes you want to backup and this will be converted into a .py file with all the modifications saved. Doc to follow

<a id="jsonExporter">2. In this program a HDA has been created to select the nodes(Geomtry context) to export them in JSON format which can be read in cross platform applications for quick export/import. Further research into converting JSON to USD is underway.</a>
   - Doc to follow.

#### 3. RBD Checker

+ The python script can be found here: [Code](https://github.com/VarishtRaheja/Houdini-Pipeline-Dev/blob/main/Scripts/RBD_Check.py)

<a id="rbd-checker">In this script I have combined both VEX and Python to check for duplicated names<i>(name attribute)</i>. I have also added a feature to change the color of the node to see if duplicate names exist. Red for duplicates and green is good to go.
   <p> Lets start with creating a simple voronoi fracture with a basic 3d geometry shape(box)
   
   ![Simple Voronoi Fracture setup](./images/rbd-checker/Task3.jpg)

   Then create a wrangle node to manually "fake" a duplication by doing the following.

   ![Create a duplicate](./images/rbd-checker/Task4.jpg)

   I have bypassed the wrangle node here to show you that we can create an event to change the color of the node depending on cerain actions. So if the duplicate does not exist then the node turns green else red in color.

   ![Change in color](./images/rbd-checker/Task5.jpg)

   Then I have created a wrangle to initialise an empty list and add all the points with their corresponding name attribute.

   ![Appending to empty list](./images/rbd-checker/Task6.jpg)

   This is the main part of the python code where the color of the node is being set and the names are being registered to a list which are not duplicates. The duplicated name is then conditioned check and passed downstream as an attribute to keep proceduralism alive. This is then being split based on the attribute and we can visulise it by adding a different color attribute to each stream before merging it back together.

   ![Split the attribute](./images/rbd-checker/Task7.jpg)

   ![Visualisation](./images/rbd-checker/Task9.jpg)


---

## Steps to download and install HDA

Installing the HDA in Houdini
1. Method: Manual Installation
- Open Houdini.
- Go to Assets -> Install Asset Library.
- Locate the .hda file on your computer and select it.
- Click Install.

<break>

2. Method: Installing in Houdini Preferences
- Place the .hda file in your Houdini preferences folder:
Documents/HoudiniXX.X/otls/
- (Replace XX.X with your Houdini version, e.g., 20.5.)
- Restart Houdini, and it should automatically load the asset.

---