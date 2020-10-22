"""  Victor Li
VARIABLE MAP
VARIABLE                 PURPOSE                             TYPE         RANGE(5x6) RANGE(10x10)
imageListNames           list of all images                  List         N/A        N/A
photoList                list of all loaded images           List         N/A        N/A
loadedVariableList       list of all variables(String)       List         N/A        N/A
varList                  list of all variables(int)          List         N/A        N/A
snakesLadders            list of all spots for snak and lad  List         N/A        N/A
bkx                      background x                        Int          0          0
bky                      background y                        Int          0          0
bkWidth                  background width                    Int          800        800
bkHeight                 background height                   Int          800        800
row                      squares per row                     Int          6          10
col                      squares per collume                 Int          5          10
gameBoard                number of total squares             Int          30         100
gameSquares              lists and numbers the squares       Int          N/A        N/A
startSquareX             x refrence point for create grid    Int          0          0
startSquareY             y refremce point for create grid    Int          0          0
squareX                  x point for squares                 Int          
squareY                  y point for squares                 Int 
squareWidth              the width of the squares            Int
squareHeight             the height of the squares           Int
rMostSquarex             the right-most square x loc         Int
numSquares               number of game squares              Int         30          100
diceX                    x loc of dice                       Int         0           0
diceY                    y loc of dice                       Int         800         800
diceLength               length of dice                      Int         100         100
diceWidth                width of dice                       Int         250         250
diceText                 text of dice("ROLL")                Str         N/A         N/A
whichSquare              which square you have clicked       Int         (-1)-0      (-1)-0
removeSquare             to make square unclickable          Bool        T/F         T/F
numGameItums             number of clickable Boundaries      Int         1           1
activeSquares            the list of clickable areas         List        N/A         N/A
diceBoundaries           clickable areas for dice            List        N/A         N/A
num                      dice roll number                    Int         0-6         0-6
lastNum                  last dice roll number               Int         0-6         0-6
rollText                 the text of what # you have rolled  Str         N/A         N/A
rollX                    the x Location of roll text         Int
rollY                    the y Locaiton of roll text         Int
rollWidth                the width of roll text              Int
rollHeight               the height of roll test             Int
diceNum                  all numbers on dice                 List        N/A         N/A
playerLoc                location of both players            List        N/A         N/A
moveCounter              number of moves done                Int         Infinite    Infinite
player1Win               test for P1 win                     Str         N/A         N/A
player2Win               text for P2 win                     Str         N/A         N/A
"""

import random
def setup():
    global bkx, bky, bkWidth, bkHeight, row, col 
    global  gameSquares, startSquareX ,startSquareY,squareX ,squareY ,squareWidth ,squareHeight, numSquares, rMostSquareX 
    global diceX, diceY, diceWidth, diceHeight, diceText
    global whichSquare, removeSquare , numGameItems , activeSquares, diceBoundaries
    global num , playerLoc, moveCounter, photoList, gameBoard, snakes, ladders, varList
    global rollText, rollWidth, rollHeight, rollX,rollY, diceNum, snakesLadders, player1Win, player2Win
    size (800,900)
    if (random.randint(0,1)) == 0:
        ##snakes and ladders 5X6 (LIST AND LOADED VARIABLELIST BELOW IS FOR 5x6 BOARD)
        snakesLadders = [[3,22],[5,8],[11,26],[17,4],[19,7],[20,29],[21,9],[27,1]]
        loadedVariableList = load30Variables()
         
    else:  
        ##snakes and ladders 10X10 (LIST AND LOADED VARIABLE LIST BELOW IS FOR 10x10 BOARD)
        snakesLadders = [[4,25],[13,46],[27,5],[33,49],[40,3],[42,63],[43,18],[50,69],[54,31],[62,81],[66,45],[74,92],[76,58],[99,41]]
        loadedVariableList = load100Variables() #CHANGE BOARD 
    #load stuff from file
    imageListNames = loadImageNames()
    photoList = loadImages( imageListNames ) #photoList[0] == 6x5, photoList[1] == 10x10
    varList = stringtoint(loadedVariableList)
    
    #Parameters
    bkx = varList[0]
    bky = varList[1]
    bkWidth = varList[2]
    bkHeight = varList[3]
    
    row = varList[4] #changes 30 == 6, 100 == 10
    col = varList[5] #changes 30 == 5, 100 == 10
    gameBoard = varList[6] #changes 30 == 0, 100 == 1
    
    #Create Grid
    gameSquares= []
    startSquareX = bkx
    startSquareY = (bkHeight/col) * (col - 1)
    squareX = startSquareX
    squareY = startSquareY
    squareWidth = bkWidth/row
    squareHeight = bkHeight/col
    rMostSquareX = startSquareX + (squareWidth * (row-1))
    
    numSquares = row * col
    
    #dice
    diceX = varList[7]
    diceY= varList[8]
    diceHeight = varList[9]
    diceWidth = varList[10]
    diceText = "Roll"
    
    whichSquare = varList[11]
    removeSquare = False 
    numGameItems = varList[12]
    activeSquares = [ True for i in range(numGameItems)]
    diceBoundaries = []
    
    num = varList[13]
    lastNum = varList[13]
    
    rollText = "You have rolled"
    rollX = diceX + diceWidth
    rollY = diceY
    rollWidth = bkWidth - diceWidth
    rollHeight = bkHeight - diceHeight
    diceNum = ["1","2","3","4","5","6"]
    
    playerLoc = [0,0]
    moveCounter = varList[14]
    
    player1Win = "player 1 Wins"
    player2Win = "player 2 Wins"

