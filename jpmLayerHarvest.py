##James Parks

import maya.cmds as cmds
import maya.mel as mm
import shutil
import os
import os.path
import jpmWriteShaders as ws
import jpmSaveToFile as aw_save
import jpmRestoreFromFile as aw_restore
import jpmLayerMaker as lm

def jpmLayerHarvest():
	currentSort = 1
	currentSort = cmds.optionVar( q="jpmLHalpha" )
	
	#Handle path
	path = cmds.optionVar( q="jpmLHpath" )
	if path == 0:
		jpmLH_setPathDialog()
		path = cmds.optionVar( q="jpmLHpath" )
		

	winName = "jpmLayerHarvest"
	if ( cmds.window( winName, exists=True) ):
		cmds.deleteUI( winName )
	cmds.window( winName, t="Layer Harvest", rtf=True, mb=1 )
	
	fileMenu = cmds.menu( "jpmLH_fileMenu", l="File" )
	cmds.menuItem( "jpmLH_setPathMenuItem", l="Set Path...", c="jpmLH_setPathDialog()" )
	cmds.menuItem( "jpmLH_printPathMenuItem", l="Print Path", c=( "print \"" + str(path) + "\"" ) )
	cmds.menuItem( "jpmLH_batchMenuItem", l="Batch...", p=fileMenu, c="jpmLH_batchDialog()" )
	cmds.menuItem( "jpmLH_writeMenuItem", l="Write...", p=fileMenu, c="jpmLH_writeDialog()" )
	cmds.menuItem( "jpmLH_harvestMenuItem", l="Harvest...", p=fileMenu, c="jpmLH_harvest()" )

	sortMenu = cmds.menu( "jpmLH_sortMenu", l="Sort" )
	cmds.radioMenuItemCollection( "jpmLH_sortMethod" )
	cmds.menuItem( "jpmLH_listAlpha", l="Alpha", rb=currentSort, cl="jpmLH_sortMethod", c="jpmLH_populateFileList(1)", p=sortMenu )
	cmds.menuItem( "jpmLH_listCreation", l="Creation", rb=(not currentSort), cl="jpmLH_sortMethod", c="jpmLH_populateFileList(0)", p=sortMenu )
	
	
	#form and layout
	jpmLH_form = cmds.formLayout( "jpmLH_form", nd=100 )
	cmds.rowColumnLayout( "jpmLH_topLayout", nc=1, cw=[1,300] )
	
	#name field and write new file button
	nameField = cmds.rowColumnLayout( nc=2, cw=([1,190],[2,100]) )
	cmds.textFieldGrp( "jpmLH_layerNameGrp", l="Harvest Name", cw=([1,80],[2,110]), cal=([1,"left"],[2,"left"]), tx="...Harvest Name..." )
	cmds.button( w=100, l="Harvest", c="jpmLH_collectAndCall()" )
	
	#file list
	cmds.setParent(jpmLH_form)
	fileList = cmds.textScrollList( "jpmLH_fileList", ams=0, w=165, dcc="jpmLH_applyHarvestFile()", dkc="jpmLH_deleteFile()" )

	#RMB pop up menu for the file list
	cmds.popupMenu( b=3, p=fileList )
	cmds.menuItem( l="Apply Selected", c="jpmLH_applyHarvestFile()" )
	cmds.menuItem( l="Rename Selected...", c="jpmLH_renameFileWin()" )
	cmds.menuItem( l="Name --->", c="jpmLH_popUpName()" )
	cmds.menuItem( divider=1 )
	cmds.menuItem( l="Delete Selected", c="jpmLH_deleteFile()" )

	#attach the file list to the re-sizing window
	cmds.formLayout( jpmLH_form, e=1, af=([fileList,"top",25],[fileList,"left",0],[fileList,"bottom",0],[fileList,"right",0]) )
	
	#re-populate the file list
	jpmLH_populateFileList(currentSort)
	
	cmds.showWindow( winName )



def jpmLH_collectAndCall():
	name = cmds.textFieldGrp( "jpmLH_layerNameGrp", q=1, tx=1 )
	jpmLH_harvest(name)

