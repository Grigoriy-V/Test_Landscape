import subprocess
import os
import sys

houdini_lib_path = "C:/Program Files/Side Effects Software/Houdini 20.5.278/houdini/python3.11libs"
houdini_bin_path = "C:/Program Files/Side Effects Software/Houdini 20.5.278/bin"
sys.path.append(houdini_lib_path)
os.add_dll_directory(houdini_bin_path)

import hou

try:
    hou.hipFile.load("scene_for_script.hip")
except hou.LoadWarning as e:
    print(e)

import hqueue.houdini as hq 

node = hq.getNode("/obj/test_landscape/import_parms") 
disp_node = node.displayNode() 
disp_node.executeGraph(False, True, False)

node = hq.getNode("/obj/test_landscape/Export") 
disp_node = node.displayNode() 
disp_node.executeGraph(False, True, False)
