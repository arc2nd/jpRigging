##James Parks
##06-15-12
##Create rivets along a NURBS surface in specified numbers of rows and columns

##object = "extrudedSurface1"
##rows = 8
##columns = 12

##jpmMultiRivet(object, rows, columns)		
##jpmMultiRivet("nurbsPlane1", 4,5)



import maya.cmds as cmds
import maya.mel as mm
##import math
##import os
##import sys

import jpmMakeRivet as rivet


def jpmMultiRivet(object, rows, columns):
	i = 0
	incrU = 1.0/rows
	incrV = 1.0/columns
	
	allRivets = []
	
	initU = incrU
	initV = incrU
	
	thisU = incrU
	thisV = incrV/2
	
	for col in range(columns):
		for row in range(rows):
			##Make the rivet
			rivetName = ("rivet_c" + str(col) + "_r" + str(row))
			thisRivet = rivet.jpmMakeRivet(object, rivetName, thisU, thisV)
			allRivets.append(thisRivet[0])

			##Increments
			i = i + 1
			
			thisU = thisU + incrU
			
		thisU = initU
		thisV = thisV + incrV
		
	cmds.group(allRivets)
	
	
	