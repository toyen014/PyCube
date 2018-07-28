import numpy
#SPECIFICATIONS FOR A 3X3X3 CUBE
FRONT_UPPER_EDGE_ALTERNATIVE = 1
CORNER_ALTERNATIVE = 2 #how many colors does one CORNER_ STICKER_ have? - 3 and so for one STICKER_ of a CORNER_ piece, there are two others
NUMBER_OF_EDGES_STICKER_ONESIDE = 4
NUMBER_OF_CORNER_STICKER_ONESIDE = 4
NUMBER_OF_CENTER_STICKER_ONESIDE = 1
NUMBER_OF_TOTAL_STICKER_ONESIDE = NUMBER_OF_EDGES_STICKER_ONESIDE + NUMBER_OF_CORNER_STICKER_ONESIDE + NUMBER_OF_CENTER_STICKER_ONESIDE
NUMBER_OF_SIDES = 6
TOTAL_NUMBER_OF_STICKER = NUMBER_OF_TOTAL_STICKER_ONESIDE * NUMBER_OF_SIDES

#=====================================================================================================================================================================================================================
#LOOP POSSIBLE
SIDE_PAIRS = {"F":"B", "B":"F", "U":"D", "D":"U", "R":"L", "L":"R"}
COLOR_PAIRS = {"G":"B", "B":"G", "Y":"W", "W":"Y", "R":"O", "O":"R"}
SIDE_ORDER = ('F', 'U', 'R', 'B', 'D', 'L')

#loop possible
CORRECT_FRONT_EDGES = ('U', 'R', 'D', 'L')
CORRECT_UPPER_EDGES = ('B', 'R', 'F', 'L')
CORRECT_RIGHT_EDGES = ('B', 'D', 'F', 'U')
CORRECT_BACK_EDGES = ('L', 'D', 'R', 'U')
CORRECT_DOWN_EDGES = ('L', 'F', 'R', 'B')
CORRECT_LEFT_EDGES = ('U', 'F', 'D', 'B')
CORRECT_EDGES = (CORRECT_FRONT_EDGES, CORRECT_UPPER_EDGES, CORRECT_RIGHT_EDGES, CORRECT_BACK_EDGES, CORRECT_DOWN_EDGES, CORRECT_LEFT_EDGES)

CORRECT_FRONT_CORNERS = (("L", "U"), ("U", "R"), ("R", "D"), ("D", "L"))
CORRECT_UPPER_CORNERS = (("L", "B"), ("B", "R"), ("R", "F"), ("F", "L"))
CORRECT_RIGHT_CORNERS = (("U", "F"), ("F", "D"), ("D", "B"), ("B", "U"))
CORRECT_BACK_CORNERS = (("U", "L"), ("L", "D"), ("D", "R"), ("R", "U"))
CORRECT_DOWN_CORNERS = (("B", "L"), ("L", "F"), ("F", "R"), ("R", "B"))
CORRECT_LEFT_CORNERS = (("B", "D"), ("D", "F"), ("F", "U"), ("U", "B"))
CORRECT_CORNERS = (CORRECT_FRONT_CORNERS, CORRECT_UPPER_CORNERS, CORRECT_RIGHT_CORNERS, CORRECT_BACK_CORNERS, CORRECT_DOWN_CORNERS, CORRECT_LEFT_CORNERS)

CORRECT_CENTERS = SIDE_ORDER [:]

#====================================================================================================================================================================================================================
inputCorners = []
inputEdges = []
inputCenters = []
cubeinput = [inputEdges, inputCorners]

#with this, you'll retrieve data of one side
def collectOneSide(sideArgument):
    #inputting colors, always 9
    counter = 1
    while (counter<=(NUMBER_OF_TOTAL_STICKER_ONESIDE)):
        color = input("\r")
        #this could be looped
        if color not in COLOR_PAIRS:
            print(" You've entered an invalid color abbreviation. Please try entering the color once more.")
            continue
        if (counter)%2==0:
            inputEdges.append(color)
        elif (counter)%5==0:
            inputCenters.append(color)
        else:
            inputCorners.append(color)
        counter += 1
