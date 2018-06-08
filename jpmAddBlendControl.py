##James Parks
##01-26-04
##jpAddBlendControl.mel

##This script creates an assymetric blend shape controller 
##complete with translate limits, visual indicator of said 
##limits, user defined left/right attributes to connect to 
##your blend shapes, and the expression to control the 
##left/right attributes

##05/25/12
##replaced expression with a node network

##############################/
##make the blend controller
##stolen from the .ma file of the
##one I made by hand
##############################/

import maya.cmds as cmds
import maya.mel as mm

def makeBlendControl( controlName, plusMinus=[] ):
	#################################
	##Determing Limits for Controller
	#################################
	minX = -0.5
	maxX = 0.5
	minY = 0
	maxY = 1
	
	negX = plusMinus[0]
	plusX = plusMinus[1]
	negY = plusMinus[2]
	plusY = plusMinus[3]
	
	if plusX:
		maxX = 0.5
	else:
		maxX = 0
		
	if negX:
		minX = -0.5
	else:
		minX = 0
		
	if plusY:
		maxY = 1
	else:
		maxY = 0
		
	if negY:
		minY = -1
	else:
		minY = 0

	
	######################/
	##BaseBlendControllerSpace
	######################/
	spaceNode = cmds.createNode( "transform", n=(controlName + "BlendControlSpace") )
	cmds.setAttr( (spaceNode + ".rp"), 0.5, 0, 0, type="double3" )
	cmds.setAttr( (spaceNode + ".sp"), 0.5, 0, 0, type="double3" )
	spaceShapeNode = cmds.createNode( "nurbsCurve", n=(controlName + "BlendControlSpaceShape"), p=spaceNode )
	cmds.setAttr( (spaceShapeNode + ".v"), k=0 )
	tempCmd = """
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1.4142135623730949 2.8284271247461898 4.2426406871192848 5.6568542494923797
		
		5
		:::NEGX::: :::POSY::: 0	
		:::NEGX::: :::NEGY::: 0
		:::POSX::: :::NEGY::: 0
		:::POSX::: :::POSY::: 0
		:::NEGX::: :::POSY::: 0
		;
	"""
	
	print tempCmd
	
	tempCmd = tempCmd.replace(":::POSY:::", str(maxY) )
	tempCmd = tempCmd.replace(":::NEGY:::", str(minY) )
	tempCmd = tempCmd.replace(":::POSX:::", str((maxX + 0.5)) )
	tempCmd = tempCmd.replace(":::NEGX:::", str((minX + 0.5)) )
	mm.eval(tempCmd)

	####################/
	##BaseBlendController
	####################/
	ctrlNode = cmds.createNode( "transform", n=(controlName + "_CTRL"), p=spaceNode )
	cmds.addAttr( ctrlNode, sn="upLeft", ln="upLeft", min=0, max=1, at="double" )
	cmds.addAttr( ctrlNode, sn="upRight", ln="upRight", min=0 ,max=1, at="double" )
	cmds.addAttr( ctrlNode, sn="downLeft", ln="downLeft", min=0, max=1, at="double" )
	cmds.addAttr( ctrlNode, sn="downRight", ln="downRight", min=0, max=1, at="double" )
	cmds.setAttr( (ctrlNode + ".tz"), k=0 )
	cmds.setAttr( (ctrlNode + ".rx"), k=0 )
	cmds.setAttr( (ctrlNode + ".ry"), k=0 )
	cmds.setAttr( (ctrlNode + ".rz"), k=0 )
	cmds.setAttr( (ctrlNode + ".sx"), k=0 )
	cmds.setAttr( (ctrlNode + ".sy"), k=0 )
	cmds.setAttr( (ctrlNode + ".sz"), k=0 )
	cmds.setAttr( (ctrlNode + ".rp"), 0.5,0,0, type="double3" )
	cmds.setAttr( (ctrlNode + ".sp"), 0.5,0,0, type="double3" )
	cmds.setAttr( (ctrlNode + ".mntl"), minX,minY,0, type="double3" )
	cmds.setAttr( (ctrlNode + ".mxtl"), maxX,maxY,0, type="double3" )
	cmds.setAttr( (ctrlNode + ".mtxe"), 1 )
	cmds.setAttr( (ctrlNode + ".mtye"), 1 )
	cmds.setAttr( (ctrlNode + ".mtze"), 1 )
	cmds.setAttr( (ctrlNode + ".xtxe"), 1 )
	cmds.setAttr( (ctrlNode + ".xtye"), 1 )
	cmds.setAttr( (ctrlNode + ".xtze"), 1 )
	cmds.setAttr( (ctrlNode + ".upLeft"), k=1 )
	cmds.setAttr( (ctrlNode + ".upRight"), k=1 )
	cmds.setAttr( (ctrlNode + ".downLeft"), k=1 )
	cmds.setAttr( (ctrlNode + ".downRight"), k=1 )

	ctrlShapeNode = cmds.createNode( "nurbsCurve", n=(controlName + "CTRLShape"), p=ctrlNode )
	cmds.setAttr( (ctrlShapeNode + ".v"), k=0 )
	tempCmd = """
	setAttr ".cc" -type "nurbsCurve" 
			1 4 0 no 3
			5 0 1.4142135623730949 2.8284271247461898 4.2426406871192848 5.6568542494923797
			
			5
			0.34088704040884532 0.15911295959115465 -7.9225500608946071e-018
			0.34088704040884527 -0.15911295959115471 -9.8060932293337966e-034
			0.65911295959115468 -0.15911295959115468 7.9225500608946071e-018
			0.65911295959115468 0.15911295959115471 2.941827968800139e-033
			0.34088704040884532 0.15911295959115465 -7.9225500608946071e-018
			;
	"""
	mm.eval(tempCmd)

	######################
	##Make the text
	######################
	textCurveName = cmds.textCurves( ch=0, f="Arial Black|h-13|w400|c0", t=controlName )[0]
	cmds.setAttr( (textCurveName + ".t"), -0.08257546319058684, 1.0583606960304566, 0, type="double3" )
	cmds.setAttr( (textCurveName + ".s"), 0.1, 0.1, 0.1, type="double3" )

	cmds.parent( textCurveName, spaceNode )




	############################
	##Make the Node Network
	############################
	leftValueClamp = cmds.createNode( "clamp", n=(ctrlNode + "_leftValue_CLAMP") )
	rightValueClamp = cmds.createNode( "clamp", n=(ctrlNode + "_rightValue_CLAMP") )
	doubleX_MD = cmds.createNode( "multiplyDivide", n=(ctrlNode + "_doubleX_MD") )
	subtractMD = cmds.createNode( "multiplyDivide", n=(ctrlNode + "_SUBTRACT_MD") )
	leftADL = cmds.createNode( "addDoubleLinear", n=(ctrlNode + "_left_ADL") )
	rightADL = cmds.createNode( "addDoubleLinear", n=(ctrlNode + "_right_ADL") )
	outputClamp = cmds.createNode( "clamp", n=(ctrlNode + "_OUTPUT_CLAMP") )

	##Double the X
	cmds.connectAttr( (ctrlNode + ".tx"), (doubleX_MD + ".input1X") )
	cmds.setAttr( (doubleX_MD + ".input2X"), 2 )

	##split into left/right clamps
	cmds.connectAttr( (doubleX_MD + ".outputX"), (leftValueClamp + ".inputR") )
	cmds.connectAttr( (ctrlNode + ".ty"), (leftValueClamp + ".inputG") )
	cmds.setAttr( (leftValueClamp + ".minR"), -1 )
	cmds.setAttr( (leftValueClamp + ".maxG"), 1 )
	cmds.connectAttr( (doubleX_MD + ".outputX"), (rightValueClamp + ".inputR") )
	cmds.connectAttr( (ctrlNode + ".ty"), (rightValueClamp + ".inputG") )
	cmds.setAttr( (rightValueClamp + ".maxR"), 1 )
	cmds.setAttr( (rightValueClamp + ".maxG"), 1 )

	##multiply rightX by -1. This becomes the equivilant of subtracting by means of addition
	cmds.connectAttr( (rightValueClamp + ".outputR"), (subtractMD + ".input1X") )
	cmds.setAttr( (subtractMD + ".input2X"), -1 )

	##Add clamped values together
	cmds.connectAttr( (leftValueClamp + ".outputR"), (leftADL + ".input2") )
	cmds.connectAttr( (leftValueClamp + ".outputG"), (leftADL + ".input1") )
	cmds.connectAttr( (subtractMD + ".outputX"), (rightADL + ".input2") )
	cmds.connectAttr( (rightValueClamp + ".outputG"), (rightADL + ".input1") )

	##clamp the ADL outputs
	cmds.connectAttr( (leftADL + ".output"), (outputClamp + ".inputR") )
	cmds.connectAttr( (rightADL + ".output"), (outputClamp + ".inputG") )
	cmds.setAttr( (outputClamp + ".maxR"), 1 )
	cmds.setAttr( (outputClamp + ".maxG"), 1 )

	##connect results back to UD channels on controller for feedback
	cmds.connectAttr( (outputClamp + ".outputR"), (ctrlNode + ".upRight") )
	cmds.connectAttr( (outputClamp + ".outputG"), (ctrlNode + ".upLeft") )
	
	return spaceNode, ctrlNode
	
	
