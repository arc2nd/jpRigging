##James Parks 09-03-03
import jpMayaLib_Anim as animLib
import maya.cmds as cmds

class jpmTransferAnim(object):
	def __init__(self):
		print "jpTransferAnim object"
		self.sourceList = []
		self.destList = []

	def copyAttr_CB(self, *args):
		print "copyAttr_CB"
		allObjs = cmds.ls(sl=True)
		source = allObjs[0]
		dest = allObjs[1]
		animLib.copyUDAttrs(source, dest)

	def transferAnim_CB(self, *args):
		print "transferAnim_CB"
		allObjs = cmds.ls(sl=True)
		source = allObjs[0]
		dest = allObjs[1]

		cTypeRB = cmds.radioButtonGrp("copyType", q=True, sl=True)
		if cTypeRB == 1:
			cType = "wholeCurves"
		else:
			cType = "currentValues"
		traX = cmds.checkBoxGrp("transAxes", q=True, v1=True)
		traY = cmds.checkBoxGrp("transAxes", q=True, v2=True)
		traZ = cmds.checkBoxGrp("transAxes", q=True, v3=True)
		rotX = cmds.checkBoxGrp("rotAxes", q=True, v1=True)
		rotY = cmds.checkBoxGrp("rotAxes", q=True, v2=True)
		rotZ = cmds.checkBoxGrp("rotAxes", q=True, v3=True)
		sclX = cmds.checkBoxGrp("scaleAxes", q=True, v1=True)
		sclY = cmds.checkBoxGrp("scaleAxes", q=True, v2=True)
		sclZ = cmds.checkBoxGrp("scaleAxes", q=True, v3=True)
		visi = cmds.checkBoxGrp("visAttr", q=True, v1=True)
		udAttrs = cmds.checkBoxGrp("udAttrs", q=True, v1=True)

		animLib.transferAnim(source, dest, copyType=cType, tX=traX, tY=traY, tZ=traZ, rX=rotX, rY=rotY, rZ=rotZ, sX=sclX, sY=sclY, sZ=sclZ, vis=visi, ud=udAttrs)

	def batchTransfer_CB(self, *args):
		print "batchTransfer_CB"
		allObjs = cmds.ls(sl=True)
		animLib.batchTransfer(allObjs)

	def batch2Transfer_CB(self, *args):
		print "batch2Transfer_CB"
		sources = self.sourceList
		dests = self.destList
		animLib.batch2Transfer(sources, dests)

	def pickSources_CB(self, *args):
		print "pickSources_CB"
		self.sourceList = []
		self.sourceList = cmds.ls(sl=True)

	def pickDests_CB(self, *args):
		print "pickDests_CB"
		self.destList = []
		self.destList = cmds.ls(sl=True)

	def bakeToLocs_CB(self, *args):
		print "bakeToLocs_CB"
		allObjs = cmds.ls(sl=True)
		animLib.bakeToLocs(allObjs)

	def show(self):
		winName = "jpTransferAnim"
		if cmds.window(winName, exists=True):
			cmds.deleteUI(winName)
		cmds.window(winName, t="Tranfer Animation", rtf=True, wh=[200,70])

		cmds.rowColumnLayout(nr=3, rh=([1,125], [2,15], [3,90]))
		cmds.rowColumnLayout(nc=2, cw=([1,100], [2,100]))
		cmds.button(l="CopyUser Attr's", w=100, c=self.copyAttr_CB)
		cmds.button(l="Transfer", w=100, c=self.transferAnim_CB)
		cmds.button(l="Batch1 - \"ABAB\"", w=100, c=self.batchTransfer_CB)
		cmds.text(l="", w=100)
		cmds.button(l="Batch2 - \"AABB\"", w=100, c=self.batch2Transfer_CB)
		cmds.button(l="Pick Sources", w=100, c=self.pickSources_CB)
		cmds.text(l="", w=100)
		cmds.button(l="Pick Dests", w=100, c=self.pickDests_CB)
		cmds.button(l="Bake To Locs", w=100, c=self.bakeToLocs_CB)
		cmds.setParent("..")
		cmds.radioButtonGrp("copyType", w=200, h=15, nrb=2, cw=([1,100], [2,100]), l1="Whole Curves", l2="CurrentValues", sl=1)
		cmds.setParent("..")
		cmds.rowColumnLayout(nr=6, rh=([1,15], [2,15], [3,15], [4,15], [5,15], [6,15]))
		cmds.text(fn="boldLabelFont", al="center", l="Attributes To Transfer")
		cmds.checkBoxGrp("transAxes", w=200, h=15, ncb=3, label="Transform", cal=([1,"left"]), l1="X", l2="Y", l3="Z", v1=1, v2=1, v3=1, cw=([1,100], [2,33], [3,33], [4,33]))
		cmds.checkBoxGrp("rotAxes", w=200, h=15, ncb=3, label="Rotate", cal=([1,"left"]), l1="X", l2="Y", l3="Z", v1=1, v2=1, v3=1, cw=([1,100], [2,33], [3,33], [4,33]))
		cmds.checkBoxGrp("scaleAxes", w=200, h=15, ncb=3, label="Scale", cal=([1,"left"]), l1="X", l2="Y", l3="Z", v1=1, v2=1, v3=1, cw=([1,100], [2,33], [3,33], [4,33]))
		cmds.checkBoxGrp("visAttr", w=200, h=15, ncb=1, label="Visibility", v1=1, cal=([1,"left"]), cw=([1,100], [2,100]))
		cmds.checkBoxGrp("udAttrs", w=200, h=15, ncb=1, label="User Defined", v1=1, cal=([1,"left"]), cw=([1,100], [2,100]))

		cmds.showWindow(winName)