# CHECKER!! MISSING
#===================================================================================================================================================================================================================
# def returnSurroundings(turnDirection):
#
#
# def simpleTurn(turnDirection):#Argument is
#     current = CORRECT_EDGES[SIDE_ORDER.index(turnDirection)]
#     current[0], current[1], current[2], current[3] = current[1], current[2], current[3], current[0]
#     for rotationalCounter in NUMBER_OF_EDGES_STICKER_ONESIDE:
#         CORRECT_EDGES[]
#=====================================================================================================================================================================================================================

#=====================================================================================================================================================================================================================
zadavani_barev = ["Please choose color; that from now on will be your front face.\nWill you please enter the colors of that face, starting from the Upper-Left corner?",
    "Now turn the cube in that manner, so you see the current upper part of the cube.\nAgain, please enter the colors you see starting from the Upper-Left corner.",
    "Great. Now turn the cube, so you can view the right side.\nEnter colors, starting from the U-L corner.",
    "For the next one, please repeat the step of looking at the CURRENT upper side.\nAnd again, please type in colors, starting with the U-L corner.",
    "Now, please look on right side agan.\nPlease enter in the colors as previously.",
    "Finally, view the upper layer. \nEnter the last 9 colors."]
for colorInputColor in range(len(zadavani_barev)):
    print(zadavani_barev[colorInputColor])
    collectOneSide(SIDE_ORDER[colorInputColor])
for inputTypeCounter in cubeinput:
    inputTypeCounter = numpy.reshape(inputTypeCounter, (6, 4))
print(inputEdges + inputCorners + inputCenters)


# ==============================================================================================================================================================================================================
#CHEKS BY PRINTING OUT THE STUFF
for x in range(2):
   print('''
     === === ===
     | {} | {} | {} |
     --- --- ---
     | {} | {} | {} |
     --- --- ---
     | {} | {} | {} |
     === === ==='''.format (inputCorners [0, 0]),inputEdges([0],[0]),inputCorners([0],[1]),inputEdges([0],[1]),inputCenters([0],[0]),inputEdges([0],[2]),inputCorners([0],[2]),inputEdges([0],[3]),inputCorners([0],[3])))



#==================================================================================================================================================================================================================























#
# correctCube = []
# edgeCounter = 0
# cornerCounter = 0
#
# for sideCounter in range(NUMBER_OF_SIDES):
#     for oneSideCounter in range(NUMBER_OF_TOTAL_STICKER_ONESIDE+1):
#         if oneSideCounter%2 == 0:
#             correctCube.append(CORRECT_EDGES[sideCounter][edgeCounter])
#             edgeCounter+=1
#         elif oneSideCounter%5==0:
#             correctCube.append(CORRECT_CENTERS[sideCounter])
#         else:
#             correctCube.append(CORRECT_CORNERS[sideCounter][cornerCounter])
#             cornerCounter+=1
# print(correctCube)


# def fTurnEdge(inputFrontEdges, inputRightEdges, inputLeftEdges, inputUpperEdges, inputDownEdge):














#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
# # theCorrectCube = []
# #
# # for stickerCounter in (range(TOTAL_NUMBER_OF_STICKER)+1):
# #     for sideCounter in NUMBER_OF_SIDES
#
#
#             # if (stickerCounter%9)%2 = 1:
#                 # theCube.append(CORRECT_CORNERS([][stickerCounter]))
#             # else:
#                 # theCube.append(CORRECT_EDGES([sideCounter]))
#
# #
# #
# #
# # inputEDGES_ = ["inputFRONT_EDGES_", "inputDOWN_EDGES_", "inputBACK_EDGES_", "inputUPPER_EDGES_", "inputRIGHT_EDGES_", "inputLEFT_EDGES_"]
# #
# # # INPUT
