def jpmIkFk():
	winName = "jpmIkFk"
	if ( cmds.window( winName, exists=True) ):
		cmds.deleteUI( winName )
	cmds.window( winName, t="jpmIkFk", rtf=True )

	cmds.rowColumnLayout( "topLayout", nc=1, cw=[1,710] )
	cmds.frameLayout( "jointsFrameLayout", l="Joints", labelAlign="top", borderStyle="in" )
	cmds.rowColumnLayout( "jointsColumnLayout", nc=3, cw=([1,235], [2,235], [3,235]) )

	cmds.rowColumnLayout( nc=2, cw=([1,100], [2,130]) )
	cmds.button( "shoulder_BIND", l="shoulder_BIND -->", w=110, c='jpmIkFk_fillText( "shoulder_BIND_text")' )
	cmds.textFieldGrp( "shoulder_BIND_text", cal=[1,"left"], cw=[1,125] )
	cmds.button( "elbow_BIND", l="elbow_BIND -->", w=110, c='jpmIkFk_fillText( "elbow_BIND_text")' )
	cmds.textFieldGrp( "elbow_BIND_text", cal=[1,"left"], cw=[1,125] )
	cmds.button( "wrist_BIND", l="wrist_BIND -->", w=110,c='jpmIkFk_fillText( "wrist_BIND_text")' )
	cmds.textFieldGrp( "wrist_BIND_text", cal=[1,"left"], cw=[1,125] )

	cmds.setParent("jointsColumnLayout")
	cmds.rowColumnLayout( nc=2, cw=([1,100], [2,130]))	
	cmds.button( "shoulder_IK", l="shoulder_IK -->", w=110, c='jpmIkFk_fillText( "shoulder_IK_text")' )
	cmds.textFieldGrp( "shoulder_IK_text", cal=[1,"left"], cw=[1,125] )
	cmds.button( "elbow_IK", l="elbow_IK -->", w=110, c='jpmIkFk_fillText( "elbow_IK_text" )' )
	cmds.textFieldGrp( "elbow_IK_text", cal=[1,"left"], cw=[1,125] )
	cmds.button( "wrist_IK", l="wrist_IK -->", w=110, c='jpmIkFk_fillText( "wrist_IK_text")' )
	cmds.textFieldGrp( "wrist_IK_text", cal=[1,"left"], cw=[1,125] )
	
	cmds.setParent("jointsColumnLayout")
	cmds.rowColumnLayout( nc=2, cw=([1,100], [2,130]))
	cmds.button( "shoulder_FK", l="shoulder_FK -->", w=110, c='jpmIkFk_fillText( "shoulder_FK_text" )' )
	cmds.textFieldGrp( "shoulder_FK_text", cal=[1,"left"], cw=[1,125] )
	cmds.button( "elbow_FK", l="elbow_FK -->", w=110, c='jpmIkFk_fillText( "elbow_FK_text" )' )
	cmds.textFieldGrp( "elbow_FK_text", cal=[1,"left"], cw=[1,125] )
	cmds.button( "wrist_FK", l="wrist_FK -->", w=110, c='jpmIkFk_fillText( "wrist_FK_text" )' )
	cmds.textFieldGrp( "wrist_FK_text", cal=[1,"left"], cw=[1,125] )
	
	cmds.setParent("topLayout")
	cmds.frameLayout( l="Choices", labelAlign="top", borderStyle="in" )
	cmds.rowColumnLayout( "choicesColumnLayout", nc=1, cw=[1,710])
	cmds.radioButtonGrp( "supplyJointsRadio", nrb=2, labelArray2=["Make Joints Given _BIND", "User Supplies Ik/Fk Joints"], cw=([1,150],[2,150]) )
	cmds.radioButtonGrp( "connectionTypeRadio", nrb=3, labelArray3=["Constraints","ISO_Constraints","Conditions"] )

	cmds.setParent("topLayout")
	cmds.frameLayout( l="Actions", labelAlign="top", borderStyle="in" )
	cmds.rowColumnLayout( "actionsColumnLayout", nc=1 )
	cmds.button( "makeSwitch_button", l="Make It", w=125 )
	
	cmds.showWindow( winName )
	
def jpmIkFk_fillText(*args):
	textField = args[0]
	selection = cmds.ls(sl=1) 
	cmds.textFieldGrp( textField, e=1, tx=selection[0] )
	