##LOADS IN THE 6X5 VARIABLES       
def load30Variables():
    
    file = open("30variables.txt")
    fileList = []                  #Start with an empty list
    text = file.readlines()
     
    for line in text:
        line = line.strip() #Gets rid of end-of-line markers, etc.
        row = ""
        for c in line:
            row = row + c
        rowList = row.split( ",")
    file.close

    return ( rowList )

##LOADS IN THE 10X10 VARIABLES
def load100Variables():
    
    file = open("100variables.txt")
    fileList = []                  #Start with an empty list
    text = file.readlines()
     
    for line in text:
        line = line.strip() #Gets rid of end-of-line markers, etc.
        row = ""
        for c in line:
            row = row + c
        rowList = row.split( ",")
    file.close

    return ( rowList )

##MAKES THE STRINGS INTO LIST
def stringtoint(List):
    newList = []
    for i in range (len(List)):
         newList.append(int(List[i]))
    return( newList )

##LOADS IN THE IMAGES NAMES
def loadImageNames():
    
    file = open("images.txt")
    fileList = []                  #Start with an empty list
    text = file.readlines()
     
    for line in text:
        line = line.strip() #Gets rid of end-of-line markers, etc.
        row = ""
        for c in line:
            row = row + c
        rowList = row.split( ",")
    file.close
    return ( rowList )

##LOADS IN THE IMAGES
def loadImages( imageListNames ):
     
    numImages = len( imageListNames )
    imageList = [ "" for i in range( numImages ) ]
    for i in range( numImages ):
        imageList[ i ] = loadImage( imageListNames[ i ] )

    return( imageList )

##SAYS WHO WINS    
def gameOver(winner):
    global rollX,rollY,rollWidth,rollHeight
    fill (225)
    rect(rollX,rollY,rollWidth,rollHeight)
    
    textSize(64)
    fill(0)
    text ( winner, rollX,rollY,rollWidth,rollHeight)
    
    

##RESETS ONCE SOMEONE WINS 
def reset():
    global moveCounter, num, lastnum,playerLoc, varList
    moveCounter = varList[14]
    num = varList[13]
    lastNum = varList[13]
    playerLoc = [0,0]

##CHECKS IF ON SNAKE OR LADDER
def locCheck(num):
    global numSquares, playerLoc, lastNum, moveCounter, snakesLadders
    if playerLoc[moveCounter % 2] + num > (numSquares-1):
        num = 0
    for i in range (len(snakesLadders)):
        if playerLoc[moveCounter % 2] == (snakesLadders[i][0]) - 1:
            playerLoc[moveCounter % 2] = (snakesLadders [i][1]) -1    
    move(num)
    for i in range (len(snakesLadders)):
        if playerLoc[moveCounter % 2] == (snakesLadders[i][0]) - 1:
            playerLoc[moveCounter % 2] = (snakesLadders [i][1]) -1

##MOVES PLAYERS   
def move(num):
    global playerLoc, moveCounter
    turn =  determineMove()
    playerLoc[turn] += num
    moveCounter += 1 
    print(moveCounter)

## DETERMINES WHOS TURNS IS IT                
def determineMove():
    global moveCounter
    if ((moveCounter+1) % 2) != 0:
        return (0)
    else:
        return (1)
    
## DICE ROLLER    
def dice():
    num = random.randint(1,6)    
    return num

