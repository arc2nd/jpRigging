import maya.cmds as cmds

def jpmKeyAllControls(selected):
	for control in selected:
		keyableAttrs = cmds.listAttr( control, r=1, w=1, k=1, u=1, v=1, m=1, s=1 )
		for attr in keyableAttrs:
			cmds.setKeyframe( control, at=attr )