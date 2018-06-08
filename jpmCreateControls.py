import maya.cmds as cmds
import maya.mel as mm

import re


def jpmCreateDefaultRig():
	cmds.createNode( "transform", n="WORLD" )
	cmds.setAttr( ".tx", l=True )
	cmds.setAttr( ".ty", l=True )
	cmds.setAttr( ".tz", l=True )
	cmds.setAttr( ".rx", l=True )
	cmds.setAttr( ".ry", l=True )
	cmds.setAttr( ".rz", l=True )
	cmds.setAttr( ".sx", l=True )
	cmds.setAttr( ".sy", l=True )
	cmds.setAttr( ".sz", l=True )

	cmds.createNode( "transform", n="CONTROLS", p="WORLD" )
	cmds.setAttr( ".tx", l=True )
	cmds.setAttr( ".ty", l=True )
	cmds.setAttr( ".tz", l=True )
	cmds.setAttr( ".rx", l=True )
	cmds.setAttr( ".ry", l=True )
	cmds.setAttr( ".rz", l=True )
	cmds.setAttr( ".sx", l=True )
	cmds.setAttr( ".sy", l=True )
	cmds.setAttr( ".sz", l=True )

	cmds.createNode( "transform", n="constraint_GRP", p="CONTROLS" )
	cmds.createNode( "transform", n="offset_CTRL", p="constraint_GRP" )
	trans = cmds.createNode( "transform", n="trans_CTRL", p="offset_CTRL" )
	cmds.addAttr( sn="hiLo", ln="hiLo", min=0, max=1, at="long" )
	cmds.setAttr( ".ove", 1 )
	cmds.setAttr( ".ovc", 6 )
	cmds.setAttr( ".hiLo", 1, k=0, cb=1 )

	cmds.createNode( "nurbsCurve", n="trans_CTRLShape", p="trans_CTRL" )
	cmds.setAttr( ".v", k=False )
	tempCmd = """
	setAttr ".cc" -type "nurbsCurve" 
		1 16 0 no 3
		17 0 0.39018064403225655 0.78036128806451321 1.1705419320967698 1.5607225761290264
		 1.950903220161283 2.3410838641935396 2.731264508225796 3.1214451522580524 3.5116257962903088
		 3.9018064403225652 4.2919870843548216 4.6821677283870784 5.0723483724193352 5.4625290164515921
		 5.8527096604838489 6.2428903045161057
		17
		2.5849939301196182e-016 2.5849939301196182e-016 -4.2217548880928932
		-1.0323720986750149 1.526084061930856e-016 -2.4923667220367975
		-2.9852315098779392 1.8278667373136461e-016 -2.9852315098779387
		-2.4923667220367975 6.3212471577318266e-017 -1.0323720986750149
		-4.2217548880928932 -1.2871197840266917e-032 2.102095550964913e-016
		-2.4923667220367975 -6.321247157731829e-017 1.0323720986750153
		-2.9852315098779387 -1.8278667373136468e-016 2.9852315098779396
		-1.0323720986750147 -1.526084061930856e-016 2.4923667220367975
		4.445640291507179e-016 -2.5849939301196182e-016 6.8578142579036632
		1.0323720986750158 -1.5260840619308553e-016 2.4923667220367971
		2.9852315098779396 -1.8278667373136458e-016 2.9852315098779383
		2.4923667220367975 -6.3212471577318241e-017 1.0323720986750142
		4.2217548880928932 5.5919994536293008e-032 -9.1327297725917102e-016
		2.4923667220367971 6.3212471577318327e-017 -1.0323720986750162
		2.9852315098779378 1.8278667373136468e-016 -2.9852315098779396
		1.0323720986750138 1.526084061930856e-016 -2.4923667220367975
		-1.381981925367624e-015 2.5849939301196177e-016 -4.2217548880928923 
	"""
	mm.eval( tempCmd )

		
	cmds.createNode( "nurbsCurve", n="transTop_CTRLShape", p="trans_CTRL" )
	cmds.setAttr(".v", k=False )
	tempCmd = """
	setAttr ".cc" -type "nurbsCurve" 
		1 9 0 no 3
		10 0 1 2 3 4 5 6 7 8 9
		10
		-0.9035742917670978 16.818880087052964 7.093475906820267e-017
		-7.093475906820267e-017 16.818880087052964 -0.9035742917670978
		0.9035742917670978 16.818880087052964 -7.093475906820267e-017
		7.093475906820267e-017 16.818880087052964 0.9035742917670978
		-0.9035742917670978 16.818880087052964 7.093475906820267e-017
		0 14.702854515815675 0
		7.093475906820267e-017 16.818880087052964 0.9035742917670978
		0.9035742917670978 16.818880087052964 -7.093475906820267e-017
		0 14.702854515815675 0
		-7.093475906820267e-017 16.818880087052964 -0.9035742917670978
	"""
	mm.eval( tempCmd )

	pivot = cmds.createNode( "transform", n="pivot_CTRL", p="trans_CTRL" )
	cmds.createNode( "nurbsCurve", n="pivot_CTRLShape", p="pivot_CTRL" )
	cmds.setAttr( ".v", k=False )
	tempCmd = """
	setAttr ".cc" -type "nurbsCurve" 
		3 16 2 no 3
		21 -2 -1 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18
		19
		-0.38617398388040047 -0.98004272312850105 -0.93230646931970274
		-2.2084043143423484e-016 -0.98004272312850105 -1.0091212506737868
		0.38617398388040103 -0.98004272312850105 -0.93230646931970274
		0.71355647939089228 -0.98004272312850116 -0.71355647939088196
		0.93230646931971317 -0.98004272312850116 -0.3861739838803907
		1.0091212506737979 -0.98004272312850116 1.037948354854368e-014
		0.93230646931971295 -0.98004272312850116 0.38617398388041146
		0.71355647939089228 -0.98004272312850116 0.71355647939090305
		0.38617398388040092 -0.98004272312850105 0.93230646931972405
		-6.9964740211345664e-017 -0.98004272312850105 1.0091212506738085
		-0.38617398388040125 -0.98004272312850105 0.93230646931972361
		-0.71355647939089217 -0.98004272312850094 0.7135564793909025
		-0.93230646931971339 -0.98004272312850094 0.3861739838804113
		-1.0091212506737977 -0.98004272312850094 1.037948354854368e-014
		-0.93230646931971317 -0.98004272312850094 -0.3861739838803907
		-0.71355647939089206 -0.98004272312850094 -0.71355647939088196
		-0.38617398388040047 -0.98004272312850105 -0.93230646931970274
		-2.2084043143423484e-016 -0.98004272312850105 -1.0091212506737868
		0.38617398388040103 -0.98004272312850105 -0.93230646931970274
	"""
	mm.eval( tempCmd )

	cmds.createNode( "nurbsCurve", n="pivot_CTRLShape1", p="pivot_CTRL" )
	cmds.setAttr( ".v", k=False )
	tempCmd = """
	setAttr ".cc" -type "nurbsCurve" 
		3 16 2 no 3
		21 -2 -1 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18
		19
		-0.38617398388040058 -1.9123491924482132 1.037948354854368e-014
		-3.4441806096946631e-016 -1.989163973802297 1.037948354854368e-014
		0.38617398388040092 -1.9123491924482132 1.037948354854368e-014
		0.71355647939089217 -1.6935992025193933 1.037948354854368e-014
		0.93230646931971306 -1.366216707008902 1.037948354854368e-014
		1.0091212506737979 -0.98004272312850116 1.037948354854368e-014
		0.93230646931971295 -0.59386873924810046 1.037948354854368e-014
		0.7135564793908924 -0.26648624373760726 1.037948354854368e-014
		0.38617398388040103 -0.047736253808787231 1.037948354854368e-014
		5.3612889323885981e-017 0.029078527545296613 1.037948354854368e-014
		-0.38617398388040114 -0.047736253808787134 1.037948354854368e-014
		-0.71355647939089206 -0.26648624373760704 1.037948354854368e-014
		-0.93230646931971339 -0.59386873924810024 1.037948354854368e-014
		-1.0091212506737977 -0.98004272312850094 1.037948354854368e-014
		-0.93230646931971328 -1.3662167070089015 1.037948354854368e-014
		-0.71355647939089217 -1.6935992025193933 1.037948354854368e-014
		-0.38617398388040058 -1.9123491924482132 1.037948354854368e-014
		-3.4441806096946631e-016 -1.989163973802297 1.037948354854368e-014
		0.38617398388040092 -1.9123491924482132 1.037948354854368e-014
	"""
	mm.eval( tempCmd )

	cmds.createNode( "nurbsCurve", n="pivot_CTRLShape2", p="pivot_CTRL" )
	cmds.setAttr( ".v", k=False )
	tempCmd = """
	setAttr ".cc" -type "nurbsCurve" 
		3 16 2 no 3
		21 -2 -1 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18
		19
		-4.5253738480370412e-017 -1.9123491924482132 -0.38617398388038954
		4.3440238583795614e-017 -1.989163973802297 1.037948354854368e-014
		1.2624196088572755e-016 -1.9123491924482132 0.38617398388041146
		1.90545616804438e-016 -1.6935992025193933 0.71355647939090283
		2.2656155764039574e-016 -1.3662167070089017 0.93230646931972361
		2.2880668288664299e-016 -0.98004272312850105 1.0091212506738085
		1.9693919257654934e-016 -0.59386873924810035 0.9323064693197235
		1.3581062323030817e-016 -0.26648624373760715 0.71355647939090283
		5.4727245399022776e-017 -0.047736253808787182 0.38617398388041146
		-3.3966731665143379e-017 0.029078527545296613 1.037948354854368e-014
		-1.1676845396707527e-016 -0.047736253808787182 -0.3861739838803907
		-1.810721098857856e-016 -0.26648624373760715 -0.71355647939088196
		-2.1708805072174371e-016 -0.59386873924810035 -0.93230646931970274
		-2.1933317596799073e-016 -0.98004272312850105 -1.0091212506737868
		-1.8746568565789721e-016 -1.3662167070089017 -0.93230646931970274
		-1.2633711631165577e-016 -1.6935992025193933 -0.71355647939088152
		-4.5253738480370412e-017 -1.9123491924482132 -0.38617398388038954
		4.3440238583795614e-017 -1.989163973802297 1.037948354854368e-014
		1.2624196088572755e-016 -1.9123491924482132 0.38617398388041146
	"""
	mm.eval( tempCmd )

	cmds.createNode( "transform", n="GEOMETRY", p="WORLD" )
	cmds.setAttr( ".ovdt", 2 )
	cmds.setAttr( ".ove", True )

	cmds.createNode( "pointConstraint", n="GEOMETRY_pointConstraint1", p="GEOMETRY" )
	cmds.addAttr( sn="w0", ln="pivot_CTRLW0", bt="W000", dv=1, min=0, at="double" )
	cmds.setAttr( ".nds", k=True )
	cmds.setAttr( ".v", k=False )
	cmds.setAttr( ".tx", k=False )
	cmds.setAttr( ".ty", k=False )
	cmds.setAttr( ".tz", k=False )
	cmds.setAttr( ".rx", k=False )
	cmds.setAttr( ".ry", k=False )
	cmds.setAttr( ".rz", k=False )
	cmds.setAttr( ".sx", k=False )
	cmds.setAttr( ".sy", k=False )
	cmds.setAttr( ".sz", k=False )
	cmds.setAttr( ".erp", True )
	cmds.setAttr( ".w0", k=True )

	cmds.createNode( "orientConstraint", n="GEOMETRY_orientConstraint1", p="GEOMETRY" )
	cmds.addAttr( sn="w0", ln="pivot_CTRLW0", bt="W000", dv=1, min=0, at="double" )
	cmds.setAttr( ".nds", k=True )
	cmds.setAttr( ".v", k=False )
	cmds.setAttr( ".tx", k=False )
	cmds.setAttr( ".ty", k=False )
	cmds.setAttr( ".tz", k=False )
	cmds.setAttr( ".rx", k=False )
	cmds.setAttr( ".ry", k=False )
	cmds.setAttr( ".rz", k=False )
	cmds.setAttr( ".sx", k=False )
	cmds.setAttr( ".sy", k=False )
	cmds.setAttr( ".sz", k=False )
	cmds.setAttr( ".erp", True )
	cmds.setAttr( ".w0", k=True )

	cmds.createNode( "scaleConstraint", n="GEOMETRY_scaleConstraint1", p="GEOMETRY" )
	cmds.addAttr( sn="w0", ln="pivot_CTRLW0", bt="W000", dv=1, min=0, at="double" )
	cmds.setAttr( ".nds", k=True )
	cmds.setAttr( ".v", k=False )
	cmds.setAttr( ".tx", k=False )
	cmds.setAttr( ".ty", k=False )
	cmds.setAttr( ".tz", k=False )
	cmds.setAttr( ".rx", k=False )
	cmds.setAttr( ".ry", k=False )
	cmds.setAttr( ".rz", k=False )
	cmds.setAttr( ".sx", k=False )
	cmds.setAttr( ".sy", k=False )
	cmds.setAttr( ".sz", k=False )
	cmds.setAttr( ".erp", True )
	cmds.setAttr( ".w0", k=True )

	cmds.createNode( "transform", n="GRP", p="GEOMETRY" )
	cmds.createNode( "transform", n="loRes", p="GRP" )
	cmds.setAttr( ".tx", l=True )
	cmds.setAttr( ".ty", l=True )
	cmds.setAttr( ".tz", l=True )
	cmds.setAttr( ".rx", l=True )
	cmds.setAttr( ".ry", l=True )
	cmds.setAttr( ".rz", l=True )
	cmds.setAttr( ".sx", l=True )
	cmds.setAttr( ".sy", l=True )
	cmds.setAttr( ".sz", l=True )

	cmds.createNode( "transform", n="hiRes", p="GRP" )

	cmds.createNode( "reverse", n="reverse1" )

	cmds.connectAttr( "GEOMETRY_pointConstraint1.ctx", "GEOMETRY.tx" )
	cmds.connectAttr( "GEOMETRY_pointConstraint1.cty", "GEOMETRY.ty" )
	cmds.connectAttr( "GEOMETRY_pointConstraint1.ctz", "GEOMETRY.tz" )
	cmds.connectAttr( "GEOMETRY_orientConstraint1.crx", "GEOMETRY.rx" )
	cmds.connectAttr( "GEOMETRY_orientConstraint1.cry", "GEOMETRY.ry" )
	cmds.connectAttr( "GEOMETRY_orientConstraint1.crz", "GEOMETRY.rz" )
	cmds.connectAttr( "GEOMETRY_scaleConstraint1.csx", "GEOMETRY.sx" )
	cmds.connectAttr( "GEOMETRY_scaleConstraint1.csy", "GEOMETRY.sy" )
	cmds.connectAttr( "GEOMETRY_scaleConstraint1.csz", "GEOMETRY.sz" )
	cmds.connectAttr( "GEOMETRY.pim", "GEOMETRY_pointConstraint1.cpim" )
	cmds.connectAttr( "GEOMETRY.rp", "GEOMETRY_pointConstraint1.crp" )
	cmds.connectAttr( "GEOMETRY.rpt", "GEOMETRY_pointConstraint1.crt" )

	cmds.connectAttr( "pivot_CTRL.t", "GEOMETRY_pointConstraint1.tg[0].tt" )
	cmds.connectAttr( "pivot_CTRL.rp", "GEOMETRY_pointConstraint1.tg[0].trp" )
	cmds.connectAttr( "pivot_CTRL.rpt", "GEOMETRY_pointConstraint1.tg[0].trt" )
	cmds.connectAttr( "pivot_CTRL.pm", "GEOMETRY_pointConstraint1.tg[0].tpm" )

	cmds.connectAttr( "GEOMETRY_pointConstraint1.w0", "GEOMETRY_pointConstraint1.tg[0].tw" )
	cmds.connectAttr( "GEOMETRY.ro", "GEOMETRY_orientConstraint1.cro" )
	cmds.connectAttr( "GEOMETRY.pim", "GEOMETRY_orientConstraint1.cpim" )

	cmds.connectAttr( "pivot_CTRL.r", "GEOMETRY_orientConstraint1.tg[0].tr" )
	cmds.connectAttr( "pivot_CTRL.ro", "GEOMETRY_orientConstraint1.tg[0].tro" )
	cmds.connectAttr( "pivot_CTRL.pm", "GEOMETRY_orientConstraint1.tg[0].tpm" )
	cmds.connectAttr( "GEOMETRY_orientConstraint1.w0", "GEOMETRY_orientConstraint1.tg[0].tw" )

	cmds.connectAttr( "GEOMETRY.pim", "GEOMETRY_scaleConstraint1.cpim" )
	cmds.connectAttr( "pivot_CTRL.s", "GEOMETRY_scaleConstraint1.tg[0].ts" )
	cmds.connectAttr( "pivot_CTRL.pm", "GEOMETRY_scaleConstraint1.tg[0].tpm" )
	cmds.connectAttr( "GEOMETRY_scaleConstraint1.w0", "GEOMETRY_scaleConstraint1.tg[0].tw" )

	cmds.connectAttr( "reverse1.ox", "loRes.v" )
	cmds.connectAttr( "trans_CTRL.hiLo", "hiRes.v" )
	cmds.connectAttr( "trans_CTRL.hiLo", "reverse1.ix" )
	cmds.connectAttr( "reverse1.msg", ":defaultRenderUtilityList1.u", na=True )

	return trans, pivot


