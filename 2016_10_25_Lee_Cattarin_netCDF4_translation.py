import netCDF4
import datetime

def readFile(filename):
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

if __name__ == "__main__":
  ## BASIC INFO
  emotions = ["anger", "anticipation", "disgust", "fear", "joy", "sadness", "surprise", "trust"]
  
  ## READ IN CSV FILES
  # I am not reading in the first column (image_title) as it has no meaning
  # outside of the specific context of my folder of image files / that same 
  # folder on github
  anger, angerVal = readFile(emotions[0])
  anticipation, anticipationVal = readFile(emotions[1])
  disgust, disgustVal = readFile(emotions[2])
  fear, fearVal = readFile(emotions[3])
  joy, joyVal = readFile(emotions[4])
  sadness, sadnessVal = readFile(emotions[5])
  surprise, surpriseVal = readFile(emotions[6])
  trust, trustVal = readFile(emotions[7])  
  
  # for testing
  '''
  print(angerVars)
  for key in anger.keys():
    print(key, anger[key])
  '''
  
  ## INIT NETCDF FILE AND GROUPS
  # first time, this should be 'w' or write, all other times 'a' or append
  nc = netCDF4.Dataset('2016_10_25_Lee_Cattarin_Emotion_Color.nc', 'w')
  # group creation only needs to happen once
  for emot in emotions:
    nc.createGroup(emot)
  
  ## SET ATTRIBUTES
  nc.description = "Data on the percentage of colors in each hex code color group in an image returned from a google search for an emotion"
  nc.history = "Created: " + str(datetime.datetime.now().time())
  nc.source = "Data generated and encoded into netCDF4 by Lee Cattarin. Data Science course 2016"
  
  nc.sync()
  
  ## ADD DATA TO NETCDF FILE
  # create Dimensions, one each for each emotion
  # these will specify how many values there are for each emotion
  # again, this only needs to be run once
  
  #createDimension(self, name, length)
  nc.createDimension("ang", angerVal)
  nc.createDimension("ant", anticipationVal)
  nc.createDimension("dis", disgustVal)
  nc.createDimension("fea", fearVal)
  nc.createDimension("joo", joyVal)
  nc.createDimension("sad", sadnessVal)
  nc.createDimension("sur", surpriseVal)
  nc.createDimension("tru", trustVal)
  
  nc.sync()
  
  # create Variables, one for each column of data / key in emotion dict
  # run once
  
  #createVariable(self, name, datatype, dimension)

  for key in anger.keys():
    nc.createVariable( '/anger/' + key, 'f4', ("ang") )  
    nc['/anger/' + key][:] = anger[key][:]
  nc.sync()

  for key in anticipation.keys():
    nc.createVariable( '/anticipation/' + key, 'f4', ("ant") )
    nc['/anticipation/' + key][:] = anticipation[key][:]
  nc.sync()
    
  for key in disgust.keys():
    nc.createVariable( '/disgust/' + key, 'f4', ("dis") )
    nc['/disgust/' + key][:] = disgust[key][:]
  nc.sync()  

  for key in fear.keys():
    nc.createVariable( '/fear/' + key, 'f4', ("fea") )
    nc['/fear/' + key][:] = fear[key][:]
  nc.sync()        

  for key in joy.keys():
    nc.createVariable( '/joy/' + key, 'f4', ("joo") )
    nc['/joy/' + key][:] = joy[key][:]
  nc.sync()
      
  for key in sadness.keys():
    nc.createVariable( '/sadness/' + key, 'f4', ("sad") )
    nc['/sadness/' + key][:] = sadness[key][:]
  nc.sync()  

  for key in surprise.keys():
    nc.createVariable( '/surprise/' + key, 'f4', ("sur") )
    nc['/surprise/' + key][:] = surprise[key][:]
  nc.sync()

  for key in trust.keys():
    nc.createVariable( '/trust/' + key, 'f4', ("tru") )
    nc['/trust/' + key][:] = trust[key][:]
  nc.sync()

  ## CLOSE NETCDF FILE
  nc.close()
  