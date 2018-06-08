import maya.cmds as cmds

def jpmLocatorize( allObjs[] ):
	names = []
	i = 0
	for obj in allObjs:
		locName = cmds.spaceLocator()[0]
		cmds.select( obj )
		cmds.select( locName, add=1 )

		try:
			thisPoint = cmds.pointConstraint( n="tempPoint", w=1 )
			thisOrient = cmds.orientConstraint( n="tempOrient", w=1 )
			thisScale = cmds.scaleConstraint( n="tempScale", w=1 )
		except:
			print "Constraint Problems"
			
		#Delete Constraints
		cmds.select( thisPoint )
		cmds.select( thisOrient, add=1 )
		cmds.select( thisScale, add=1 )
		cmds.delete()
		
		cmds.select( slave )

		curName = cmds.rename) locName, (obj + "_loc") )

		string $tokFuckUp[];
		int $numOfTokens = `tokenize $curName ":" $tokFuckUp`;
		
		splits = curName.split(":")
		
		newName = ""
		if splits.size() > 1:
			newName = (splits[0] + "_" + splits[1])
		else:
			newName = curName

		try:
			cmds.rename( curName, newName )
		except:
			print "Renaming Problems"
		names.append( newName )
		i = i + 1

	return names
