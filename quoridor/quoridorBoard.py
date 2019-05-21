# -*- coding: utf-8 -*-
"""
Created on Mon Mar 25 19:30:17 2019

@author: varba
"""

import pygame
from wallPosition import WallPosition
from boardPosition import BoardPosition

pygame.init()

bgColor = (212, 212, 212)
blackColor = (0, 0, 0)
whiteColor = (255, 255, 255)
wallColor = (77, 38, 0)
lineColor = (0, 0, 0)
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

def displayText(screen, text):
    largeText = pygame.font.Font('freesansbold.ttf',18)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = (display_width - 130,(display_height/2)-10)
    screen.blit(TextSurf, TextRect)
    
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
                              tile_size, tile_size], 2)
    
def drawPlayer(screen, row, col, color):
    if (color == "BLACK"):
        pygame.draw.circle(screen, blackColor, 
                                 [init_x + (tile_size + gap_size)*col + tile_size//2, 
                                  init_y + (tile_size + gap_size)*row + tile_size//2], 
                                  player_size)
    elif (color == "WHITE"):
        pygame.draw.circle(screen, whiteColor, 
                                 [init_x + (tile_size + gap_size)*col + tile_size//2, 
                                  init_y + (tile_size + gap_size)*row + tile_size//2], 
                                  player_size)
    
def drawNextPlayerSquare(screen, row, col):
    pygame.draw.rect(screen, tileColor, 
                     [init_x + (tile_size + gap_size)*col+2, 
                      init_y + (tile_size + gap_size)*row+2, 
                      tile_size-3, tile_size-3])

    
def drawWall(screen, wall):
    col = wall.column
    row = wall.row
    if (wall.direction == "V"):
        pygame.draw.rect(screen, wallColor, 
                         [init_x + tile_size*(col+1) + gap_size*col + 1,
                          init_y + (tile_size + gap_size)*row, 
                          gap_size-1, 2*tile_size+ gap_size])
    elif (wall.direction == "H"):
        pygame.draw.rect(screen, wallColor, 
                         [init_x + (tile_size + gap_size)*col,
                          init_y + tile_size*(row+1) + gap_size*row + 1, 
                          2*tile_size+ gap_size, gap_size-1])
 
def drawPosition(screen, boardPos):
    drawBoard(screen)
    if (boardPos.nextPlayer == "W"):
        drawNextPlayerSquare(screen, boardPos.white.row, boardPos.white.col)
        if (boardPos.isWhiteWinner()):
            displayText(screen, "Winner: WHITE")
        else:
            displayText(screen, "Next player: WHITE")        
    elif (boardPos.nextPlayer =="B"):
        drawNextPlayerSquare(screen, boardPos.black.row, boardPos.black.col)
        if (boardPos.isBlackWinner()):
            displayText(screen, "Winner: BLACK")
        else: 
            displayText(screen, "Next player: BLACK")
    drawPlayer(screen, boardPos.white.row, boardPos.white.col, "WHITE")
    drawPlayer(screen, boardPos.black.row, boardPos.black.col, "BLACK")
    for wall in boardPos.walls:
        if (wall.isValidPosition()):        
            drawWall(screen, wall)

    

screen = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Quoridor')
boardPos = BoardPosition()
#wall1 = WallPosition(2, 3, "V", "WHITE")
#boardPos.addWall(wall1)
#wall2 = WallPosition(3, 4, "H", "BLACK")
#boardPos.addWall(wall2)
drawPosition(screen, boardPos)

clock = pygame.time.Clock()

crashed = False
while not crashed:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                boardPos.movePlayer("UP")
            elif event.key == pygame.K_DOWN:
                boardPos.movePlayer("DOWN")
            elif event.key == pygame.K_LEFT:
                boardPos.movePlayer("LEFT")
            elif event.key == pygame.K_RIGHT:
                boardPos.movePlayer( "RIGHT")
            drawPosition(screen, boardPos)

        print(event)

    pygame.display.update()
    #clock.tick(60)
    clock.tick(60)

pygame.quit()
quit()