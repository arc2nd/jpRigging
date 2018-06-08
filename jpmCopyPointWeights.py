class jpmCopyPointWeights(object):
	def __init__(self):
		self.sourceWeights = []
		self.gui()
		
	def storePointWeights(self,  *args):
		print args
		sourcePoints = cmds.ls(sl=True, fl=True)
		sourcePoint = sourcePoints[0]

		sourceParts = sourcePoint.split("[")[-1].split("]")
		intSourcePoint = sourceParts[0]

		##Find the skinClusters 
		skinList = cmds.listHistory(sourcePoint)
		skinList = cmds.ls(skinList, type="skinCluster")
		sourceSkin = skinList[0]

		allJoints = cmds.skinCluster(sourceSkin, q=True, wi=True)

	##
	#	int $jointCount = `size($allJoints)`;
	#	//float $sourceWeights[];
	#	for($k=0; $k < $jointCount; $k++)
	#	{
	#		$sourceWeights[$k] = `getAttr($sourceSkin + ".weightList[" + $intSourcePoint + "].w[" + $k + "]")`;
	#	}//end for: copyWeights
	##

		everyJoint = cmds.ls(type="joint")
		everyJointCount = len(everyJoint)
		for k in range(everyJointCount):
			self.sourceWeights.append(cmds.getAttr(sourceSkin + ".weightList[" + str(intSourcePoint) + "].w[" + str(k) + "]"))

		print self.sourceWeights


	def pastePointWeights(self, *args):
		print args
		destPoints = cmds.ls(sl=True, fl=True)

		##Find the skinClusters 
		skinList = cmds.listHistory(destPoints[0])
		skinList = cmds.ls(skinList, type="skinCluster")
		sourceSkin = skinList[0]

		allJoints = cmds.skinCluster(sourceSkin, q=True, wi=True)

		jointCount = len(allJoints)

		oldNormWeights = cmds.getAttr(sourceSkin + ".normalizeWeights")
		cmds.setAttr(sourceSkin + ".normalizeWeights", 0)

		for thisPoint in destPoints:
			destParts = thisPoint.split("[")[-1].split("]")
			intDestPoint = destParts[0]

	#		/*for($k=0; $k < $jointCount; $k++)
	#		{
	#			setAttr($sourceSkin + ".weightList[" + $intDestPoint + "].w[" + $k + "]") $sourceWeights[$k];
	#		}//end for: pasteWeights
	#		*/

			everyJoint = cmds.ls(type="joint")
			everyJointCount = len(everyJoint)
			for k in range(everyJointCount):
				cmds.setAttr(sourceSkin + ".weightList[" + str(intDestPoint) + "].w[" + str(k) + "]", sourceWeights[k])

		cmds.setAttr(sourceSkin + ".normalizeWeights", oldNormWeights)

	def switchVerts(self, newObj):
		curSel = cmds.ls(sl=True)
		vertsToSelect = []
		
		for thisObj in curSel: #thisObj = curSel[0]
			if ".vtx" in thisObj:
				vertNum = thisObj.split("[")[-1].split("]")[0]
				vertsToSelect.append(vertNum)
				
		cmds.select(clear=True)
				
		for thisVert in vertsToSelect: #thisVert = vertsToSelect[0]
			cmds.select(newObj + ".vtx[" + thisVert + "]", toggle=True)
			
	def switchVerts_collectAndCall(self, *args):
		newGeoName = cmds.textFieldGrp("newGeoGrp", q=True, tx=True)
		self.switchVerts(newGeoName)

	def gui(self):
		winName = "jpmCopyPointWeights";
		if cmds.window(winName, exists=True):
			cmds.deleteUI(winName)
			
		cmds.window(winName, t="Copy Point Weights", rtf=True)

		cmds.rowColumnLayout(nr=2, rh=([1,25],[2,25]))
			
		cmds.button(l="Store", w=100, c=self.storePointWeights)
		cmds.button(l="Paste", w=100, c=self.pastePointWeights)
		cmds.textFieldGrp( "newGeoGrp", l="Geo Name : ", cl2=("left","left"), cw2=(75,150) )
		cmds.button( l="Switch Geo", c=self.switchVerts_collectAndCall)

		cmds.showWindow(winName)