############################
##ewww,... it's all GUI
############################
def AddBlendControl_collectAndCall():
	name = cmds.textFieldGrp( "controlNameGrp", q=1, tx=1 )
	plusMinus = []
	plusMinus.append(cmds.checkBoxGrp( "XAxes", q=1, v1=1 ) )
	plusMinus.append(cmds.checkBoxGrp( "XAxes", q=1, v2=1 ) )
	plusMinus.append(cmds.checkBoxGrp( "YAxes", q=1, v1=1 ) )
	plusMinus.append(cmds.checkBoxGrp( "YAxes", q=1, v2=1 ) )
	print plusMinus
	makeBlendControl( name, plusMinus )

def jpmAddBlendControl():
	winName = "AddBlendControl" 
	if ( cmds.window( winName, exists=True) ):
		cmds.deleteUI( winName )
	cmds.window( winName, t="Add Blend Control", rtf=True )

	cmds.rowColumnLayout( nc=1, cw=(1,200) )

	cmds.textFieldGrp( "controlNameGrp", l="Control Name : ", cl2=("left","left"), cw2=(75,150) )
	cmds.button( l="Create", c="AddBlendControl_collectAndCall()" )

	cmds.checkBoxGrp( "XAxes", en=0, w=200, h=15, ncb=2, label="X Axes", cal=(1,"left"), l1="-X", l2="+X", v1=1, v2=1, cw3=(66,33,33) )	
	cmds.checkBoxGrp( "YAxes", en=0, w=200, h=15, ncb=2, label="Y Axes", cal=(1,"left"), l1="-Y", l2="+Y", v1=0, v2=1, cw3=(66,33,33) )
		
	cmds.showWindow( winName )
	
	
