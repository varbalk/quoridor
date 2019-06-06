# -*- coding: utf-8 -*-
"""
Created on Tue Mar 12 19:46:53 2019

@author: varbalk@gmail.com
@author: daniel.varro@gmail.com
"""
from position import Position

class BoardPosition:

   
    def __init__(self):
        self.walls = [];
        self.position = {'W': Position(0,4), 'B' : Position(8,4) }
        self.nextPlayer = 'W'
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
        
    def switchPlayer(self):
        if self.nextPlayer == "W":
            self.nextPlayer = "B"
        elif self.nextPlayer == "B": 
            self.nextPlayer = "W"

    
    def movePlayer(self, dir):
        # No moves if there is already a winner
        if (self.isWhiteWinner() or self.isBlackWinner()):
            return False
        
        player = self.nextPlayer
        playerPos = None
        otherPos = None
        moveSuccess = False
        if (player == 'W'):
            playerPos = self.position['W']
            otherPos = self.position['B']
        else:
            playerPos = self.position['B']
            otherPos = self.position['W']
        
        if dir == "UP":
            # Check if white is not at top edge of the board AND
            # Check if there is no wall above
            if (playerPos.row > 0 and 
                not self.isThereWall(playerPos.row-1, playerPos.col, "H")):
                    # Check if other player is jumped
                    if (playerPos.col == otherPos.col
                        and playerPos.row == otherPos.row+1 ):
                        if (playerPos.row > 1):
                            playerPos.row -=2
                            if (not self.isBlackWinner()):
                                self.switchPlayer()
                                moveSuccess = True
                    else:
                        # Regular move otherwise
                        playerPos.row -= 1
                        if (not self.isBlackWinner()):
                            self.switchPlayer()
                            moveSuccess = True
        elif dir == "DOWN":
            # Check if white is not at bottom edge of the board
            # Check if there is no wall below
            if (playerPos.row < 8 and 
                not self.isThereWall(playerPos.row, playerPos.col, "H")):
                # Check if other player is jumped
                if (playerPos.col == otherPos.col
                    and playerPos.row == otherPos.row-1):
                    if (playerPos.row > 1):
                        playerPos.row += 2
                        if (not self.isWhiteWinner()):
                            self.switchPlayer()
                            moveSuccess = True
                else:
                    # Regular move otherwise
                    playerPos.row += 1                
                    if (not self.isWhiteWinner()):
                        self.switchPlayer()
                        moveSuccess = True
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
                        self.switchPlayer()
                        moveSuccess = True
                else: 
                    playerPos.col -= 1
                    self.switchPlayer()
                    moveSuccess = True
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
                        self.switchPlayer()
                        moveSuccess = True
                else:
                    playerPos.col += 1
                    self.switchPlayer()
                    moveSuccess = True
        return moveSuccess

    def isWhiteWinner(self):
        if (self.position['W'].row == 8): 
            return True
        else:
            return False

    def isBlackWinner(self):
        if (self.position['B'].row == 0): 
            return True
        else:
            return False
        
