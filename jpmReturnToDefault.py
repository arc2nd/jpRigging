import maya.cmds as cmds
import re

def jpmReturnToDefault():
	zeroObjs = cmds.ls(sl=1)
	isTrans = []
	for thisObj in zeroObjs:
		isTrans = re.search("trans_CTRL", thisObj)
		if isTrans:
			continue
		else:
			allAttr = cmds.listAttr( thisObj, k=1 )
			for thisAttr in allAttr:
				if thisAttr == "visibility":
					continue
				defaultValue = cmds.attributeQuery( thisAttr, node=thisObj, ld=1 )
				cmds.setAttr( (thisObj + "." + thisAttr), defaultValue[0] )