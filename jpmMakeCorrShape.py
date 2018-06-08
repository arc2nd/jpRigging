##James Parks
##07/12/12
##Makes corrective blend shapes

##get the bind geo
##dupe it and move to world space
##USER SCULPTS B SHAPE
##Make the parallel blend shape (A:-1, B:1)
##Return controls to zero (or turn off skinClusters
##Duplicate final corrective shape

import maya.cmds as cmds
import re

def jpmMCS_makeSculpt( bindGeo ):
	aShape = cmds.duplicate( bindGeo, n="NO_TOUCHY" )[0]
	bShape = cmds.duplicate( bindGeo, n="SCULPT_ME" )[0]
	cmds.parent( aShape, bShape, world=1 )
	
	bsNode = cmds.blendShape( aShape, bShape, bindGeo, parallel=1, n="temp_BLEND" )[0]
	cmds.setAttr( bsNode + "." + aShape, -1 )
	cmds.setAttr( bsNode + "." + bShape, 1 )
	
	print "Go forth and sculpt, my child"
	return bsNode
	
def jpmMCS_makeFinal( bindGeo, bsNode ):
	print "Make the final corrective shape"
	
	##Find the skinCluster and turn it off
	history = cmds.listHistory( bindGeo )
	
	allSCNodes = []
	for histNode in history:
		objType = cmds.objectType( histNode )
		if objType == "skinCluster":
			allSCNodes.append( histNode )
			cmds.setAttr( (histNode + ".envelope"), 0 )
			print histNode

	corrShape = cmds.duplicate( bindGeo, n="CORRECTIVE_SHAPE" )[0]
	cmds.parent( corrShape, world=1 )
	cmds.delete( bsNode )
	
	for scNode in allSCNodes:
		cmds.setAttr( (scNode + ".envelope"), 1 )
	return allSCNodes

def jpmSelectAllControls():
	thisObj = cmds.ls(sl=1)[0]

	splitName = re.split(":", thisObj)
	prefix = ""
	for i in (range(len(splitName)-1)):
		if prefix == "":
			prefix = splitName[i]
		else:
			prefix = prefix + ":" + splitName[i]

	cmds.select(prefix + ":*_CTRL")
	cmds.select(prefix + ":*_ctl", add=1)
	

def jpmMCSButtonPush(*args):
	print args
	if args[0] == "bind":
		cmds.textFieldGrp( "bindGeoGrp", e=1, tx=cmds.ls(sl=1)[0] )
		cmds.text( "statusTextGrp", e=1, l="", bgc=(0.27,0.27,0.27) )
	if args[0] == "blend":
		bindGeo = cmds.textFieldGrp( "bindGeoGrp", q=1, tx=1 )
		bsNode = jpmMCS_makeSculpt( bindGeo )
		cmds.optionVar( sv=( "jpMCS_bsNode", bsNode ) )
		cmds.text( "statusTextGrp", e=1, l="SCULPT NOW", bgc=(1,0,0) )
	if args[0] == "final":
		bindGeo = cmds.textFieldGrp( "bindGeoGrp", q=1, tx=1 )
		bsNode = cmds.optionVar( q=( "jpMCS_bsNode" ) )
		jpmMCS_makeFinal( bindGeo, bsNode )
		cmds.text( "statusTextGrp", e=1, l="DELETE \"NO_TOUCHY\" \nAND \"SCULPT ME\"", bgc=(0,1,0) )
	
def jpmMakeCorrShape():
	winName = "jpmMakeCorrShape"
	if ( cmds.window( winName, exists=True) ):
		cmds.deleteUI( winName )
	cmds.window( winName, t="Make Corrective Blends", rtf=True, mb=1 )
	
	cmds.rowColumnLayout( nc=1, cw=([1,200]) )
	cmds.rowColumnLayout( nc=2, cw=([1,75],[2,125]) )
	cmds.button( l="Bind GEO-->", width=75, c="jpmMCSButtonPush(\"bind\")" )
	cmds.textFieldGrp( "bindGeoGrp", cw=([1,120]), cal=([1,"left"]), tx="...bind geo..." )
	cmds.setParent( ".." )
	
	cmds.button( w=200, l="Will it BLEND???", c="jpmMCSButtonPush(\"blend\")" )
	cmds.text( l="" )
	cmds.text( "statusTextGrp", l="", h=50, fn= "boldLabelFont")
	
	cmds.button( w=200, l="Finalize", c="jpmMCSButtonPush(\"final\")" )
	
	
	cmds.showWindow( winName )