def jpmCreatePVArrow( name ):
	if name == "":
		transformNode = cmds.createNode( "transform", n="Arrow_CTRL" )
	else:
		transformNode = cmds.createNode( "transform", n=(name + "_CTRL") )
	cmds.setAttr( ".rp", 0, 21.604083934761103, 0, type="double3" )
	cmds.setAttr( ".sp", 0, 21.604083934761103, 0, type="double3" ) ## 0 21.604083934761103 0 
	cmds.createNode( "nurbsCurve", n=(transformNode + "Shape"), p=transformNode )
	cmds.setAttr( ".v", k=False )
	tempCmd = """
	setAttr ".cc" -type "nurbsCurve" 
		1 7 0 no 3
		8 0 0.86776747823511613 1.7355349564702323 2.6033024347053488 3.4710699129404654
		 4.3388373911755815 5.2066048694106977 6.0743723476458147
		8
		-1.8369095307335659e-016 20.604083934761103 -1.6081428723391245e-016
		0.59506061137965627 21.59373323518869 -6.9388939039072013e-017
		0.2220669070073662 21.603213102768141 6.9388939039072493e-017
		0.43388373911755851 22.604083934761103 1.4488866631167306e-016
		-0.43388373911755784 22.604083934761103 1.4488866631167306e-016
		-0.2220669070073662 21.603213102768148 6.9388939039072567e-017
		-0.5950606113796566 21.59373323518869 -6.9388939039072013e-017
		-4.6124670922964572e-016 20.604083934761103 -1.6081428723391252e-016
	"""
	mm.eval( tempCmd )
	cmds.select( transformNode )
	return transformNode


