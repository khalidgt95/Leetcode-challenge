# -*- coding: utf-8 -*-
"""
Created on Sat Apr 18 00:34:02 2020

@author: Khalid
"""

import numpy as np

case1 = [["X",".",".","X"],
         [".","X",".","."],
         [".","X",".","X"]]



case2 = [["X","X","X","X"],
         ["X","X","X","X"],
         ["X",".","X","X"]]


case3 = [["X","X","X","X"],
         [".",".",".","."],
         [".",".","X","X"],
         ["X",".",".","."]]



def countBattleShips(board):
  
  return 0

board = case3

rows, columns = len(case1), len(case1[0])
total_elements = rows * columns

total_battleships = 0

row_set = set()
column_set = set()

index_battleship = dict()


for i in range(rows):
  for j in range(columns):
    
    if board[i][j] == "X":
      
      flag = False
                    # left, top, right, bottom
      orientations  = [0,0,0,0]
      
      ## First check all the neighbors
      if j > 0:
        if board[i][j-1] == "X":
          orientations[0] = 1 
          
      if j < columns-1:
        if board[i][j+1] == "X":
          orientations[2] = 1
          
      if i > 0:
        if board[i-1][j] == "X":
          orientations[1] = 1
          
      if i < rows-1:
        if board[i+1][j] == "X":
          orientations[3] = 1
          
      
      ## This means that there are ships which are not 
      ## neighbors but are present on the board
      
      for k in range(len(orientations)):
        if orientations[k] == 0:
          if k == 0:
            
            for k in range(j):
              if board[i][k] == "X":
                flag = True
                total_battleships += 1
                break
              
          elif k == 1:
            
            for k in range(i):
              if board[k][j] == "X":
                flag = True
                total_battleships += 1
                break
              
          elif k == 2:
            
            for k in range(j+1,columns):
              if board[i][k] == "X":
                flag = True
                total_battleships += 1
                break
              
          elif k == 3:
            
            for k in range(i+1,rows):
              if board[k][j] == "X":
                flag = True
                total_battleships += 1
                break
        
        if flag:
          break
        
print(total_battleships)
      
