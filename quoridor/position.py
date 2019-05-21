# -*- coding: utf-8 -*-
"""
Created on Sun Mar 31 18:57:20 2019

@author: varba
"""

class Position:
    def __init__(self, row, col):
        self.row = row;
        self.col = col; 

    def isValidPosition(self):
        if self.row >= 0 and self.row <=8 and self.column > 0 and self.column <=8:
            return True
        else:
            return False