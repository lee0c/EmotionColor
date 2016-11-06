'''
Author: Lee Cattarin
Date: Nov 6, 2016
Purpose: Utility file for the EmotionColor project
'''

# This function will read and parse one CSV file
# returns a dictionary with data and the number of lines of data in the file
# the dictionary keys are hex codes and values are lists of the percent data 
# for those hex codes from different images
def readCSV(filename):
  temp = dict()
  header = []
  numLines = 0
  for line in open('CSV/2016_10_06_' + filename + '.csv'):
    dat = line.strip().split(',')
    # header line
    if dat[0][0] == 'i':
      for i in range(1, len(dat)):
        temp[dat[i]] = []
        header.append(dat[i])
    # all other lines
    else:
      numLines += 1
      for i in range(1, len(dat)):
        val = float(dat[i])
        temp[header[i-1]].append(val)
    
  return temp, numLines