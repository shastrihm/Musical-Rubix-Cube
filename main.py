import Rubix as rx 
import MusicalNotes as mn 
import pygame as pg
import pygButton as btn 

pg.init()

pg.mixer.init()

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 600
RUBIX_CUBE_SIZE = 160
BUTTON_SPACING = 10
screen = pg.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
BTNDict = None
pg.display.set_caption("Musical Cube")

# The loop will carry on until the user exit the game (e.g. clicks the close button).
carryOn = True
 
# The clock will be used to control how fast the screen updates
clock = pg.time.Clock()

# Define some colors
BLACK = ( 0, 0, 0)
WHITE = ( 255, 255, 255)
GREEN = ( 0, 255, 0)
RED = ( 255, 0, 0)
BLUE = ( 0, 110, 255)
ORANGE = ( 255, 172, 48)
YELLOW = (247, 255, 20)
GREY = ( 188, 188, 188)
colorsDict = {
                "green":GREEN,
                "white":WHITE,
                "red":RED,
                "blue":BLUE,
                "orange":ORANGE,
                "yellow":YELLOW
            }

def drawLine():
    pg.draw.lines(screen, BLACK, closed, pointlist, thickness)

# centered at x,y
def drawSquare(x,y,sqrwidth,color):
    pg.draw.rect(screen, color, ((x)-(sqrwidth/2),(y)-(sqrwidth/2),sqrwidth,sqrwidth), 1)

# uncentered
def drawColoredGrid(x,y,sqrwidth,color,note,orientation,face5=False):
    pg.draw.rect(screen, color, (x,y,sqrwidth,sqrwidth), 0)
    pg.draw.rect(screen, BLACK, (x,y,sqrwidth,sqrwidth), 1)
    noteify(note,x,y,orientation,sqrwidth,face5)


def drawUnfoldedCube(sqrwidth):
    drawSquare(SCREEN_WIDTH/2,SCREEN_HEIGHT/2,sqrwidth,BLACK)
    drawSquare(SCREEN_WIDTH/2-sqrwidth,SCREEN_HEIGHT/2,sqrwidth,BLACK)
    drawSquare(SCREEN_WIDTH/2,SCREEN_HEIGHT/2-sqrwidth,sqrwidth,BLACK)
    drawSquare(SCREEN_WIDTH/2+sqrwidth,SCREEN_HEIGHT/2,sqrwidth,BLACK)
    drawSquare(SCREEN_WIDTH/2,SCREEN_HEIGHT/2+sqrwidth,sqrwidth,BLACK)
    drawSquare(SCREEN_WIDTH/2+sqrwidth*2,SCREEN_HEIGHT/2,sqrwidth,BLACK)

    cuboidSize = sqrwidth/3
    # returns starting spots to draw grid of each square [green,red,yellow,orange,white,blue]
    return [(SCREEN_WIDTH/2 - sqrwidth/2,SCREEN_HEIGHT/2 - sqrwidth/2),
            (SCREEN_WIDTH/2 + sqrwidth/2,SCREEN_HEIGHT/2 + sqrwidth/2 - cuboidSize),
            (SCREEN_WIDTH/2 - sqrwidth/2,SCREEN_HEIGHT/2 + sqrwidth/2),
            (SCREEN_WIDTH/2 - sqrwidth/2 - cuboidSize,SCREEN_HEIGHT/2 - sqrwidth/2),
            (SCREEN_WIDTH/2 + sqrwidth/2 - cuboidSize,SCREEN_HEIGHT/2 - sqrwidth/2 - cuboidSize),
            (SCREEN_WIDTH/2 + sqrwidth*2.5 - cuboidSize,SCREEN_HEIGHT/2 - sqrwidth/2)]

