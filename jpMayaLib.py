import maya.cmds as cmds
import maya.mel as mm

import re
import math
import os

def getPositions(object):
    thisType = cmds.ls(object, st=True)[1]
    if thisType != "joint":
        thisPos = cmds.objectCenter(cmds.listRelatives(object, fullPath=1, s=True)[0], gl=True)
    else:
        #thisPos = cmds.objectCenter(object, gl=True)
        thisPos = cmds.xform(object, q=True, t=True, a=True, ws=True)
    return thisPos

def setPositions(object, thisPos):
    cmds.xform(object, t=thisPos, a=True, ws=True)

def distance(start, end):
    deltaX = start[0] - end[0]
    deltaY = start[1] - end[1]
    deltaZ = start[2] - end[2]

    powX = math.pow(deltaX, 2)
    powY = math.pow(deltaY, 2)
    powZ = math.pow(deltaZ, 2)
    powers = powX + powY + powZ
    distanceBetween = math.sqrt(powers)

    return distanceBetween
	
#sample = getNearest(allBrokens, splineJoints)
def getNearest(first, second, threshold=9999.99):
    firstDict = {}
    secondDict = {}
    pairedDict = {}
    closest = ""
	
	for thisObj in first:
        thisObjPos = getPositions(thisObj)
        firstDict[thisObj] = thisObjPos
        
    for thisObj in second:
        thisObjPos = getPositions(thisObj)
        secondDict[thisObj] = thisObjPos
    
	for thisFirst in firstDict.keys():
		closest = ""
		nearest = threshold
		for thisSecond in secondDict.keys():
			distanceBetween = distance(firstDict[thisFirst], secondDict[thisSecond])
			if distanceBetween < nearest:
				nearest = distanceBetween
				closest = thisSecond
		pairedDict[thisFirst] = closest
	return pairedDict
	
def getKDnearest(first, second, threshold):
	print "implement a k-d tree to find nearst points"
		
def filterList(selected, filter):
	filterSelected = cmds.ls(filter, r=1, tr=1)
	bothSelected = []
	for obj in selected:
		for filteredObj in filterSelected:
			if obj == filteredObj:
				bothSelected.append(obj)
	return bothSelected
	
def typeFilterList(selected, filter):
    filterSelected = cmds.ls(typ=filter)
    bothSelected = []
    for obj in selected:
        for filteredObj in filterSelected:
            if obj == filteredObj:
                bothSelected.append(obj)
    return bothSelected

def makeSDK(driver, driven, keys):
    for key in keys:
        cmds.setDrivenKeyframe(driven, cd=driver, itt="linear", ott="linear", driverValue=key[0], value=key[1])

def insertGrp(grpParent, grpName):
    theseChildren = cmds.listRelatives(grpParent, c=1)
    shapeChildren = cmds.listRelatives(grpParent, s=1)

    if not shapeChildren == None:
        for thisShapeChild in shapeChildren:
            theseChildren.remove(thisShapeChild)

    if not cmds.objExists(grpName):
        thisGrp = cmds.group(name=grpName, empty=1)
    else:
        thisGrp = grpName

    if cmds.objExists(grpParent):
        cmds.parent(thisGrp, grpParent)
    else:
        print "Specified parent does not exist"

    constraintSnap(grpParent, thisGrp)

    if cmds.objExists(thisGrp):
        cmds.makeIdentity(thisGrp, apply=1)
    else:
        print grpName + " does not exist"

    cmds.parent(theseChildren, thisGrp)

    return thisGrp

def constraintSnap(master, slave):
    cmds.select(cl=1)
    cmds.select(master)
    cmds.select(slave, add=True)

    #CreateConstraints
    try:
        thisPoint = cmds.pointConstraint(n="tempPoint", w=1)
        thisOrient = cmds.orientConstraint(n="tempOrient", w=1)
        thisScale = cmds.scaleConstraint(n="tempScale", w=1)
    except:
        print "Constraint Problems"

    #Delete Constraints
    cmds.select(thisPoint)
    cmds.select(thisOrient, add=1)
    cmds.select(thisScale, add=1)
    cmds.delete()

    cmds.select(slave)
	
