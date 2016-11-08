'''
Author: Lee Cattarin
Date: Nov 8, 2016
Purpose: To condense the emotion-color data into a summary dataset, and change hex colors to a rough approximation of color words that match up to the color.
'''

import util

def hex_to_color(r, g, b):
   # take in r, g, b as INTEGER VALUES
   # 255, 204, 153, 102, 51, 0
   
   # return options are black grey white brown red yellow orange green blue purple
   
   # covers black, white, grey
   if r == g and g == b:
      if r == 0:
         return "Black"
      elif r == 255:
         return "White"
      return "Grey"
   
   # brown is a weird case
   if r <= 204 and r - g == 51 and g - b >= 51:
      return "Brown"
   
   # purple and pink (which returns none because there is no pink)
   if r > g and b > g:
      if r - b >= 153:
         return "None"
      elif b - r <= 102:
         return "Purple"
   
   # yellow is very easy
   if (r == g and r > 153) or (r == 255 and g == 204 and b <= 102):
      return "Yellow"   
   
   # Orange
   if r >= 204 and (r - g <= 51 or (r - g <= 153 and g - b <= 102)):
      return "Orange"
   
   # primary colors are easy
   if r - g >= 102 and r - b >= 102:
      return "Red"
   if b - g >= 0 and b - r >= 102:
      return "Blue"    
   if g - r >= 102 and g - b >= 0:
      return "Green"   
   
   
if __name__ == "__main__":
   ## BASIC INFO
   emotions = ["anger", "anticipation", "disgust", "fear", "joy", "sadness", "surprise", "trust"]
   colors = ["Red", "Orange", "Yellow", "Green", "Blue", "Purple", "Brown", "White", "Grey", "Black", "None"]
   
   ## READ IN CSV FILES
   # I am not reading in the first column (image_title) as it has no meaning
   # outside of the specific context of my folder of image files / that same 
   # folder on github
   data = []
   for item in emotions:
      data.append(util.readCSV(item))
   
   final = dict()
   
   for i in range(len(data)):
      ## individual emotion data: dict and count
      temp = dict()
      for hexc in data[i][0].keys():
         ## list of values
         r = int(hexc[0:2], 16)
         g = int(hexc[2:4], 16)
         b = int(hexc[4:], 16)
         color = hex_to_color(r, g, b)
         if color not in temp.keys():
            temp[color] = 0
         for value in data[i][0][hexc]:
            ## single value
            temp[color] += value
      for key in temp.keys():
         ## for each compiled color value, divide by number of entries for this emotion
         temp[key] = temp[key] / data[i][1]
      final[emotions[i]] = temp
      
      
   file = open("CSV/2016_11_08_all_emotions.csv", "w")
   out = "Emotion"
   for item in colors:
      out += "," + item
      
   out = out + "\n"
   file.write(out)
   
   for key in final:
      out = key
      for color in colors:
         out += "," + str(final[key][color])
      out += "\n"
      file.write(out)
      
   file.close()
   