def jpmCreatePivotCTRLShape(name=""):
	if name == "":
		transformNode = cmds.createNode( "transform", n="Sphere_ctrl" )
	else:
		transformNode = cmds.createNode( "transform", n=(name + "_ctrl") )
	cmds.setAttr( ".sp", 0, 0, 0, type="double3" )
	cmds.createNode( "nurbsCurve", n=(transformNode + "Shape"), p=transformNode )
	cmds.setAttr( ".v", k=False )
	tempCmd = """
	setAttr ".cc" -type "nurbsCurve" 
		3 16 2 no 3
		21 -2 -1 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18
		19
		3.4366936756842077 8.7217336461463049 -8.2969124815585786
		8.9726509488121291e-016 8.7217336461463049 -8.9805133565476218
		-3.4366936756842148 8.7217336461463049 -8.2969124815585786
		-6.3501818929512561 8.7217336461463049 -6.3501818929511629
		-8.2969124815586728 8.7217336461463049 -3.436693675684122
		-8.9805133565477213 8.7217336461463049 9.2370555648813024e-014
		-8.296912481558671 8.7217336461463049 3.4366936756843067
		-6.3501818929512561 8.7217336461463049 6.3501818929513512
		-3.4366936756842139 8.7217336461463049 8.2969124815587687
		-4.4542901576289594e-016 8.7217336461463049 8.9805133565478137
		3.4366936756842148 8.7217336461463049 8.2969124815587652
		6.3501818929512535 8.7217336461463049 6.3501818929513458
		8.2969124815586728 8.7217336461463049 3.4366936756843049
		8.980513356547716 8.7217336461463049 9.2370555648813024e-014
		8.296912481558671 8.7217336461463049 -3.436693675684122
		6.3501818929512517 8.7217336461463049 -6.3501818929511629
		3.4366936756842077 8.7217336461463049 -8.2969124815585786
		8.9726509488121291e-016 8.7217336461463049 -8.9805133565476218
		-3.4366936756842148 8.7217336461463049 -8.2969124815585786
	"""
	mm.eval( tempCmd )

	cmds.createNode( "nurbsCurve", n=(transformNode + "Shape1"), p=transformNode )
	cmds.setAttr( ".v", k=False )
	tempCmd = """
	setAttr ".cc" -type "nurbsCurve" 
		3 16 2 no 3
		21 -2 -1 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18
		19
		3.4366936756842077 17.018646127704969 9.2370555648813024e-014
		8.9726509488121291e-016 17.702247002694008 9.2370555648813024e-014
		-3.4366936756842148 17.018646127704969 9.2370555648813024e-014
		-6.3501818929512561 15.07191553909756 9.2370555648813024e-014
		-8.2969124815586728 12.158427321830516 9.2370555648813024e-014
		-8.9805133565477213 8.7217336461463049 9.2370555648813024e-014
		-8.296912481558671 5.2850399704620941 9.2370555648813024e-014
		-6.3501818929512561 2.3715517531950354 9.2370555648813024e-014
		-3.4366936756842139 0.42482116458762675 9.2370555648813024e-014
		-4.4542901576289594e-016 -0.2587797104014129 9.2370555648813024e-014
		3.4366936756842148 0.42482116458762675 9.2370555648813024e-014
		6.3501818929512535 2.3715517531950354 9.2370555648813024e-014
		8.2969124815586728 5.2850399704620941 9.2370555648813024e-014
		8.980513356547716 8.7217336461463049 9.2370555648813024e-014
		8.296912481558671 12.158427321830516 9.2370555648813024e-014
		6.3501818929512517 15.07191553909756 9.2370555648813024e-014
		3.4366936756842077 17.018646127704969 9.2370555648813024e-014
		8.9726509488121291e-016 17.702247002694008 9.2370555648813024e-014
		-3.4366936756842148 17.018646127704969 9.2370555648813024e-014
	"""
	mm.eval( tempCmd )

	cmds.createNode( "nurbsCurve", n=(transformNode + "Shape2"), p=transformNode )
	cmds.setAttr( ".v", k=False )
	tempCmd = """
	setAttr ".cc" -type "nurbsCurve" 
		3 16 2 no 3
		21 -2 -1 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18
		19
		-1.6813858021235122e-015 17.018646127704969 -3.4366936756841113
		-2.5544178790530078e-015 17.702247002694008 9.2370555648813024e-014
		-3.207584381054821e-015 17.018646127704969 3.4366936756843067
		-3.5414466291682588e-015 15.07191553909756 6.3501818929513494
		-3.5051771225868643e-015 12.158427321830516 8.2969124815587652
		-3.1042975649037621e-015 8.7217336461463049 8.9805133565478137
		-2.3998382347939609e-015 5.2850399704620941 8.2969124815587634
		-1.4990466793269523e-015 2.3715517531950354 6.3501818929513494
		-5.3906024712680123e-016 0.42482116458762675 3.4366936756843067
		3.3397182980269548e-016 -0.2587797104014129 9.2370555648813024e-014
		9.8713833180450809e-016 0.42482116458762675 -3.436693675684122
		1.3210005799179447e-015 2.3715517531950354 -6.3501818929511629
		1.2847310733365518e-015 5.2850399704620941 -8.2969124815585786
		8.8385151565344749e-016 8.7217336461463049 -8.9805133565476218
		1.7939218554364758e-016 12.158427321830516 -8.2969124815585786
		-7.2139936992336144e-016 15.07191553909756 -6.3501818929511593
		-1.6813858021235122e-015 17.018646127704969 -3.4366936756841113
		-2.5544178790530078e-015 17.702247002694008 9.2370555648813024e-014
		-3.207584381054821e-015 17.018646127704969 3.4366936756843067
	"""
	mm.eval(tempCmd)
	cmds.select( transformNode )
	return transformNode


