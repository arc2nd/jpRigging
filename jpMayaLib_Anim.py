##James Parks
import maya.cmds as cmds



def copyUDAttrs(source, dest):
	##list all user-defined attributes and recreate them on the new object
	udAttr = cmds.listAttr(source, userDefined=True)
	print "\nUser-Defined Attributes Copied:\n"
	if udAttr:
		for thisAttr in udAttr:
			if not cmds.attributeQuery(thisAttr, exists=True, node=dest):
				hasRange = cmds.attributeQuery(thisAttr, node=source, rangeExists=True)
				default = cmds.attributeQuery(thisAttr, node=source, listDefault=True)
				type = cmds.getAttr(source + "." + thisAttr, type=True)
				isKeyable = cmds.getAttr(source + "." + thisAttr, keyable=True)
				#cmds.select(source)

				if type=="string" or type=="stringArray" or type=="matrix" or type=="doubleArray" or type=="floatArray" or type=="Int32Array" or type=="vectorArray" or type=="pointArray":
					try:
						cmds.addAttr(dest, longName=thisAttr, dataType=type)
					except:
						cmds.addAttr(dest, longName=thisAttr, attributeType=type)
					finally:
						print "I'm so confused, I can't figure out the attribute type"
				elif type=="enum":
					flags = cmds.attributeQuery(thisAttr, node=source, listEnum=True)
					cmds.addAttr(dest, longName=thisAttr, attributeType=type, enumName=flags[0])
				elif default:
					if hasRange:
						range = cmds.attributeQuery(thisAttr, node=source, range=True)
						cmds.addAttr(dest, longName=thisAttr, attributeType=type, min=range[0], max=range[1], defaultValue=default[0])
					else:
						cmds.addAttr(dest, longName=thisAttr, attributeType=type, defaultValue=default[0])
				else:
					if hasRange:
						range = cmds.attributeQuery(thisAttr, node=source, range=True)
						cmds.addAttr(dest, longName=thisAttr, attributeType=type, min=range[0], max=range[1])
					else:
						cmds.addAttr(dest, longName=thisAttr, attributeType=type)
				
				cmds.setAttr(dest + "." + thisAttr, e=True, keyable=isKeyable)
			print "-----" + thisAttr + "\n"
		print "Finished Copying User-Defined Attributes"

def transferValue(source, dest, attr):
	val = cmds.getAttr(source + "." + attr)
	try:
		cmds.setAttr(dest + "." + attr, val)
	except:
		print "Can't transfer values from " + source + " to " + dest + "." + attr
		
def transferCurve(source, dest, attr):
	curve = cmds.copyKey(source, clipboard="anim", attribute=attr)
	try:
	    cmds.pasteKey(dest, attribute=attr, option="insert", clipboard="anim")
	except:
		print "Can't transfer curves from " + source + " to " + dest + "." + attr

def transferAnim(source, dest, copyType, tX=True, tY=True, tZ=True, rX=True, rY=True, rZ=True, sX=True, sY=True, sZ=True, vis=True, ud=True):
	cmds.select(source)
	cmds.select(dest, add=True)
	copyUDAttrs(source, dest)
	
	allAttr = cmds.listAttr(source, keyable=True)
	udAttr = cmds.listAttr(source, userDefined=True)
	
	for thisAttr in allAttr:
		#isKeyed = cmds.copyKey(source, cb="anim", attribute=thisAttr)
		isKeyed = cmds.selectKey(source + "." + thisAttr, add=1, keyframe=1)
		isAttrUd = 0
		if udAttr:
			if thisAttr in udAttr:
				isAttrUd = 1
				
		##Checks Copy Type whether to copy animCurves or just current values and then does so
		val = cmds.getAttr(source + "." + thisAttr)

		if thisAttr == "translateX" and tX == 1:
			transferValue(source, dest, thisAttr)
		if thisAttr == "translateY" and tY == 1:
			transferValue(source, dest, thisAttr)
		if thisAttr == "translateZ" and tZ == 1:
			transferValue(source, dest, thisAttr)

		if thisAttr == "rotateX" and rX == 1:
			transferValue(source, dest, thisAttr)
		if thisAttr == "rotateY" and rY == 1:
			transferValue(source, dest, thisAttr)
		if thisAttr == "rotateZ" and rZ == 1:
			transferValue(source, dest, thisAttr)

		if thisAttr == "scaleX" and sX == 1:
			transferValue(source, dest, thisAttr)
		if thisAttr == "scaleY" and sY == 1:
			transferValue(source, dest, thisAttr)
		if thisAttr == "scaleZ" and sZ == 1:
			transferValue(source, dest, thisAttr)

		if thisAttr == "visibility" and vis == 1:
			transferValue(source, dest, thisAttr)
		if ud == 1 and isAttrUd == 1:
			transferValue(source, dest, thisAttr)
			
		if copyType == "wholeCurves" and isKeyed:
			if thisAttr == "translateX" and tX == 1:
				transferCurve(source, dest, thisAttr)
			if thisAttr == "translateY" and tY == 1:
				transferCurve(source, dest, thisAttr)
			if thisAttr == "translateZ" and tZ == 1:
				transferCurve(source, dest, thisAttr)

			if thisAttr == "rotateX" and rX == 1:
				transferCurve(source, dest, thisAttr)
			if thisAttr == "rotateY" and rY == 1:
				transferCurve(source, dest, thisAttr)
			if thisAttr == "rotateZ" and rZ == 1:
				transferCurve(source, dest, thisAttr)

			if thisAttr == "scaleX" and sX == 1:
				transferCurve(source, dest, thisAttr)
			if thisAttr == "scaleY" and sY == 1:
				transferCurve(source, dest, thisAttr)
			if thisAttr == "scaleZ" and sZ == 1:
				transferCurve(source, dest, thisAttr)

			if thisAttr == "visibility" and vis == 1:
				transferCurve(source, dest, thisAttr)
			if ud == 1 and isAttrUd == 1:
				transferCurve(source, dest, thisAttr)
		print "-----" + thisAttr + "\n"
	print "Finished Transfer"
	
def batchTransfer(sources):
	size = len(sources)
	remainder = size % 2
	if remainder != 0:
		print "This works in pairs, select an even number"
		return

	for i in range(0, size, 2):
		transferAnim(sources[i], sources[i+1], copyType="wholeCurves", tX=True, tY=True, tZ=True, rX=True, rY=True, rZ=True, sX=True, sY=True, sZ=True, vis=True, ud=True)

def batch2Transfer(sources, dests):
	size = len(sources)
	for i in range(size):
		transferAnim(sources[i], dests[i], copyType="wholeCurves", tX=True, tY=True, tZ=True, rX=True, rY=True, rZ=True, sX=True, sY=True, sZ=True, vis=True, ud=True)

def bakeToLocs(sources):	
	dests = locatorize(sources)
	cmds.group(dests)
	batch2Transfer(sources, dests)

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