##James Parks
##various snap procedures
##Converted from procedures from Comet
def animSnap(master, slave):
    sel = cmds.ls(sl=1)
    if master == "" or slave == "":
        master = sel[0]
        slave = sel[1]
    dupe = cmds.duplicate(slave, rc=1, rr=1)
    dupeSlave = dupe[0]
    snap(master, dupeSlave)
    ndsSnap(dupeSlave, slave)
    cmds.delete(dupeSlave)
    cmds.select((master, slave), r=1)

def snap(master, slave):
    sel = cmds.ls(sl=1)
    if master == "" or slave == "":
        master = sel[0]
        slave = sel[1]
    cmds.select(cl=1)
    cmds.select(master)
    cmds.select(slave, add=1)
    thisPoint = ""
    thisOrient = ""
    try:
        thisPoint = cmds.pointConstraint(n="tempPoint", w=1)[0]
    except:
        print "Point constraint didn't work for some reason"
    try:
        thisOrient = cmds.orientConstraint(n="tempOrient", w=1)[0]
    except:
        print "Constraints didn't work for some reason"
    ##cmds.refresh()
    if cmds.objExists(thisPoint):
        cmds.select(thisPoint)
        cmds.delete()
    if cmds.objExists(thisOrient):
        cmds.select(thisOrient)
        cmds.delete()
    cmds.select(master, slave, r=1)

def ndsSnap(master, slave):
    sel = cmds.ls(sl=1)
    if master == "" or slave == "":
        master = sel[0]
        slave = sel[1]
    if master == "" or slave == "":
        return
    xt = []
    xt.append(cmds.getAttr(master + ".translateX"))
    xt.append(cmds.getAttr(master + ".translateY"))
    xt.append(cmds.getAttr(master + ".translateZ"))
    xr = []
    xr.append(cmds.getAttr(master + ".rotateX"))
    xr.append(cmds.getAttr(master + ".rotateY"))
    xr.append(cmds.getAttr(master + ".rotateZ"))
    try:
        cmds.setAttr((slave + ".translateX"), xt[0])
    except:
        print "SetAttr tx didn't work for some reason"
    try:
        cmds.setAttr((slave + ".translateY"), xt[1])
    except:
        print "SetAttr ty didn't work for some reason"
    try:    
        cmds.setAttr((slave + ".translateZ"), xt[2])
    except:
        print "SetAttr tz didn't work for some reason"
    try:
        cmds.setAttr((slave + ".rotateX"), xr[0])
    except:
        print "SetAttr rx didn't work for some reason"
    try:
        cmds.setAttr((slave + ".rotateY"), xr[1])
    except:
        print "SetAttr ry didn't work for some reason"
    try:
        cmds.setAttr((slave + ".rotateZ"), xr[2])
    except:
        print "SetAttr rz didn't work for some reason"
		
