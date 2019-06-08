# -*- coding: utf-8 -*-
"""
Created on Mon Mar 25 19:30:17 2019

@author: varbalk@gmail.com
@author: daniel.varro@gmail.com
"""

import pygame
from wallPosition import WallPosition
from boardPosition import BoardPosition

pygame.init()

bgColor = (212, 212, 212)
blackColor = (0, 0, 0)
darkColor = (50, 50, 50)
whiteColor = (255, 255, 255)
wallColor = (77, 38, 0)
lineColor = (50, 50, 50)
tileColor = (255, 117, 26)
tileColor2 = (255, 212, 128)
tile_size = 50
init_x = 20
init_y = 20
gap_size = tile_size // 5
player_size = tile_size // 2 -5 
display_width = 800
display_height = 600

def text_objects(text, font):
    textSurface = font.render(text, True, blackColor)
    return textSurface, textSurface.get_rect()

def displayText(screen, text, centerWidth, centerHeight):
    largeText = pygame.font.Font('freesansbold.ttf',18)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = (centerWidth, centerHeight)
    screen.blit(TextSurf, TextRect)

#display_width - 130,(display_height/2)-10    
def drawBoard(screen):
    screen.fill(bgColor)
    pygame.draw.rect(screen, tileColor2, 
                             [init_x, 
                              init_y, 
                              (tile_size + gap_size)*9, 
                              (tile_size + gap_size)*9])
    #pygame.draw.rect(screen, lineColor, [10, 10, tile_size, tile_size], 3)
    for row in range(0,9):
        for col in range(0,9):
            pygame.draw.rect(screen, lineColor, 
                             [init_x + (tile_size + gap_size)*col, 
                              init_y + (tile_size + gap_size)*row, 
                              tile_size, tile_size], 1)
    
def drawPlayer(screen, row, col, color):
    if (color == "B"):
        pygame.draw.circle(screen, blackColor, 
                                 [init_x + (tile_size + gap_size)*col + tile_size//2, 
                                  init_y + (tile_size + gap_size)*row + tile_size//2], 
                                  player_size)
    elif (color == "W"):
        pygame.draw.circle(screen, whiteColor, 
                                 [init_x + (tile_size + gap_size)*col + tile_size//2, 
                                  init_y + (tile_size + gap_size)*row + tile_size//2], 
                                  player_size)
    
def drawNextPlayerSquare(screen, row, col):
    pygame.draw.rect(screen, tileColor, 
                     [init_x + (tile_size + gap_size)*col+1, 
                      init_y + (tile_size + gap_size)*row+1, 
                      tile_size-2, tile_size-2])

    
def drawWall(screen, wall, color):
    col = wall.col
    row = wall.row
    if (wall.direction == "V"):
        pygame.draw.rect(screen, color, 
                         [init_x + tile_size*(col+1) + gap_size*col + 1,
                          init_y + (tile_size + gap_size)*row, 
                          gap_size-2, 2*tile_size+ gap_size])
    elif (wall.direction == "H"):
        pygame.draw.rect(screen, color, 
                         [init_x + (tile_size + gap_size)*col,
                          init_y + tile_size*(row+1) + gap_size*row + 1, 
                          2*tile_size+ gap_size, gap_size-2])
 
def drawPosition(screen, boardPos, mode):
    drawBoard(screen)
    textToDisplay = ""
    if mode == "MOVE":
        drawNextPlayerSquare(screen, 
                             boardPos.position[boardPos.nextPlayer].row, 
                             boardPos.position[boardPos.nextPlayer].col)        
    
    if (boardPos.isWhiteWinner()):
        textToDisplay = "Winner: WHITE"
    elif boardPos.isBlackWinner():
        textToDisplay = "Winner: BLACK"
    elif boardPos.nextPlayer == "W" and mode == "MOVE":
        textToDisplay = "Move for WHITE"
    elif boardPos.nextPlayer == "W" and mode == "WALL":
        textToDisplay = "Wall for WHITE"
    elif boardPos.nextPlayer == "B" and mode == "MOVE":
        textToDisplay = "Move for BLACK"
    elif boardPos.nextPlayer == "B" and mode == "WALL":
        textToDisplay = "Wall for BLACK"   
    else:
        textToDisplay = ""   
    displayText(screen, textToDisplay, display_width - 130, (display_height/2)-10)
    displayText(screen, "Walls (WHITE): " + str(boardPos.numOfWalls['W']),  
                display_width - 130, 40)
    displayText(screen, "Walls (BLACK): " + str(boardPos.numOfWalls['B']),  
                display_width - 130, display_height - 40)    
    drawPlayer(screen, boardPos.position['W'].row, boardPos.position['W'].col, 'W')
    drawPlayer(screen, boardPos.position['B'].row, boardPos.position['B'].col, 'B')
    for wall in boardPos.walls:
        if (wall.isValidPosition()):        
            drawWall(screen, wall, wallColor)
            

screen = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Quoridor')
boardPos = BoardPosition()
drawPosition(screen, boardPos, "MOVE")

clock = pygame.time.Clock()

crashed = False
mode = "MOVE"
newWall = None
colors = {'W': whiteColor, 'B': blackColor}
while not crashed:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True
        elif event.type == pygame.KEYDOWN:
            if mode == "MOVE":
                if event.key == pygame.K_UP:
                    boardPos.movePlayer("UP")
                elif event.key == pygame.K_DOWN:
                    boardPos.movePlayer("DOWN")
                elif event.key == pygame.K_LEFT:
                    boardPos.movePlayer("LEFT")
                elif event.key == pygame.K_RIGHT:
                    boardPos.movePlayer( "RIGHT")
                elif (event.key == pygame.K_w and 
                      boardPos.numOfWalls[boardPos.nextPlayer] >0):
                    mode = "WALL"
                    initPosition = boardPos.position[boardPos.nextPlayer]
                    newWall = WallPosition(initPosition.row, 
                                           initPosition.col, 
                                           "H", 
                                           boardPos.nextPlayer)
            elif mode == "WALL":
                if event.key == pygame.K_UP and newWall.row > 0:
                    newWall.row -=1
                elif event.key == pygame.K_DOWN and newWall.row < 7:
                    newWall.row +=1
                elif event.key == pygame.K_LEFT and newWall.col > 0:
                    newWall.col -=1
                elif event.key == pygame.K_RIGHT and newWall.col < 7:
                    newWall.col +=1
                elif event.key == pygame.K_f:
                    if newWall.direction == 'H':
                        newWall.direction = 'V'
                    else:
                        newWall.direction = 'H'
                    mode = "WALL"
                elif event.key == pygame.K_w:
                    mode = "MOVE"
                    newWall = None
                elif event.key == pygame.K_SPACE:
                    notOverlapping = boardPos.addWall(newWall)
                    if notOverlapping:
                        boardPos.switchPlayer()
                        mode = "MOVE"
                        newWall = None
                    
        # Draw the board position and the pending wall
        drawPosition(screen, boardPos, mode)
        if mode == "WALL":
            drawWall(screen, newWall, colors[boardPos.nextPlayer])

        print(event)

    pygame.display.update()
    clock.tick(60)

pygame.quit()
quit()