def jpmIkFk_collectAndCall():
	##Joints
	rootBind = cmds.textFieldGrp( "shoulder_BIND", q=1, v=1 )
	flexBind = cmds.textFieldGrp( "elbow_BIND", q=1, v=1 )
	endBind = cmds.textFieldGrp( "wrist_BIND", q=1, v=1 )
	
	##Choices
	supplyJoints = cmds.radioButtonGrp( "supplyJointsRadio", q=1, v=1 )
	connectionType = cmds.radioButtonGrp( "connectionTypeRadio", q=1, v=1 )
	
	bindJoints = [rootBind, flexBind, endBind]
	##Decision Tree
	if supplyJoints == 1:
		rootFK = cmds.textFieldGrp( "shoulder_FK", q=1, v=1 )
		flexFK = cmds.textFieldGrp( "elbow_FK", q=1, v=1 )
		endFK = cmds.textFieldGrp( "wrist_FK", q=1, v=1 )
		
		rootIK =cmds.textFieldGrp( "shoulder_IK", q=1, v=1 )
		flexIK = cmds.textFieldGrp( "elbow_IK", q=1, v=1 )
		endIK = cmds.textFieldGrp( "wrist_IK", q=1, v=1 )
		
		fkJoints = [rootFK, flexFK, endFK]
		ikJoints = [rootIK, flexIK, endIK]
		if connectionType == 1:
			print "Supplied Joints, Constraint Connections"
		elif connectionType == 2:
			print "Supplied Joints, ISO Constraint Connections"
		elif connectionType == 3:
			print "Supplied Joints, Condition Connections"
	else:
		allJoints = []
		if connectionType == 1:
			print "Make Joints, Constraint Connections"
			allJoints = jpmFkIk_DupeJoints(bindJoints)
		elif connectionType == 2:
			print "Make Joints, ISO Constraint Connections"
			allJoints = jpmFkIk_DupeJoints(bindJoints)
		elif connectionType == 3:
			print "Make Joints, Condition Connections"
			allJoints = jpmFkIk_DupeJoints(bindJoints)

			
def jpmFkIk_DupeJoints(startJoints=[]):
	print "Duplicate Joints"	
	bindJoints = startJoints
		
	rootBind = bindJoints[0]
	flexBind = bindJoints[1]
	endBind = bindJoints[2]
		
	rootPos = getPositions( rootBind )
	flexPos = getPositions( flexBind )
	endPos = getPositions( endBind )

	rootParse = parseNames( rootBind )
	flexParse = parseNames( flexBind )
	endParse = parseNames( endBind )
	controlParse = parseNames( control )
	
	cmds.select( cl=True )
	rootIK = cmds.joint( p=rootPos, n=(str(rootParse) + "_IK_JNT") )
	flexIK = cmds.joint( p=flexPos, n=(str(flexParse) + "_IK_JNT") )
	endIK = cmds.joint( p=endPos, n=(str(endParse) + "_IK_JNT") )
	cmds.joint( rootIK, oj="yxz", sao="zup", zso=True, e=1)
	cmds.joint( flexIK, oj="yxz", sao="zup", zso=True, e=1)
	cmds.joint( endIK, oj="yxz", sao="zup", zso=True, e=1)
	
	cmds.select( cl=True )
	rootFK = cmds.joint( p=rootPos, n=(str(rootParse) + "_FK_JNT") )
	flexFK = cmds.joint( p=flexPos, n=(str(flexParse) + "_FK_JNT") )
	endFK = cmds.joint( p=endPos, n=(str(endParse) + "_FK_JNT") )
	cmds.joint( rootFK, oj="yxz", sao="zup", zso=True, e=1)
	cmds.joint( flexFK, oj="yxz", sao="zup", zso=True, e=1)
	cmds.joint( endFK, oj="yxz", sao="zup", zso=True, e=1)

	fkJoints = [rootFK,flexFK,endFK]
	ikJoints = [rootIK,flexIK,endIK]
	
	joints = [bindJoints,fkJoints,ikJoints]
	
	return joints
	
