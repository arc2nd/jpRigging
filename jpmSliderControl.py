sliderName = "testSlider"

def makeSliderCtrl(sliderName):
    controlName = sliderName + "_CTRL"
    pointerName = sliderName + "_onSurf"
    helperName = sliderName + "_onSurf_HELPER"
    jointName = sliderName + "_surfJNT"
    
    selectedPoint = cmds.ls(sl=True)[0]
    sliderSurf = selectedPoint.split("[")[0].split(".")[0]
    
    ##Make Nodes
    controlNode = makeHalfDiamondCtrl(sliderName)
    helperNode = cmds.group(name=helperName, empty=True)
    pointerNode = cmds.group(name=pointerName, empty=True)
    
    ptOnSurf = cmds.createNode("pointOnSurfaceInfo", name=sliderName + "_ptOnSurfInfo")
    closestPt = cmds.createNode("closestPointOnSurface", name=sliderName + "_closestPtOnSurf")
    
    ##Position and Connect Nodes    
    cmds.connectAttr(sliderSurf + ".worldSpace[0]", ptOnSurf + ".inputSurface")
    cmds.connectAttr(sliderSurf + ".worldSpace[0]", closestPt + ".inputSurface")
    
    cmds.setAttr(ptOnSurf + ".parameterU", float(selectedPoint.split("[")[1][:-1]))
    cmds.setAttr(ptOnSurf + ".parameterV", float(selectedPoint.split("[")[2][:-1]))
    
    snapToPt = cmds.getAttr(ptOnSurf + ".position")[0]
    
    cmds.connectAttr(closestPt + ".parameterU", ptOnSurf + ".parameterU")
    cmds.connectAttr(closestPt + ".parameterV", ptOnSurf + ".parameterV")
    
    cmds.setAttr(helperNode + ".translate", snapToPt[0], snapToPt[1], snapToPt[2])
    cmds.setAttr(pointerNode + ".translate", snapToPt[0], snapToPt[1], snapToPt[2])
    cmds.setAttr(controlNode + ".translate", snapToPt[0], snapToPt[1], snapToPt[2])
    cmds.connectAttr(helperNode + ".translate", closestPt + ".inPosition")
    
    pntConst = cmds.pointConstraint(controlName, helperNode)[0]
    normCnst = cmds.normalConstraint(sliderSurf, pointerNode)[0]
    cmds.connectAttr(ptOnSurf + ".normalizedTangentU", normCnst + ".worldUpVector")
    cmds.connectAttr(ptOnSurf + ".position", pointerNode + ".translate")
    
    cmds.select(controlName)
    ctrls.jpmCreateIso()
	
	
def makeHalfDiamondCtrl(name=""):
	if name == "":
		transformNode = cmds.createNode( "transform", n="HalfDiamond_ctrl" )
	else:
		transformNode = cmds.createNode( "transform", n=(name + "_ctrl") )
	cmds.setAttr( ".v", k=False )
	cmds.createNode( "nurbsCurve", n=(transformNode + "Shape"), p=transformNode )
	cmds.setAttr( ".v", k=False )
	tempCmd = """
	setAttr ".cc" -type "nurbsCurve" 
		1 9 0 no 3
		10 0 1 2 3 4 5 6 7 8 9
		10
		-0.49043959096453954 1.1485305913236596 3.8501775160668944e-017
		-3.8501775160668944e-017 1.1485305913236596 -0.49043959096453954
		0.49043959096453954 1.1485305913236596 -3.8501775160668944e-017
		3.8501775160668944e-017 1.1485305913236596 0.49043959096453954
		-0.49043959096453954 1.1485305913236596 3.8501775160668944e-017
		0 0 0
		3.8501775160668944e-017 1.1485305913236596 0.49043959096453954
		0.49043959096453954 1.1485305913236596 -3.8501775160668944e-017
		0 0 0
		-3.8501775160668944e-017 1.1485305913236596 -0.49043959096453954
		;
	"""
	mm.eval( tempCmd )
	cmds.select( transformNode )
	return transformNode