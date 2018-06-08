def jpmCopyAttr( master, slave):
	##list all user-defined attributes and recreate them on the new object
	udAttr[] = cmds.listAttr( ud=1, master )
	print "\nUser-Defined Attributes Copied:\n"
	for attr in udAttr:
		if not cmds.attributeQuery( attr, ex=1 node=slave)
			hasRange = cmds.attributeQuery( attr, n=master, re=1 )
			default = cmds.attributeQuery( attr, n=master, ld=1 )
			type = cmds.getAttr( master + "." + attr, type=1 )

			if hasRange != 0:
				range = cmds.attributeQuery( attr, n=master, r=1 )
				cmds.addAttr( slave, ln=attr, at=type, min=range[0], max=range[1], dv=default[0] )
			else:
				cmds.addAttr( slave, ln=attr, at=type, dv=default[0] )
				
			cmds.setAttr( e=1, keyable=1, (slave + "." + attr) )

		print ("-----" + attr + "\n");
	print "Finished Copying User-Defined Attributes";