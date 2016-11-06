'''
Author: Lee Cattarin
Date: Nov. 6, 2016
Purpose: This file puts the data in the CSV files into something that is easy to work
with in Processing, which is java-based.
'''

import colorsys
import math
import util

'''
This function written by Alan Zucconi and found at
http://www.alanzucconi.com/2015/09/30/colour-sorting/
It is not my work
'''
def step (r,g,b, repetitions=1):
  lum = math.sqrt( .241 * r + .691 * g + .068 * b )

  h, s, v = colorsys.rgb_to_hsv(r,g,b)

  h2 = int(h * repetitions)
  lum2 = int(lum * repetitions)
  v2 = int(v * repetitions)
  
  if h2 % 2 == 1:
    v2 = repetitions - v2
    lum = repetitions - lum  

  return (h2, lum, v2)

if __name__ == "__main__":
  ## BASIC INFO
  emotions = ["anger", "anticipation", "disgust", "fear", "joy", "sadness", "surprise", "trust"]
  
  ## READ IN CSV FILES
  # I am not reading in the first column (image_title) as it has no meaning
  # outside of the specific context of my folder of image files / that same 
  # folder on github
  anger, angerVal = util.readCSV(emotions[0])
  anticipation, anticipationVal = util.readCSV(emotions[1])
  disgust, disgustVal = util.readCSV(emotions[2])
  fear, fearVal = util.readCSV(emotions[3])
  joy, joyVal = util.readCSV(emotions[4])
  sadness, sadnessVal = util.readCSV(emotions[5])
  surprise, surpriseVal = util.readCSV(emotions[6])
  trust, trustVal = util.readCSV(emotions[7])
  
  total = dict()
  for item in emotions:
    total[item] = []
    
  colors = list(anger.keys())
  for i in range(len(colors)):
    colors[i] = (int(colors[i][0:2], 16), int(colors[i][2:4], 16), int(colors[i][4:], 16) )
    
  for item in colors:
    print(item)
  colors = sorted(colors, key=lambda rgb: step(rgb[0],rgb[1],rgb[2],8))
  
  for i in range(len(colors)):
    colors[i] = "{:0>2}{:0>2}{:0>2}".format(hex(colors[i][0])[2:], hex(colors[i][1])[2:], hex(colors[i][2])[2:])
    
    
    
    
  
  for key in colors:
    total["anger"].append(sum(anger[key])/angerVal * 360)
    
  for key in colors:
    total["anticipation"].append(sum(anticipation[key])/anticipationVal * 360)
    
  for key in colors:
    total["disgust"].append(sum(disgust[key])/disgustVal * 360)
    
  for key in colors:
    total["fear"].append(sum(fear[key])/fearVal * 360)
    
  for key in colors:
    total["joy"].append(sum(joy[key])/joyVal * 360)
    
  for key in colors:
    total["sadness"].append(sum(sadness[key])/sadnessVal * 360)
    
  for key in colors:
    total["surprise"].append(sum(surprise[key])/surpriseVal * 360)
    
  for key in colors:
    total["trust"].append(sum(trust[key])/trustVal * 360) 
    
  for key in total:
    print('float[]', key, '=', total[key])
    
  for item in colors:
    print('#' + item, end=', ')