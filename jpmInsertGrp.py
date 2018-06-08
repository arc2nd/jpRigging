import maya.cmds as cmds
import maya.mel as mm

import jpmConstraintSnap as snaps

def jpmInsertGrp( grpParent, grpName ):
	theseChildren = cmds.listRelatives( grpParent, c=1 )
	shapeChildren = cmds.listRelatives( grpParent, s=1 )
		
	for thisShapeChild in shapeChildren:
		thsesChildren.remove(thisShapeChild)
	
	if not cmds.objExists(grpName):
		thisGrp = cmds.group( name=grpName, empty=1 )
	else:
		thisGrp = grpName
	
	if cmds.objExists( grpParent ):
		cmds.parent( thisGrp, grpParent )
	else:
		print "Specified parent does not exist"
		
	snaps.jpmConstraintSnap( grpParent, thisGrp )
	
	if cmds.objExists( thisGrp ):
		cmds.makeIdentity( thisGrp, apply=1 )
	else:
		print grpName + " does not exist"
	
	cmds.parent( theseChildren, thisGrp )
		
	return thisGrp