def jpmFkIk_MakeConstraintConnections( control, startJoints=[]):
	print "Make Constraint Connections"
	bindJoints = startJoints[0]
	fkJoints = startJoints[1]
	ikJoints = startJoints[2]
	
	rootBind = bindJoints[0]
	flexBind = bindJoints[1]
	endBind = bindJoints[2]
	
	rootFK = fkJoints[0]
	flexFK = fkJoints[1]
	endFK = fkJoints[2]
	
	rootIK = ikJoints[0]
	flexIK = ikJoints[1]
	endIK = ikJoints[2]
	
	rootPos = getPositions( rootBind )
	flexPos = getPositions( flexBind )
	endPos = getPositions( endBind )

	rootParse = parseNames( rootBind )
	flexParse = parseNames( flexBind )
	endParse = parseNames( endBind )
	controlParse = parseNames( control )
	
	##Make Controls
	rootCtrl = cmds.circle( n=(rootParse + "_FK_CTRL"), c=rootPos, fp=rootPos, fc=True, r=1, ch=False, nr=[0,1,0] )
	mm.eval( "CenterPivot" )
	flexCtrl = cmds.circle( n=(flexParse + "_FK_CTRL"), c=flexPos, fp=flexPos, fc=True, r=1, ch=False, nr=[0,1,0] )
	mm.eval( "CenterPivot" )
	endCtrl = cmds.circle( n=(endParse + "_FK_CTRL"), c=endPos, fp=endPos, fc=True, r=1, ch=False, nr=[0,1,0] )
	mm.eval( "CenterPivot" )

	cmds.parent( flexCtrl, rootCtrl )
	cmds.parent( endCtrl, flexCtrl )

	cmds.parentConstraint( rootCtrl, rootFK, mo=True )
	cmds.parentConstraint( flexCtrl, flexFK, mo=True )
	cmds.parentConstraint( endCtrl, endFK, mo=True )

	cmds.select( cl=True )

	##Make IK
	limbIK = cmds.ikHandle( n=(str(rootParse) + "_IK"), sj=rootIK, ee=endIK )
	cmds.parentConstraint( control, limbIK[0], mo=True)

	##Add Attributes
	cmds.select ( cl=True )
	if not cmds.attributeQuery( "FkIk", node=control, ex=1):
		cmds.addAttr( control, ln="FkIk", at="float",  min=0, max=1, dv=1 )
		cmds.setAttr( (control + ".FkIk"), e=True, keyable=True )

	##Make Constraints and Connections
	rootCon = cmds.parentConstraint( rootIK, rootBind, mo=True )
	flexCon = cmds.parentConstraint( flexIK, flexBind, mo=True )
	endCon = cmds.parentConstraint( endIK, endBind, mo=True )
	cmds.parentConstraint( rootFK, rootBind, mo=True )
	cmds.parentConstraint( flexFK, flexBind, mo=True )
	cmds.parentConstraint( endFK, endBind, mo=True )

	revNode = cmds.shadingNode( "reverse", asUtility=True, n=(controlParse + "_REV") )
	cmds.connectAttr( (control + ".FkIk"), (revNode + ".inputX") )
	cmds.connectAttr( (revNode + ".outputX"), (rootCon[0] + "." + rootFK + "W1") )
	cmds.connectAttr( (revNode + ".outputX"), (flexCon[0] + "." + flexFK + "W1") )
	cmds.connectAttr( (revNode + ".outputX"), (endCon[0] + "." + endFK + "W1") )

	cmds.connectAttr( (control + ".FkIk"), (rootCon[0] + "." + rootIK + "W0") )
	cmds.connectAttr( (control + ".FkIk"), (flexCon[0] + "." + flexIK + "W0") )
	cmds.connectAttr( (control + ".FkIk"), (endCon[0] + "." + endIK + "W0") )

	cmds.connectAttr( (revNode + ".outputX"), (rootCtrl[0] + ".visibility") )
	cmds.connectAttr( (revNode + ".outputX"), (flexCtrl[0] + ".visibility") )
	cmds.connectAttr( (revNode + ".outputX"), (endCtrl[0] + ".visibility") )

	return rootIK, flexIK, endIK

		
