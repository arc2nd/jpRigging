##James Parks 06/06/05
##jpmTypeFilterList.mel

##Given an array of objects (such as resulting from `ls -sl`) and an object 
##type string will return only the objects that are both in that list and 
##who are that object type

import maya.cmds as cmds

def jpmTypeFilterList(selected, filter):
	filterSelected = cmds.ls(typ=filter);
	bothSelected = []
	for obj in selected:
		for filteredObj in filterSelected:
			if obj == filteredObj:
				bothSelected.append(obj)
	return bothSelected