# -*- coding: utf-8 -*-
"""
Created on Tue Mar 12 20:40:26 2019

@author: varbalk@gmail.com
@author: daniel.varro@gmail.com

"""

class WallPosition:
    def __init__(self, row, column, direction, player):
        self.row = row;
        self.col = column;
        self.direction = direction;
        self.player = player;
        
    def isValidPosition(self):
        if self.row >= 0 and self.row <8 and self.col >= 0 and self.col <8:
            return True
        else:
            return False
        
    def isOverlapping(self, otherWall):
        # if the central coordinates are the same, the walls overlap
        if self.col == otherWall.col and self.row == otherWall.row:
            return True
        # horizontal walls overlap if the rows are the same, and columns differ by 1
        elif (self.direction == "H" and otherWall.direction == "H" and 
              self.row == otherWall.row and 
              (self.col == otherWall.col + 1 or 
               self.col == otherWall.col - 1) ): 
            return True
        # vertical walls overlap if the columns are the same, and rows differ by 1
        elif (self.direction == "V" and otherWall.direction == "V" and 
              self.col == otherWall.col and 
              (self.row == otherWall.row + 1 or 
               self.row == otherWall.row - 1) ): 
            return True
        else:
            return False
    
    #def hasWall(self, row, column):
        
