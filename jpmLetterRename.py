import maya.cmds as cmdsallChars = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]sizeOfChars = len(allChars)capChars = []for char in allChars:	capChars.append(char.capitalize())allObjs = cmds.ls(sl=1)
numOfObjs = len(allObjs)

numOfLets = numOfObjs/26
i=0for obj in allObjs:	if i/sizeOfChars == 0:		cmds.rename( obj, allChars[i].capitalize())	else:		cmds.rename( obj, (allChars[(i/sizeOfChars - 1)].capitalize() + allChars[i%sizeOfChars].capitalize() ) )	i = i + 1