def jpmFkIk_MakeISOConstraintConnections(startJoints=[]):
	print "Make ISO Constraint Connections"
	bindJoints = startJoints[0]
	fkJoints = startJoints[1]
	ikJoints = startJoints[2]
	
	rootBind = bindJoints[0]
	flexBind = bindJoints[1]
	endBind = bindJoints[2]
	
	rootFK = fkJoints[0]
	flexFK = fkJoints[1]
	endFK = fkJoints[2]
	
	rootIK = ikJoints[0]
	flexIK = ikJoints[1]
	endIK = ikJoints[2]
	
	rootPos = getPositions( rootBind )
	flexPos = getPositions( flexBind )
	endPos = getPositions( endBind )

	rootParse = parseNames( rootBind )
	flexParse = parseNames( flexBind )
	endParse = parseNames( endBind )
	controlParse = parseNames( control )
	
	##Make Controls
	rootCtrl = cmds.circle( n=(rootParse + "_FK_CTRL"), c=rootPos, fp=rootPos, fc=True, r=1, ch=False, nr=[0,1,0] )
	mm.eval( "CenterPivot" )
	flexCtrl = cmds.circle( n=(flexParse + "_FK_CTRL"), c=flexPos, fp=flexPos, fc=True, r=1, ch=False, nr=[0,1,0] )
	mm.eval( "CenterPivot" )
	endCtrl = cmds.circle( n=(endParse + "_FK_CTRL"), c=endPos, fp=endPos, fc=True, r=1, ch=False, nr=[0,1,0] )
	mm.eval( "CenterPivot" )

	cmds.parent( flexCtrl, rootCtrl )
	cmds.parent( endCtrl, flexCtrl )

	cmds.parentConstraint( rootCtrl, rootFK, mo=True )
	cmds.parentConstraint( flexCtrl, flexFK, mo=True )
	cmds.parentConstraint( endCtrl, endFK, mo=True )

	cmds.select( cl=True )

	##Make IK
	limbIK = cmds.ikHandle( n=(str(rootParse) + "_IK"), sj=rootIK, ee=endIK )
	cmds.parentConstraint( control, limbIK[0], mo=True)

	##Add Attributes
	cmds.select ( cl=True )
	if not cmds.attributeQuery( "FkIk", node=control, ex=1):
		cmds.addAttr( control, ln="FkIk", at="float",  min=0, max=1, dv=1 )
		cmds.setAttr( (control + ".FkIk"), e=True, keyable=True )

	##Make Constraints and Connections
	rootCon = cmds.parentConstraint( rootIK, rootBind, mo=True )
	flexCon = cmds.parentConstraint( flexIK, flexBind, mo=True )
	endCon = cmds.parentConstraint( endIK, endBind, mo=True )
	cmds.parentConstraint( rootFK, rootBind, mo=True )
	cmds.parentConstraint( flexFK, flexBind, mo=True )
	cmds.parentConstraint( endFK, endBind, mo=True )

	revNode = cmds.shadingNode( "reverse", asUtility=True, n=(controlParse + "_REV") )
	cmds.connectAttr( (control + ".FkIk"), (revNode + ".inputX") )
	cmds.connectAttr( (revNode + ".outputX"), (rootCon[0] + "." + rootFK + "W1") )
	cmds.connectAttr( (revNode + ".outputX"), (flexCon[0] + "." + flexFK + "W1") )
	cmds.connectAttr( (revNode + ".outputX"), (endCon[0] + "." + endFK + "W1") )

	cmds.connectAttr( (control + ".FkIk"), (rootCon[0] + "." + rootIK + "W0") )
	cmds.connectAttr( (control + ".FkIk"), (flexCon[0] + "." + flexIK + "W0") )
	cmds.connectAttr( (control + ".FkIk"), (endCon[0] + "." + endIK + "W0") )

	cmds.connectAttr( (revNode + ".outputX"), (rootCtrl[0] + ".visibility") )
	cmds.connectAttr( (revNode + ".outputX"), (flexCtrl[0] + ".visibility") )
	cmds.connectAttr( (revNode + ".outputX"), (endCtrl[0] + ".visibility") )

	return rootIK, flexIK, endIK

	
	
	
def jpmFkIk_MakeConditionConnections(startJoints=[]):
	print "Make Condition Connections"
	bindJoints = startJoints[0]
	fkJoints = startJoints[1]
	ikJoints = startJoints[2]
	
	rootBind = bindJoints[0]
	flexBind = bindJoints[1]
	endBind = bindJoints[2]
	
	rootFK = fkJoints[0]
	flexFK = fkJoints[1]
	endFK = fkJoints[2]
	
	rootIK = ikJoints[0]
	flexIK = ikJoints[1]
	endFK = ikJoints[2]
	
	rootPos = getPositions( rootBind )
	flexPos = getPositions( flexBind )
	endPos = getPositions( endBind )

	rootParse = parseNames( rootBind )
	flexParse = parseNames( flexBind )
	endParse = parseNames( endBind )
	controlParse = parseNames( control )
	
	
	
	
def getPositions(object):
	thisPos = cmds.xform(object, q=True, t=True, a=True, ws=True)
	return thisPos	

def parseNames(object):
	parsed = ""
	removeTags = []
	theseTags = object.split("_")
	badTags = ["BIND", "PLACE", "JNT", "IK", "FK", "SINGLE", "CTRL", "GRP", "CTRLGRP", "GEO"]
	for tag in theseTags:
		for bad in badTags:
			if tag == bad:
				removeTags.append(tag)
	for tag in removeTags:
		theseTags.remove(tag)
	parsed = "_".join(theseTags)
	return parsed
	
jpmIkFk()