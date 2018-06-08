##James Parks

import maya.cmds as cmds
import maya.mel as mm

def jpmLayerMaker():
	winName = "jpmLayerMaker"
	if ( cmds.window( winName, exists=True) ):
		cmds.deleteUI( winName )
	cmds.window( winName, t="Layer Maker", rtf=True, mb=1 )
	
	fileMenu = cmds.menu( "jpmLM_fileMenu", l="File" )
	cmds.menuItem( "jpmLM_batchMenuItem", l="Batch...", p=fileMenu, c="jpmLM_batchDialog()" )
	cmds.menuItem( "jpmLM_writeMenuItem", l="Write...", p=fileMenu, c="jpmLM_writeDialog()" )
	
	cmds.rowColumnLayout( nc=1, cw=[1,200] )
	cmds.textFieldGrp( "layerNameGrp", l="Layer Name", cw=([1,80],[2,120]), cal=([1,"left"],[2,"left"]), tx="...Layer Name..." )
	cmds.button( w=200, l="Make That Layer, Baby!!!", c="jpmLMCollectAndCall()" )

	cmds.showWindow( winName )

def jpmLMCollectAndCall():
	name = cmds.textFieldGrp( "layerNameGrp", q=1, tx=1 )
	jpmMakeLayer(name)

def jpmMakeLayer(name):
	allLayers = cmds.ls( et="renderLayer")
	layerExists = 0

	for layer in allLayers:
		if name == layer:
			layerExists = 1

	if not layerExists:
		cmds.createRenderLayer( name=name,  number=1, empty=1, mc=1)
		cmds.editRenderLayerAdjustment( "defaultRenderGlobals.imageFilePrefix", lyr=name )
		cmds.setAttr(  "defaultRenderGlobals.imageFilePrefix", name, type="string" )
		cmds.setAttr( (name + ".renderable"), 0 )
		print ("Layer " + name + " made\n")
	else:
		print ("Layer " + name + " already exists")

def jpmLM_batchDialog():
	cmds.fileBrowserDialog( m=0, fc=jpmLM_batch, an='Pick Batch File' )

def jpmLM_batch( fileName, fileType):
	layers = jpReadLines(fileName)
	for layer in layers:
		jpmMakeLayer(layer)
	return 1

def jpReadLines( fileToRead):
	lines = []
	badLines = []

	if os.path.exists(fileToRead) == False:
		print "File Not Found"
	else:
		thisFile = file(fileToRead, "r+")
		badLines = thisFile.readlines()
		thisFile.close()
	for i in range(0, len(badLines)):
		lines.append(badLines[i].strip())
	return lines

def jpmLM_writeDialog():
	cmds.fileBrowserDialog( m=1, fc=jpmLM_write, an='Save Layers' )

def jpmLM_write( fileName, fileType):
	layers = cmds.ls( type="renderLayer" )
	layers.sort()
	
	layerString = ""
	for layer in layers:
		layer = layer.split(":")[-1]
		if layer != "defaultRenderLayer":
			layerString = layerString + layer + "\n"
			
	saveFile = file(fileName, "w+")
	saveFile.write(layerString)
	saveFile.close()