def jpmCreateTopTransCTRLShape(name=""):
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
		-3.2695972730969305 7.6568706088243985 2.5667850107112632e-016
		-2.5667850107112632e-016 7.6568706088243985 -3.2695972730969305
		3.2695972730969305 7.6568706088243985 -2.5667850107112632e-016
		2.5667850107112632e-016 7.6568706088243985 3.2695972730969305
		-3.2695972730969305 7.6568706088243985 2.5667850107112632e-016
		0 0 0
		2.5667850107112632e-016 7.6568706088243985 3.2695972730969305
		3.2695972730969305 7.6568706088243985 -2.5667850107112632e-016
		0 0 0
		-2.5667850107112632e-016 7.6568706088243985 -3.2695972730969305
	"""
	mm.eval( tempCmd )
	cmds.select( transformNode )
	return transformNode


def jpmCreateCubeCTRLShape( name ):
	if name == "":
		transformNode = cmds.createNode( "transform", n="Cube_CTRL" )
	else:
		transformNode = cmds.createNode( "transform", n=(name + "_CTRL") )
	cmds.setAttr( ".t", -1.5680030265428871e-014, -8.8817841970011971e-016, 1.3385268919885202e-015, type="double3" )
	cmds.setAttr( ".r", -1.4032955127785321e-014, -1.4032955127785321e-014, 1.4032955127785321e-014, type="double3" )
	cmds.setAttr( ".rp", -1.1588795329010843e-016, 6.3680390100319908, 0.024728240848780322, type="double3" )
	cmds.setAttr( ".sp", -1.1588795329010843e-016, 6.3680390100319908, 0.024728240848780322, type="double3" )
	cmds.createNode( "nurbsCurve", n=(transformNode + "Shape"), p=transformNode )
	cmds.setAttr( ".v", k=False )
	tempCmd = """
	setAttr ".cc" -type "nurbsCurve" 
		1 16 0 no 3
		17 0 0.0625 0.125 0.1875 0.25 0.3125 0.375 0.4375 0.5 0.5625 0.625 0.6875 0.75
		 0.8125 0.875 0.9375 1
		17
		2.3194955435178888 5.5727642415227461 2.3084895721825029
		2.3194955435178888 5.5727642415227461 -2.9775983427050172
		2.3194955435178888 8.6098559695918322 -2.9775983427050172
		2.3194955435178888 8.6098559695918322 2.3084895721825029
		-2.3224970176413917 8.6098559695918322 2.3084062569612027
		-2.3224970176413917 8.6098559695918322 -2.9775983427050172
		2.3194955435178888 8.6098559695918322 -2.9775983427050172
		2.3194955435178888 5.5727642415227461 -2.9775983427050172
		-2.3224970176413917 5.5727642415227461 -2.9775983427050172
		-2.3224970176413917 8.6098559695918322 -2.9775983427050172
		-2.3224970176413917 8.6098559695918322 2.3084062569612027
		-2.3224970176413917 5.5727642415227461 2.3084062569612027
		2.3194955435178888 5.5727642415227461 2.3084895721825029
		2.3194955435178888 8.6098559695918322 2.3084895721825029
		-2.3224970176413917 8.6098559695918322 2.3084062569612027
		-2.3224970176413917 5.5727642415227461 2.3084062569612027
		-2.3224970176413917 5.5727642415227461 -2.9775983427050172
	"""
	mm.eval( tempCmd )
	cmds.select( transformNode )
	return transformNode

def jpmCreateCubeTwoCTRLShape( name ):
	if name == "":
		transformNode = cmds.createNode( "transform", n="Cube_CTRL" )
	else:
		transformNode = cmds.createNode( "transform", n=(name + "_CTRL") )
	cmds.createNode( "nurbsCurve", n=(transformNode + "Shape"), p=transformNode )
	cmds.setAttr( ".v", k=False )
	tempCmd = """
	setAttr ".cc" -type "nurbsCurve" 
		1 16 0 no 3
		17 0 0.0625 0.125 0.1875 0.25 0.3125 0.375 0.4375 0.5 0.5625 0.625 0.6875 0.75
		 0.8125 0.875 0.9375 1
		17
		1 0 1
		1 0 -1
		1 2 -1
		1 2 1
		-1 2 1
		-1 2 -1
		1 2 -1
		1 0 -1
		-1 0 -1
		-1 2 -1
		-1 2 1
		-1 0 1
		1 0 1
		1 2 1
		-1 2 1
		-1 0 1
		-1 0 -1
	"""
	mm.eval( tempCmd )
	cmds.select( transformNode )
	return transformNode

def jpmCreatePivot( name ):
	if name == "":
		transformNode = cmds.createNode( "transform", n="RotatePivot_CTRL" )
	else:
		transformNode = cmds.createNode( "transform", n=(name + "_CTRL") )
	cmds.setAttr( ".v", l=False, k=True )
	cmds.setAttr( ".rx", l=False, k=True )
	cmds.setAttr( ".ry", l=False, k=True )
	cmds.setAttr( ".rz", l=False, k=True )
	cmds.setAttr( ".sx", l=False, k=True )
	cmds.setAttr( ".sy", l=False, k=True )
	cmds.setAttr( ".sz", l=False, k=True )
	cmds.createNode( "nurbsCurve", n=(transformNode + "Shape"), p=transformNode)
	tempCmd = """
	setAttr ".cc" -type "nurbsCurve" 
		1 40 0 no 3
		41 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 21 22 23 24 25 26 27 28 29 30 31 32 33
		 34 35 36 37 38 39 40 41 42 43 44 48 49
		41
		0.00027026134873264573 0 -0.48295078555756277
		0.00027026134873264573 0.04681445281954482 -0.28622775564261815
		0.00027026134873264573 0 -0.31724066850894472
		0.00027026134873264573 -0.04681445281954482 -0.28622775564261815
		0.00027026134873264573 0 -0.48295078555756277
		0.00027026134873264573 0 -0.31724066850894472
		0.00027026134873264573 0 0.00028417007083714196
		0.00027026134873264573 0 0.31819815387748474
		0.00027026134873264573 0 0.4829507855575772
		0.00027026134873264573 0.046543955432853647 0.28736443592594763
		0.00027026134873264573 0 0.31819815387748474
		0.00027026134873264573 -0.046543955432853647 0.28736443592594763
		0.00027026134873264573 0 0.4829507855575772
		0.00027026134873264573 0 0.31819815387748474
		0.00027026134873264573 0 0.00028417007083714196
		0.00027026134873264573 0 0.00028417007083714196
		0.00027026134873264573 -0.32058948929605674 0.00028417007083714196
		-0.04441393275851984 -0.29098779719272228 0.00028417007083714196
		0.00027026134873264573 -0.47875908414913337 0.00028417007083714196
		0.044954455455985143 -0.29098779719272228 0.00028417007083714196
		0.00027026134873264573 -0.32058948929605674 0.00028417007083714196
		0.00027026134873264573 0 0.00028417007083714196
		0.31707600453549428 0 0.00028417007083714196
		0.48455544385728117 0 0.00028417007083714196
		0.28573196018204039 0.047314300719933679 0.00028417007083714196
		0.31707600453549428 0 0.00028417007083714196
		0.28573196018204039 -0.047314300719933679 0.00028417007083714196
		0.48455544385728117 0 0.00028417007083714196
		0.31707600453549428 0 0.00028417007083714196
		0.00027026134873264573 0 0.00028417007083714196
		-0.31616538334891375 0 0.00028417007083714196
		-0.2846509147871093 -0.047571558594920287 0.00028417007083714196
		-0.48455544385728117 0 0.00028417007083714196
		-0.2846509147871093 0.047571558594920287 0.00028417007083714196
		-0.31616538334891375 0 0.00028417007083714196
		0.00027026134873264573 0 0.00028417007083714196
		-7.0256300777060687e-017 0.31616538334891375 0.00028417007083714196
		-0.047571558594920349 0.2846509147871093 0.00028417007083714196
		-1.0759292209556318e-016 0.48455544385728117 0.00028417007083714196
		0.047571558594920224 0.2846509147871093 0.00028417007083714196
		-8.3266726846886741e-017 0.31616538334891375 0.00028417007083714196
		;
	"""
	mm.eval( tempCmd )
	cmds.select( transformNode )
	return transformNode

def jpmCreateStraightCompass( name ):
	if name == "":
		transformNode = cmds.createNode( "transform", n="straightCompass_CTRL" )
	else:
		transformNode = cmds.createNode( "transform", n=(name + "_CTRL") )
	cmds.setAttr( ".rp", 0, 0, 0, type="double3" )
	cmds.setAttr( ".sp", 0, 0, 0, type="double3" )
	cmds.createNode( "nurbsCurve", n=(transformNode + "Shape"), p=transformNode )
	cmds.setAttr( ".v", k=False )
	tempCmd = """
	setAttr ".cc" -type "nurbsCurve" 
		1 24 0 no 3
		25 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24
		25
		1.5100141398616076 -8.8817841970012523e-016 1.006814637648324
		2.0134374445789143 -8.8817841970012523e-016 0.00012788714515576949
		1.5101420270067636 -8.8817841970012523e-016 -1.0066228069305903
		1.5101100552204745 -8.8817841970012523e-016 -0.50326344578586157
		0.50339133293101734 0 -0.50332738935843957
		0.50345527650359512 0 -1.5100461116478967
		1.0068146376483236 0 -1.510014139861608
		0.00012788714515578456 8.8817841970012523e-016 -2.0134374445789143
		-1.0066228069305903 0 -1.5101420270067636
		-0.5032634457858618 0 -1.5101100552204745
		-0.50332738935843957 0 -0.50339133293101734
		-1.5100461116478974 0 -0.50345527650359534
		-1.5100141398616078 0 -1.0068146376483238
		-2.0134374445789138 0 -0.00012788714515554744
		-1.5101420270067643 0 1.0066228069305905
		-1.5101100552204747 0 0.50326344578586191
		-0.50339133293101779 0 0.50332738935843979
		-0.50345527650359556 0 1.5100461116478971
		-1.006814637648324 0 1.510014139861608
		-0.00012788714515619851 -8.8817841970012523e-016 2.0134374445789143
		1.0066228069305898 0 1.5101420270067636
		0.50326344578586135 0 1.5101100552204749
		0.50332738935843913 0 0.50339133293101757
		1.5100461116478967 -8.8817841970012523e-016 0.50345527650359545
		1.5100141398616076 -8.8817841970012523e-016 1.006814637648324
	"""
	mm.eval( tempCmd )
	cmds.select( transformNode )
	return transformNode


def jpmCreateAngledCompass( name ):
	if name == "":
		transformNode = cmds.createNode( "transform", n="angledCompass_CTRL" )
	else:
		transformNode = cmds.createNode( "transform", n=(name + "_CTRL") )
	cmds.setAttr( ".rp", 0, 0, 0, type="double3" )
	cmds.setAttr( ".sp", 0, 0, 0, type="double3" )
	cmds.createNode( "nurbsCurve", n=(transformNode + "Shape"), p=transformNode )
	cmds.setAttr( ".v", k=False )
	tempCmd = """
	setAttr ".cc" -type "nurbsCurve" 
		1 24 0 no 3
		25 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24
		25
		0.61345279489009374 0 0.93174043503344905
		-0.0070406582847747463 0 1.2372846876331001
		-0.62401378231725702 1.7763568394002505e-015 0.92418659641619971
		-0.31464713801541999 0 0.92607505607051255
		-0.68243920933809854 1.7763568394002505e-015 0.59614592603596417
		-0.92986009747670739 1.7763568394002505e-015 0.30365579294533801
		-0.93162026204790049 1.7763568394002505e-015 0.61297696485361319
		-1.237466577207351 1.7763568394002505e-015 -0.0075538386172491201
		-0.92457960376312809 1.7763568394002505e-015 -0.62430772277948621
		-0.92633976833431941 1.7763568394002505e-015 -0.3149865508712113
		-0.67471756476095035 1.7763568394002505e-015 -0.60346978901168713
		-0.30408615058825783 0 -0.92985197537913655
		-0.61345279489009752 1.7763568394002505e-015 -0.93174043503344905
		0.0070406582847731729 0 -1.237284687633099
		0.62401378231725457 0 -0.92418659641619905
		0.3146471380154171 0 -0.92607505607051177
		0.68243920933809832 0 -0.59614592603596184
		0.92986009747670584 0 -0.30365579294533795
		0.93162026204789627 0 -0.61297696485361275
		1.2374665772073488 0 0.0075538386172498972
		0.92457960376312476 0 0.62430772277948698
		0.92633976833431741 0 0.31498655087121241
		0.67471756476094302 0 0.60346978901168802
		0.30408615058825672 0 0.92985197537913766
		0.61345279489009374 0 0.93174043503344905
	"""
	mm.eval(tempCmd)
	cmds.select( transformNode )
	return transformNode
	
def jpmCreateCurvedCompass( name ):
	if name == "":
		transformNode = cmds.createNode( "transform", n="curvedCompass_CTRL" )
	else:
		transformNode = cmds.createNode( "transform", n=(name + "_CTRL") )
	cmds.setAttr( ".rp", 0, 0, 0, type="double3" )
	cmds.setAttr( ".sp", 0, 0, 0, type="double3" )
	cmds.createNode( "nurbsCurve", n=(transformNode + "Shape"), p=transformNode )
	cmds.setAttr( ".v", k=False )
	tempCmd = """
	setAttr ".cc" -type "nurbsCurve" 
		1 40 0 no 3
		41 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27
		 28 29 30 31 32 33 34 35 36 37 38 39 40
		41
		-0.37644932285437899 0.81351261549545573 0.3767563729058212
		-0.37683750363584162 0.62358643761252397 0.83747625587171015
		-0.37752935293310269 0.28533253816003656 1.3358240387269267
		-0.38001433611817836 -0.10926932742706474 1.6993940687114253
		-0.75446490576511771 -0.1085025719117324 1.6993946600244185
		-0.0036524641937544277 -0.81531552871798629 1.9610810718649332
		0.75004749814407023 -0.1115833341727489 1.6993922841761622
		0.37391939716677569 -0.11081314360749495 1.6993928781382266
		0.37469605448296706 0.2687383090405393 1.3554207269359879
		0.37546180050617539 0.64312572956734337 0.79804253855442653
		0.37580687910021859 0.81197223436494714 0.37675518498169325
		0.85473459013003872 0.6508367020226673 0.37663091912115121
		1.3183403804291753 0.29908337472727986 0.37635965101982638
		1.7127821379850707 -0.17564305627581955 0.37599354748193647
		1.7127821379850707 -0.17593312244281267 0.75212232516355293
		1.8254196093626804 -0.58911176478448213 -0.00045431618552083108
		1.7127821379850707 -0.17477285777484175 -0.752392785562912
		1.7127821379850707 -0.1750629239418342 -0.37626400788129555
		1.388497755693447 0.23655538158241551 -0.37594657260053044
		0.90250593392676803 0.61810414025277005 -0.37565232660682923
		0.37580687910021859 0.81255236669893316 -0.37550237038154055
		0.37546189986078821 0.64440427246834475 -0.79692736836945688
		0.37475850848428444 0.30129773040160557 -1.3152114978977947
		0.37391939716677569 -0.10819190905768727 -1.6995617723041283
		0.75004749814407023 -0.10896209962294101 -1.6995623662661927
		-0.0036524641937544277 -0.81228983460690851 -1.9623362623133396
		-0.75446490576511771 -0.10588133736192429 -1.6995599904179368
		-0.37833680478793535 -0.10665152792717847 -1.6995605843800003
		-0.37753384622619601 0.2852004175121825 -1.3382452636177806
		-0.37680565855707049 0.64040934200891164 -0.81079945388144825
		-0.37644932285437899 0.8140927478294413 -0.37550118245741171
		-0.81664711783750943 0.6746421373422169 -0.37560872515679833
		-1.3277145355904734 0.29914533189605663 -0.37589830395410662
		-1.7174579985309599 -0.16803888457110938 -0.37625859102329873
		-1.7174579985309599 -0.16774881840411671 -0.75238736870491607
		-1.8317890116384872 -0.58162296624020349 -0.00044854091061985457
		-1.7174579985309599 -0.16890908307208807 0.75212774202154975
		-1.7174579985309599 -0.16861901690509518 0.37599896433993329
		-1.3184911600893072 0.30679370602525213 0.3763655971382267
		-0.75472760063252708 0.69367787835862482 0.37666395774129047
		-0.37644932285437899 0.81351261549545573 0.3767563729058212
		;
	"""
	mm.eval(tempCmd)
	cmds.select( transformNode )
	return transformNode


def jpmCreateCircle( name ):
	if name == "":
		cmds.circle( c=(0, 0, 0), nr=(0, 1, 0), sw=360, r=1, d=1, ut=0, tol=0.01, s=16, ch=1 ) 
	else:
		cmds.circle( c=(0, 0, 0), nr=(0, 1, 0), sw=360, r=1, d=1, ut=0, tol=0.01, s=16, ch=1, n=(name + "_CTRL") ) 
	mm.eval( "objectMoveCommand" )


def jpmCreateLocator():
	cmds.spaceLocator( p=(0, 0 ,0) )


def jpmCreateTriangle( name ):
	if name == "":
		transformNode = cmds.createNode( "transform", n="triangle_CTRL" )
	else:
		transformNode = cmds.createNode( "transform", n=(name + "_CTRL") )
	cmds.createNode( "nurbsCurve", n=(transformNode + "Shape"), p=transformNode )
	cmds.setAttr( ".v", k=False )
	tempCmd = """
	setAttr ".cc" -type "nurbsCurve" 
		1 3 0 no 3
		4 0 1.7320508075688772 3.4641016151377544 5.1961524227066311
		4
		6.1230317691118863e-017 1.5 -2.718365896964281e-016
		-0.86602540378443871 2.7755575615628914e-016 -3.0615158845559481e-017
		0.86602540378443837 -3.3306690738754696e-016 -3.0615158845559382e-017
		6.7185298123495496e-016 1.4999999999999998 -2.7183658969642805e-016
	"""
	mm.eval( tempCmd )
	cmds.select( transformNode )
	return transformNode
	
def jpmCreateCapsule():
	cmds.cylinder( p=(0,0,0), ax=(0,1,0), ssw=0, esw=360, r=5, hr=0.4, d=3, ut=0, tol=0.01, s=8, nsp=1, ch=0 )

	
import re

def jpmCreateIso():
	selected = cmds.ls( sl=True )
	for isoThing in selected:
		isoGrp = cmds.group( em=True ) 
		print isoGrp
		cmds.select( clear=True )
		cmds.select( isoThing )
		cmds.select( isoGrp, add=True )
		things = cmds.ls( sl=True )
		print things
		
		master = things[0]
		slave = things[1]
		
		#The ConstraintSnap -- recreated here for you amusement and eddification
		cmds.select( cl=True )
		cmds.select( master )
		cmds.select( slave, add=True )
		
		#create constraints
		cmds.pointConstraint( n="tempPoint", weight=1 )
		cmds.orientConstraint( n="tempOrient", weight=1 )
		cmds.scaleConstraint( n="tempScale", weight=1 )
	
		#delete constraints -> leaving transform information
		cmds.select( "tempPoint" )
		cmds.select( "tempOrient", add=True )
		cmds.select( "tempScale", add=True )
		cmds.delete()
		#end of the Constraint Snap
		
		
		thingParent = cmds.listRelatives( isoThing, p=True )
		print thingParent
		if thingParent != None:
			cmds.parent( isoGrp, thingParent[0] )
		cmds.select( isoGrp )
		#cmds.makeIdentity( apply=True, t=1, r=0, s=0 )
		cmds.parent( isoThing, isoGrp )

		isoTok = re.split("_", isoThing)
		print isoTok

		isoName = ""
		for i in range(len(isoTok)-1):
			if i == 0:
				isoName = isoTok[i]
			else:
				isoName = isoName + "_" + isoTok[i]
				
		cmds.rename( isoGrp, (isoName + "_ISO") )
		
def jpmCreateSlider(sliderName="default"):
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

def jpmCreateControls():
	winName = "createControlsWin"
	if ( cmds.window( winName, exists=True) ):
		cmds.deleteUI( winName )
	cmds.window( winName, t="CreateControls", rtf=True )

	cmds.rowColumnLayout()
	cmds.button( h=25, w=125, en=True, al="left", l="Default_RIG", c="jpmCreateDefaultRig()" )
	cmds.separator();
	cmds.button( h=25, w=125, en=True, al="left", l="Arrow", c="jpmCreatePVArrow(\"\")" )
	cmds.button( h=25, w=125, en=True, al="left", l="Sphere", c="jpmCreatePivotCTRLShape(\"\")" )
	cmds.button( h=25, w=125, en=True, al="left", l="Half Diamond", c="jpmCreateTopTransCTRLShape(\"\")" )
	cmds.button( h=25, w=125, en=True, al="left", l="Cube1", c="jpmCreateCubeCTRLShape(\"\")" )
	cmds.button( h=25, w=125, en=True, al="left", l="Cube2", c="jpmCreateCubeTwoCTRLShape(\"\" )" )
	cmds.button( h=25, w=125, en=True, al="left", l="Pivot", c="jpmCreatePivot(\"\")" )
	cmds.button( h=25, w=125, en=True, al="left", l="Straight Compass", c="jpmCreateStraightCompass(\"\")" )
	cmds.button( h=25, w=125, en=True, al="left", l="Angled Compass", c="jpmCreateAngledCompass(\"\")" )
	cmds.button( h=25 ,w=125, en=True, al="left", l="Curved Compass", c="jpmCreateCurvedCompass(\"\")" )
	cmds.button( h=25, w=125, en=True, al="left", l="Circle", c="jpmCreateCircle(\"\")" )
	cmds.button( h=25, w=125, en=True, al="left", l="Triangle", c="jpmCreateTriangle(\"\")" )
	cmds.button( h=25, w=125, en=True, al="left", l="Locator", c="jpmCreateLocator()" )
	cmds.button( h=25, w=125, en=True, al="left", l="Slider", c="jpmCreateSlider()" )
	cmds.separator()
	cmds.button( h=25, w=135, en=True, al="left", l="Capsule", c="jpmCreateCapsule()" )
	cmds.button( h=25, w=125, en=True, al="left", l="Iso", c="jpmCreateIso()" )

	cmds.showWindow( winName )
