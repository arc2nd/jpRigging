##James Parks
##06-15-12
##Create rivets along a NURBS surface at the specified uPos, vPos


##jpmMakeRivet(object, uPos, vPos)		


import maya.cmds as cmds
import maya.mel as mm
##import math
##import os
##import sys


def jpmMakeRivet(object, rivetName, uPos, vPos):
	allRivets = []
	allPosis = []
	allAims = []
	
	#Make locator and PointOnSurfaceInfo node
	thisLoc = cmds.spaceLocator( n=(rivetName + "_loc") )[0]
	thisPosi = cmds.createNode( "pointOnSurfaceInfo", n=(rivetName + "_posi") )
	cmds.setAttr( (thisPosi + ".turnOnPercentage"), 0 )
	cmds.setAttr( (thisPosi + ".parameterU"), uPos )
	cmds.setAttr( (thisPosi + ".parameterV"), vPos )
	cmds.connectAttr( (object + ".ws"), (thisPosi + ".is") )
			
	##Make the aimConstraint
	thisAim = cmds.createNode( "aimConstraint", n=(rivetName + "_aim"), p=thisLoc )
	cmds.setAttr( (thisAim + ".tg[0].tw"), 1 )
	cmds.setAttr( (thisAim + ".a"), 0, 1, 0, type="double3" )
	cmds.setAttr( (thisAim + ".u"), 0, 0, 1, type="double3" )
	cmds.setAttr( (thisAim + ".v"), k=0 )
	cmds.setAttr( (thisAim + ".tx"), k=0 )
	cmds.setAttr( (thisAim + ".ty"), k=0 )
	cmds.setAttr( (thisAim + ".tz"), k=0 )
	cmds.setAttr( (thisAim + ".rx"), k=0 )
	cmds.setAttr( (thisAim + ".ry"), k=0 )
	cmds.setAttr( (thisAim + ".rz"), k=0 )
	cmds.setAttr( (thisAim + ".sx"), k=0 )
	cmds.setAttr( (thisAim + ".sy"), k=0 )
	
	cmds.setAttr( (thisAim + ".sz"), k=0 )
	allRivets.append(thisLoc)
	allPosis.append(thisPosi)
	allAims.append(thisAim)
	
	##Connect stuff up
	cmds.connectAttr( (thisPosi + ".position"), (thisLoc + ".translate") )
	cmds.connectAttr( (thisPosi + ".n"), (thisAim + ".tg[0].tt") )
	cmds.connectAttr( (thisPosi + ".tv"), (thisAim + ".wu") )
	cmds.connectAttr( (thisAim + ".crx"), (thisLoc + ".rx") )
	cmds.connectAttr( (thisAim + ".cry"), (thisLoc + ".ry") )
	cmds.connectAttr( (thisAim + ".crz"), (thisLoc + ".rz") )
	
	return allRivets