def amIaReference(selected):
	verboseLevel = 0
	if selected == "":
		return "0"
	try:
		refTest = cmds.referenceQuery(selected, f=1)
	except:
		refTest = 0
		
	if refTest != 0:
		###################
		##Find the filename
		###################
		refFile = cmds.referenceQuery(selected, f=1)
		tokRefFile = re.split("/", refFile)
		
		###################
		##Is it a namespace? Split for ":" in the namespace
		###################
		refNodes = cmds.referenceQuery(refFile, n=1)
		tokNameSpace = re.split(":", refNodes[0])
		NS_tokens = len(tokNameSpace)
		
		##No matter how deep it's referenced this should get them all,... I hope
		finalNS = ""
		for i in range(0, (NS_tokens-1)):
			finalNS = (finalNS + tokNameSpace[i] + ":")
		
		###################
		##Find the Prefix by comparing the first and last node names starting from the front
		###################
		prefix = ""
		firstNodeSize = len(refNodes[0])
		
		for i in range(0, firstNodeSize):
			refSize = len(refNodes)
			subStringOne = refNodes[0][0:i]
			subStringTwo = refNodes[(refSize-1)][0:i]
			if verboseLevel != 0:
				print (subStringOne + " || " + subStringTwo + "\n")
			if subStringOne == subStringTwo:
				prefix = refNodes[0][0:i]

		###################
		##Return the appropriate response
		###################
		if NS_tokens > 1:
			print ("I am a reference. My name space is " + finalNS)
			return finalNS
		elif prefix != "":
			print ("I am a reference. My prefix is " + prefix)
			return prefix
		else:
			print "I am _NOT_ a reference"
			return "0"
	else:
		print "I am _NOT_ a reference"
		return "0"

def locatorize(allObjs):
	names = []
	i = 0
	for obj in allObjs:
		locName = cmds.spaceLocator(name=obj + "_loc")[0]
		cmds.select(obj)
		cmds.select(locName, add=1)

		try:
			thisPoint = cmds.pointConstraint(n="tempPoint", w=1)
			thisOrient = cmds.orientConstraint(n="tempOrient", w=1)
			thisScale = cmds.scaleConstraint(n="tempScale", w=1)
		except:
			print "Constraint Problems"
			
		#Delete Constraints
		cmds.select(thisPoint)
		cmds.select(thisOrient, add=1)
		cmds.select(thisScale, add=1)
		cmds.delete()

		names.append(locName)
	return names
	
def orientJoint(name):
	cmds.makeIdentity(name, apply=1)
	cmds.joint(name, e=1, oj="yzx", sao="yup", zso=1)
	
##parent lots of objects in a string, one after the other
def multiParent(objects=[]):
	for i in range(len(objects)):
		try:
			cmds.parent(objects[i+1], objects[i])
		except:
			print ""
			break

def addDistance(firstPos, offset):
	finalPos = [ firstPos[0]+offset[0], firstPos[1]+offset[1], firstPos[2]+offset[2] ]
	return finalPos

def midPoint(firstObj, secondObj):
	initDist = getDistance(firstObj, secondObj)
	startPos = getPositions(firstObj)
	thisOffset = [initDist[1]/2, initDist[2]/2, initDist[3]/2]
	
	midPos = addDistance(startPos, thisOffset)
	return midPos
	
##split one joint up into multiple
def splitJoint(name, numOfJoints, anchors=[]):
	initDist = self.getDistance(anchors[0], anchors[1])
	startPos = self.getPositions(anchors[0])
	#numOfJoints = 3
	thisOffset = [initDist[1]/numOfJoints, initDist[2]/numOfJoints, initDist[3]/numOfJoints]
	splitJoints = []
	splitJoints.append(self.makeJoint((name + "0"), startPos, "BIND"))
	for i in range(1,numOfJoints+1):
		thisName = (name + str(i))
		thisPos = self.addDistance(startPos, (thisOffset * 1))
		splitJoints.append(self.makeJoint(thisName, thisPos, "BIND"))
		#splitJoints.append(self.makeJoint(("spine" + str(i)), self.addDistance(startPos, (thisOffset * i), "BIND"))
		startPos = self.addDistance(startPos, thisOffset)
	self.multiParent(splitJoints)
	#cmds.parent(splitJoints[0], spineRootJnt)

	joints = [ splitJoints ]
	return joints

##read lines in from a file on disk
def readLines(fileToRead):
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

##read a whole file in from disk
def readFile(fileToRead):
	readFile = ""
	badFile = ""
	if os.path.exists(fileToRead) == False:
		print "File Not Found"
	else:
		thisFile = file(fileToRead, "r+")
		badFile = thisFile.read()
		thisFile.close()
	readFile = badFile.strip()
	return readFile
