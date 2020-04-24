# -*- coding: utf-8 -*-
"""
Created on Sun Apr 19 19:17:06 2020

@author: Khalid
"""

rating = [2,5,3,4,1]

teams_count = 0

for i in range(len(rating)):
  
  first_element = rating[i]

  team_ascend = list()
  team_descend = list()
    
  for j in range(i+1, len(rating)):

    value = rating[j]

    if value < first_element:
      
      team_descend.append([first_element, value])            
      
      # app



    if value > first_element:
    
      if value < team_ascend[-1]:
        team_ascend[1] = value
      else:
        team_ascend.append(value)
    
    else:
      
      if len(team_descend) == 1:
        team_descend.append([value])
        continue
      
      if value > 
      
      team_descend.append(value)
    
    
    if value < team_descend[-1]:
      if len(team_descend) > 1:
        team_descend[1] = value
      else:
        team_descend.append(value)
    
    
    
    if value > team_ascend[-1]:
      if len(team_ascend) > 1:
        team_ascend[1] = value
      else:
        team_ascend.append(value)
      
  
    print(team_ascend, team_descend, value)
    
  print("\n")
  
  if len(team_ascend) >= 3 or len(team_descend) >= 3:
    teams_count += 1
    
  
print(teams_count)
  