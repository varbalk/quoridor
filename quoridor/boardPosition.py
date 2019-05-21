# -*- coding: utf-8 -*-
"""
Created on Tue Mar 12 19:46:53 2019

@author: varbalk@gmail.com
@author: daniel.varrok@gmail.com
"""
from position import Position

class BoardPosition:

    """    
    whitePlayerRow = 0;
    whitePlayerCol = 4;

    blackPlayerRow = 8;
    blackPlayerCol = 4;

    whiteWalls = [];
    blackWalls = [];
    """
    
    def __init__(self):
        self.walls = [];
        self.white = Position(0,4)
        self.black = Position(8,4)
        self.nextPlayer = "W"
    """    
    def printBoard(self):
        for row in range(9):
            for col in range(9):
                if row == self.whitePlayerRow and col == self.whitePlayerCol :
                    print("|W", end='')
                elif row == self.blackPlayerRow and col == self.blackPlayerCol : 
                    print("|B", end='')
                else:
                    print("| ", end='')
            print("|")
    """
        
    def addWall(self, wall):
        if (not wall.isValidPosition()):
            return False
        notOverlapping = True;
        for nextWall in self.walls:
            if wall.isOverlapping(nextWall):
                notOverlapping = False;
        if notOverlapping:
            self.walls.append(wall);
        return notOverlapping

    def isThereWall(self, aRow, aCol, wallDir):
        found = False
        for wall in self.walls:
            if (wallDir == "H" and wall.row == aRow and 
                (wall.col == aCol or wall.col == aCol-1)):
                found = True
                break
            elif (wallDir == "V" and wall.col == aCol and 
                (wall.row == aRow or wall.row == aRow-1)):
                found = True
                break
        return found
        
    def switchPlayer(self, currPlayer):
        if currPlayer == "W":
            return "B"
        elif currPlayer == "B": 
            return "W"

    
    def movePlayer(self, dir):
        # No moves if there is already a winner
        if (self.isWhiteWinner() or self.isBlackWinner()):
            return
        
        player = self.nextPlayer
        playerPos = None
        otherPos = None
        if (player == "W"):
            playerPos = self.white
            otherPos = self.black
        else:
            playerPos = self.black
            otherPos = self.white

        if dir == "UP":
            # Check if white is not at top edge of the board AND
            # Check if there is no wall above
            if (playerPos.row > 0 and 
                not self.isThereWall(playerPos.row-1, playerPos.col, "H")):
                    # Check if other player is jumped
                    if (playerPos.col == otherPos.col
                        and playerPos.row == otherPos.row-1 ):
                        if (playerPos.row > 1):
                            playerPos.row -=2
                            if (not self.isBlackWinner()):
                                self.nextPlayer = self.switchPlayer(player)
                    else:
                        # Regular move otherwise
                        playerPos.row -= 1
                        if (not self.isBlackWinner()):
                            self.nextPlayer = self.switchPlayer(player)
        elif dir == "DOWN":
            # Check if white is not at bottom edge of the board
            # Check if there is no wall below
            if (playerPos.row < 8 and 
                not self.isThereWall(playerPos.row, playerPos.col, "H")):
                # Check if other player is jumped
                if (playerPos.col == otherPos.col
                    and playerPos.row == otherPos.row+1):
                    if (playerPos.row > 1):
                        playerPos.row += 2
                        if (not self.isWhiteWinner()):
                            self.nextPlayer = self.switchPlayer(player)
                else:
                    # Regular move otherwise
                    playerPos.row += 1                
                    if (not self.isWhiteWinner()):
                        self.nextPlayer = self.switchPlayer(player)
        elif dir == "LEFT":
            # Check if white is not at left edge of the board
            # Check if there is no wall on the left
            if (playerPos.col > 0 and 
                not self.isThereWall(playerPos.row, playerPos.col-1, "V")):
                # Check if other player is jumped
                if (playerPos.row == otherPos.row
                    and playerPos.col == otherPos.col+1):
                    if (playerPos.col >1):
                        playerPos.col -= 2
                        self.nextPlayer = self.switchPlayer(player)
                else: 
                    playerPos.col -= 1
                    self.nextPlayer = self.switchPlayer(player)
        elif dir == "RIGHT": 
            # Check if white is not at right edge of the board
            # Check if there is no wall on the right
            if (playerPos.col < 8 and 
                not self.isThereWall(playerPos.row, playerPos.col, "V")):
                # Check if other player is jumped
                if (playerPos.row == otherPos.row 
                    and playerPos.col == otherPos.col-1):
                    if (playerPos.col < 7):
                        playerPos.col += 2 
                        self.nextPlayer = self.switchPlayer(player)
                else:
                    playerPos.col += 1
                    self.nextPlayer = self.switchPlayer(player)

    def isWhiteWinner(self):
        if (self.white.row == 8): 
            return True
        else:
            return False

    def isBlackWinner(self):
        if (self.black.row == 0): 
            return True
        else:
            return False
        
"""                        
                        if (player == "W" and self.white.col == self.black.col
                            and self.white.row == self.black.row-1):
                            self.white.row = self.white.row-2
                            self.nextPlayer = self.switchPlayer(player)                                                            
                        elif (player == "B" and self.white.col == self.black.col
                            and self.white.row-1 == self.black.row):
                            self.black.row = self.black.row-2
                            if (not self.isBlackWinner()):
                                self.nextPlayer = self.switchPlayer(player)
                     
                            if player == "W":
                                self.white.row = self.white.row-1
                                self.nextPlayer = self.switchPlayer(player)
                            elif player == "B":
                                self.black.row = self.black.row-1
                                if (not self.isBlackWinner()):
                                    self.nextPlayer = self.switchPlayer(player)
"""
"""                        
                if (player == "W" and self.white.col == self.black.col
                    and self.white.row == self.black.row+1):
                    self.white.row = self.white.row+2
                    if (not self.isWhiteWinner()):
                        self.nextPlayer = self.switchPlayer(player)
                elif (player == "B" and self.white.col == self.black.col
                    and self.white.row+1 == self.black.row):
                    self.black.row = self.black.row+2
                    self.nextPlayer = self.switchPlayer(player)
                   
                else:
                    # Regular move otherwise
                    if player == "W":
                        self.white.row = self.white.row+1
                        if (not self.isWhiteWinner()):
                            self.nextPlayer = self.switchPlayer(player)
                    elif player == "B":
                        self.black.row = self.black.row+1
                        self.nextPlayer = self.switchPlayer(player)
"""                     
"""
                        if (player == "W" and self.white.row == self.black.row
                            and self.white.col == self.black.col+1):
                            self.white.col = self.white.col-2
                        elif (player == "B" and self.white.row == self.black.row
                            and self.white.col+1 == self.black.col):
                            self.black.col = self.black.col-2
                        else:
                            # Regular move otherwise
                            if player == "W":
                                self.white.col = self.white.col-1
                            elif player == "B":
                                self.black.col = self.black.col-1
                        self.nextPlayer = self.switchPlayer(player)
"""    
"""
                if (player == "W" and self.white.row == self.black.row
                    and self.white.col == self.black.col-1):
                    self.white.col = self.white.col+2
                elif (player == "B" and self.white.row == self.black.row
                    and self.white.col-1 == self.black.col):
                    self.black.col = self.black.col+2
                else:
                    # Regular move otherwise
                    if player == "W":
                        self.white.col = self.white.col+1
                    elif player == "B":
                        self.black.col = self.black.col+1
"""