def drawCube2D(cube,sqrwidth):
    counter = 0
    base = drawUnfoldedCube(sqrwidth)
    cuboidSize = sqrwidth/3
    arrayRep = cube.display()
    notes = cube.noteDisplay()
    
    # green
    for j in range(0,3):
        for k in range(0,3):
            drawColoredGrid(base[0][0]+cuboidSize*k,base[0][1]+cuboidSize*j,cuboidSize,colorsDict[arrayRep[0][counter]],notes[0][counter],0)
            counter+=1

    counter = 0

    # red
    for j in range(0,3):
        for k in range(0,3):
            drawColoredGrid(base[1][0]+cuboidSize*j,base[1][1]-cuboidSize*k,cuboidSize,colorsDict[arrayRep[1][counter]],notes[1][counter],1)
            counter+=1

    counter = 0

    # yellow
    for j in range(0,3):
        for k in range(0,3):
            drawColoredGrid(base[2][0]+cuboidSize*k,base[2][1]+cuboidSize*j,cuboidSize,colorsDict[arrayRep[2][counter]],notes[2][counter],0)
            counter+=1

    counter = 0

    # orange
    for j in range(0,3):
        for k in range(0,3):
            drawColoredGrid(base[3][0]-cuboidSize*j,base[3][1]+cuboidSize*k,cuboidSize,colorsDict[arrayRep[3][counter]],notes[3][counter],3)
            counter+=1

    counter = 0

    # white
    for j in range(0,3):
        for k in range(0,3):
            drawColoredGrid(base[4][0]-cuboidSize*k,base[4][1]-cuboidSize*j,cuboidSize,colorsDict[arrayRep[4][counter]],notes[4][counter],2)
            counter+=1

    counter = 0

    # blue
    for j in range(0,3):
        for k in range(0,3):
            drawColoredGrid(base[5][0]-cuboidSize*k,base[5][1]+cuboidSize*j,cuboidSize,colorsDict[arrayRep[5][counter]],notes[5][counter],2,face5=True)
            counter+=1

def noteify(note,x,y,orientation,sqrsize,face5=False):
    # orientation = 0 (normal) 1 (on its back) 2 (upside down) 3 (on its stomach) 4 (normal)
    font = pg.font.SysFont("Calibri", round(.5*sqrsize))
    label = font.render(note, 1, BLACK)
    label = pg.transform.rotate(label,90.0*orientation)
    if face5:
        label = pg.transform.flip(label,False,True)
    screen.blit(label, (x,y))


def playCubeCurrentState(cube):
    for face in cube.faces:
        face.playFace()



def initBtns(color,startgridx,startgridy, width, height, cube):
    x = startgridx
    y = startgridy
    labels = [
            ("Rotate Left Away", cube.rotateLeft, True),
            ("Rotate Left Toward", cube.rotateLeft, False),
            ("Rotate Right Away", cube.rotateRight, True),
            ("Rotate Right Toward", cube.rotateRight, False), 
            ("Rotate Top CW", cube.rotateTop, True), 
            ("Rotate Top CCW", cube.rotateTop, False), 
            ("Rotate Bottom CW", cube.rotateBottom, True),
            ("Rotate Bottom CCW", cube.rotateBottom, False), 
            ("Rotate Front CW", cube.rotateFront, True), 
            ("Rotate Front CCW", cube.rotateFront, False), 
            ("Rotate Back CW", cube.rotateBack, True), 
            ("Rotate Back CCW", cube.rotateBack, False),
            ("Reset", cube.reset, None),
            ("Play Current Cube State!", playCubeCurrentState, cube)]

    buttons = {}
    i = 0
    for label in labels:
        button = btn.button(color,x,y+(height+BUTTON_SPACING)*i,width,height,label[0])
        button.draw(screen,outline=True)
        buttons[label] = button
        i+=1
        

    return buttons


# -------- ON startup -----------
screen.fill(GREY)
CUBE = rx.RubixCube()
drawCube2D(CUBE,RUBIX_CUBE_SIZE)
BTNDict = initBtns(WHITE,5,5,SCREEN_WIDTH*(1/5),30,CUBE)


# -------- Main Program Loop -----------
while carryOn:
    # --- Main event loop
    for event in pg.event.get(): # User did something

        pos = pg.mouse.get_pos()

        if event.type == pg.QUIT: # If user clicked close
              carryOn = False # Flag that we are done so we exit this loop

        if event.type == pg.MOUSEBUTTONDOWN:
            for k,v in BTNDict.items():
                if v.isOver(pos):
                    print('clicked')
                    fun = k[1]
                    fun(k[2])
                    break

 
    # --- Game logic should go here
    drawCube2D(CUBE,RUBIX_CUBE_SIZE)


    # --- Drawing code should go here
    # First, clear the screen to white. 

    #screen.fill(WHITE)


    

    # --- Go ahead and update the screen with what we've drawn.
    pg.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(60)
 

pg.quit()






