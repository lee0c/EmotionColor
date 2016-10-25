import netCDF4

def readFile(filename):
  temp = dict()
  header = []
  numLines = 0
  for line in open('CSV/6_10_2016_' + filename + '.csv'):
    dat = line.split(',')
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
  # just for the record, I am not reading in the first
  anger, angerVars = readFile(emotions[0])
  anticipation, anticipationVars = readFile(emotions[1])
  disgust, disgustVars = readFile(emotions[2])
  fear, fearVars = readFile(emotions[3])
  joy, joyVars = readFile(emotions[4])
  sadness, sadnessVars = readFile(emotions[5])
  surprise, surpriseVars = readFile(emotions[6])
  trust, trustVars = readFile(emotions[7])    
  
  ## INIT NETCDF FILE AND GROUPS
  # first time, this should be 'w' or write, all other times 'a' or append
  nc = netCDF4.Dataset('25_10_2016_Lee_Cattarin_Emotion_Color.nc', 'a')
  # group creation only needs to happen once
  '''
  for emot in emotions:
    nc.createGroup(emot)
  '''
  
  
   
  
  
  ## CLOSE NETCDF FILE
  nc.close()
  