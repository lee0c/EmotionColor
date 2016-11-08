if __name__ == "__main__":
   filename = "CSV/2016_11_08_Joe_Hallock_Colors.csv"
   
   colors = ["Red", "Orange", "Yellow", "Green", "Blue", "Purple", "Brown", "White", "Grey", "Black", "None"]
   
   ## READ IN DATA
   
   data = dict()
   columns = []
   header = True
   
   for line in open(filename):
      current = line.split(",")
      if header:
         ## get header / column title data
         header = False
         for item in current:
            if not item == "":
               columns.append(item.strip())
               data[item.strip()] = []
        
      else:
         if current[0].isdigit() or current[0] == "":
            ## extra lines at the top
            continue
         
         for i in range(len(current)):
            if i < len(columns):
               data[columns[i]].append(current[i].strip())
            
   ## REMOVE EXTRANEOUS DATA   
             
   data.pop("", None)
   data.pop("Age", None)
   data.pop("Gender", None)
   data.pop("Location", None)
   
   columns.remove("")
   columns.remove("Age")
   columns.remove("Gender")
   columns.remove("Location")   
   
   ## PARSE DATA
   
   final = dict()
   for item in columns:
      ## iterate through qualities
      final[item] = dict()
      
      for color in colors:
         ## go through colors to establish base values
         final[item][color] = 0
         
      for color in data[item]:
         ## going through the colors in the data list
         final[item][color] += 1
      
      ## divides counts by total
      responses = float(len(data[item]))
      for color in final[item].keys():
         final[item][color] = final[item][color] / responses
         
   ## WRITE DATA TO NEW FILE
   
   file = open("CSV/2016_11_08_Joe_Hallock_CompactColors.csv", "w")
   out = "Quality"
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