def jpmLH_harvest(name):
	layers = cmds.ls( type="renderLayer" )
	layers.sort()

	selected = cmds.ls( sl=1 )
	
	path = cmds.optionVar( q="jpmLHpath" )
	noPath = ""
	if path == "0":
		noPath = cmds.confirmDialog( t="Set A Path", ma="center", m="You Must Set A Path", b="OK" )
	if noPath == "OK":
		jpmLH_setPathDialog()
		
	fullname = path + "/" + name + ".harvest"
	
	folder = os.path.splitext(fullname)[0]
	if not os.path.exists(folder):
		os.mkdir(folder)
	
	layerString = ""
	for layer in layers:
		layer = layer.split(":")[-1]
		if layer != "defaultRenderLayer":
			cmds.editRenderLayerGlobals( crl=layer )
			members = cmds.editRenderLayerMembers( layer, q=1, fn=1)
			
			shaderFileName = folder + "/" + layer + ".SHD"
			selFileName = folder + "/" + layer + ".slc"
			
			ws.jpmSaveShadersToFile(shaderFileName, members)
			aw_save.jpmSaveSelectionToFile(selFileName, members)
			layerString = layerString + layer + "|" + shaderFileName + "|" + selFileName + "\n"
			
	saveFile = file(fullname, "w+")
	saveFile.write(layerString)
	saveFile.close()
	
	currentSort = 1
	currentSort = cmds.optionVar( q="jpmLHalpha" )
	#re-populate the file list
	jpmLH_populateFileList(currentSort)

def jpmLH_applyHarvestFile():	
	##get the path and filename information
	##read each line of the file in and evaluate it
	## as a python command
	path = cmds.optionVar( q="jpmLHpath" ) + "/"
	name = cmds.textScrollList( "jpmLH_fileList", q=1, si=1 )[0]
	fullname = path + name

	thisFile = open(fullname)
	allLines = thisFile.readlines()
	thisFile.close()

	for line in allLines:
		cmds.select(cl=1)
		layer, shaderFile, selectFile = line.split("|")
		layer = layer.strip()
		shaderFile = shaderFile.strip()
		selectFile = selectFile.strip()

		lm.jpmMakeLayer(layer)
		aw_restore.jpmRestoreFromFile(selectFile, 0, 0, "add", 0)

		cmds.editRenderLayerGlobals( crl=layer )
		sel = cmds.ls(sl=1)
		cmds.editRenderLayerMembers( layer, sel, nr=0 )
		
		if os.path.exists(shaderFile):
			thatFile = open(shaderFile)
			shaderLines = thatFile.readlines()
			thatFile.close()
			for shaderLine in shaderLines:
				eval(shaderLine)		

	
def jpmLH_batchDialog():
	cmds.fileBrowserDialog( m=0, fc=jpmLH_batch, an='Pick Batch File' )

def jpmLH_batch( fileName, fileType):
	layers = jpReadLines(fileName)
	for layer in layers:
		jpmMakeLayer(layer)
	return 1
	
def jpmLH_popUpName():
	#take the currently selected file and put it in the GUI's name field
	name = cmds.textScrollList( "jpmLH_fileList", q=1, si=1)[0]
	name,ext = os.path.splitext(name)
	cmds.textFieldGrp( "jpmLH_layerNameGrp", e=1, tx=name )
	
def jpmLH_deleteFile():	
	##get the path and filename information
	##move the file to filename.deleted
	##re-populate the file list
	currentSort = cmds.optionVar( q="jpmLHalpha" )

	path = cmds.optionVar( q="jpmLHpath" ) + "/"
	name = cmds.textScrollList( "jpmLH_fileList", q=1, si=1 )[0]
	fullname = path + name
	shutil.move( fullname, fullname + ".deleted" )
	jpmLH_populateFileList(currentSort)

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


def jpmLH_writeDialog():
	cmds.fileBrowserDialog( m=1, fc=jpmLH_write, an='Save Layers' )

def jpmLH_write( fileName, fileType):
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
	
def jpmLH_setPathDialog():
	cmds.fileBrowserDialog( m=4, fc=jpmLH_setPath, an='Set Layer Harvest Path' )

def jpmLH_setPath( fileName, fileType):
	cmds.optionVar( sv=["jpmLHpath",fileName] );
	currentSort = cmds.optionVar( q="jpmLHalpha" )
	jpmLH_populateFileList(currentSort)
	return 1
	
	
def jpmLH_populateFileList(alpha):
	##get the path information
	##clear the file list
	##get a list of all files .harvest in the path
	##add each file to the file list
	
	path = cmds.optionVar( q="jpmLHpath" ) + "/"
	cmds.optionVar( iv=("jpmLHalpha", alpha) )
	
	if path == "0":
		jpmLH_setPathDialog()
	harvestFiles = []
	cmds.textScrollList( "jpmLH_fileList", e=1, ra=1 )
	harvestFiles = cmds.getFileList( fld=path, fs="*.harvest" )
	if alpha:
		if len(harvestFiles) > 1:
			harvestFiles.sort()
	if harvestFiles != "":
		for harv in harvestFiles:
			cmds.textScrollList( "jpmLH_fileList", e=1, a=harv )