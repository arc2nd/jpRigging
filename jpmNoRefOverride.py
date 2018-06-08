import maya.cmds as cmds

objs = cmds.ls(sl=True)

for thisObj in objs:
	shape = cmds.listRelatives(thisObj, shape=True, path=True)
	print shape
	if shape[0] != "":
		cmds.setAttr(shape[0] + ".overrideEnabled", 0)
	cmds.setAttr(thisObj + ".overrideEnabled", 0)