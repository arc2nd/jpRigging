import maya.cmds as cmds

allSources = cmds.ls(selection=True)
allDests = cmds.ls(selection=True)

for i in range(len(allSources)):
	cmds.copySkinWeights(ss=allSources[i], ds=allDests[i], noMirror=True, sa='closestPoint', ia='closestJoint')