##MOUSE ROUTINE
def mouseReleased():
    global diceBoundaries, whichSquare, removeSquare, activeSquares, numGameItems, gameBoundaries, num, lastNum
    
#  all Boundaries is a list of tuples,  each tuple is the upper left and lower right of each box
#  if removeSquare is True, you will not be able to click again in that square again as that place in activeSquares will be turned to False
    whichSquare = - 1

    for i in range( numGameItems ):
        if activeSquares[ i ]:
            validXRange = diceBoundaries[i][0][0] <= mouseX <= diceBoundaries[i][1][0] 
            validYRange = diceBoundaries[i][0][1]  <= mouseY <= diceBoundaries[i][1][1]
            validLocation = validXRange and validYRange
            if validLocation:
                whichSquare = i
                break
        else:
            validLocation = False
    if validLocation and removeSquare:
        activeSquares[ whichSquare ] = False
        
    if whichSquare == 0:
        num = dice()
        locCheck(num)
        lastNum = num
        num = 0
        
##    
def createDiceArea ():
    global diceX, diceY, diceWidth, diceLength, diceBoundaries, diceText, moveCounter
    global rollText, rollWidth, rollHeight, rollX,rollY
    upperLeft =  [ diceX,diceY ]
    lowerRight = [ diceX  + diceWidth, diceY + diceHeight ]
    clickBoundary = [ upperLeft, lowerRight ]
    fill(225)
    rect( diceX , diceY, diceWidth, diceHeight )
    rect (rollX,rollY,rollWidth,rollHeight)
    fill(0)
    textSize(64)
    text(diceText, diceX , diceY, diceWidth, diceHeight) 
    diceBoundaries.append( clickBoundary )
    
    if moveCounter > 0:
        text( "Rolled" ,rollX,rollY,rollWidth,rollHeight)
        text ( diceNum[lastNum-1] , rollX + 200, rollY,rollWidth,rollHeight)
    if moveCounter % 2 == 0:
        text( "P1 Turn", rollX + 300,rollY,rollWidth,rollHeight)
    else:
        text( "P2 Turn", rollX + 300,rollY,rollWidth,rollHeight)
    
def createOddGameRow (x ,y):
    global row, startSquareX, startSquareY ,squareHeight ,squareWidth, gameSquares 
    for i in range( row ):
        loc =  [ x,y ]
        fill(255-i*25)
        rect( x , y, squareWidth, squareHeight )
        gameSquares.append( loc )
    
        x = x + squareWidth
   
        
def createEvenGameRow (x ,y):
    global row, startSquareX, startSquareY ,squareHeight ,squareWidth, gameSquares
    for i in range( row ):
        loc =  [ x,y ]
        fill(255-i*25)
        rect( x , y, squareWidth, squareHeight )
        gameSquares.append( loc )
    
        x = x - squareWidth
    
def player1(loc):
    global gameSquares, squareWidth, squareHeight, player1Loc,row
    fill(0)
    ellipseMode (CENTER) 
    x = (gameSquares[loc][0]) + (squareWidth/2)
    y = (gameSquares[loc][1]) + (squareHeight/4) 
    ellipse(x,y,squareWidth/4,squareHeight/4)
    
def player2(loc):
    global gameSquares, squareWidth, squareHeight, player1Loc,row
    fill(255)
    ellipseMode (CENTER) 
    x = (gameSquares[loc][0]) + (squareWidth/2)
    y = (gameSquares[loc][1]) + (squareHeight/4) * 3
    ellipse(x,y,squareWidth/4,squareHeight/4)
            
def draw():
    global squareX,squareY, squareHeight, rMostSquareX,gameSquares, num, startSquareX, startSquareY, playerLoc, photoList, gameBoard, numSquares
    global bkx, bky, bkWidth, bkHeight
    global player1Win, player2Win
    
    createDiceArea()
    for i in range (row):
        if ((i+1) % 2) != 0: 
            createOddGameRow(squareX,squareY)
        else:
            createEvenGameRow(rMostSquareX,squareY)
        squareY -= squareHeight
    image (photoList[gameBoard], bkx, bky, bkWidth, bkHeight)
    player1(playerLoc[0])
    player2(playerLoc[1])
    print(playerLoc[0])
    for i in range (len(playerLoc)):
        if (playerLoc[i]) == (numSquares - 1):
            if i == 0:
                gameOver(player1Win)
                reset()
            elif i == 1:
                gameOver(player2Win)
                reset()
    squareX = startSquareX
    squareY = startSquareY

    
    
    
    
