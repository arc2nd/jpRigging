myPath = "U:\BNS_Tech\BNS_Pipeline\JamesParks_Scripts\Mayascripts\jpPython"
import sys
sys.path.append(myPath)

import maya.cmds as cmds
import maya.mel as mm
from jpmTypeFilterList import *

def jpmSelectGeo():
	new_pwObjs = ["foo"]
	old_pwObjs = ["bar"]

	while old_pwObjs[0] != new_pwObjs[0]:
		old_pwObjs[0] = new_pwObjs[0]
		new_pwObjs = cmds.pickWalk( direction="up" )

	print new_pwObjs
	print old_pwObjs
	
	cmds.select( new_pwObjs[0], hi=1)
	heir = cmds.ls( tr=0, sl=1 )

	print heir

	polys = jpmTypeFilterList(heir, "mesh")
	nurbs = jpmTypeFilterList(heir, "nurbsSurface")

	print polys
	print nurbs

	allShapes = []
	allShapes.extend(polys)
	allShapes.extend(nurbs)

	print allShapes

	allObjs = []
	for shape in allShapes:
		allObjs.extend(cmds.listRelatives( shape, allParents=True ))
	cmds.select(cl=1)
	print allObjs

	for obj in allObjs:
		cmds.select(obj, add=1)


jpmSelectGeo()