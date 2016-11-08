'''
Author: Lee Cattarin
Date: Sep 27, 2016
Purpose: To analyze by color the results of Google Image Searches for emotion terms and record this data in an SQLite table.
'''

import sqlite3
import os.path
from PIL import Image
import math

def create_tables(c, emotion_tables, color_codes):
    ## Since table creation can only be run once, it is in a function so it can be called once and then not called next run
    for i in range(len(emotion_tables)):
        c.execute( "CREATE TABLE {tn} ({nf} {ft} PRIMARY KEY)"\
            .format(tn=emotion_tables[i], nf="image_title", ft="TEXT") )
        for j in range(len(color_codes)):
            c.execute( "ALTER TABLE {tn} ADD COLUMN '{cn}' {ct} DEFAULT '{df}'"\
                      .format(tn=emotion_tables[i], cn=color_codes[j], ct="REAL", df=0) )
            
def closest(rgb, vals, rgb_codes):
    ## Find closest pixel to current one
    ans = []
    for item in rgb:
        for v in range(len(vals)-1):
            if vals[v] == item:
                ans.append(vals[v])
                break
            elif vals[v] < item and item < vals[v+1]:
                if item - vals[v] > vals[v+1] - item:
                    ans.append(vals[v+1])
                else:
                    ans.append(vals[v])
                break
            
            if v == len(vals)-2:
                ans.append(vals[len(vals)-1])
                
    ans = tuple(ans)
    return rgb_codes.index(ans)
            

## NAME OF FILE, NAME OF TABLES, GRAYSCALE NUMS
fname = "4_10_2016_Lee_Cattarin_Emotions.sqlite"
emotion_tables = [ "fear", "anger", "sadness", "joy", "disgust", "trust", "anticipation", "surprise" ]
emotion_tables.sort()

## CREATING COLOR OPTIONS
rgb_codes = []
hex_codes = []
vals = [0, 51, 102, 153, 204, 255]
for r in range(len(vals)):
    for g in range(len(vals)):
        for b in range(len(vals)):
            rgb_codes.append( (vals[r], vals[g], vals[b]) )
            hex_codes.append( "{:0>2}{:0>2}{:0>2}".format(hex(vals[r])[2:],hex(vals[g])[2:],hex(vals[b])[2:]) )

## CONNECT TO SQLITE FILE / OPTIONAL CREATE TABLES
conn = sqlite3.connect(fname)
c = conn.cursor()

## remove this after first successful run
## create_tables(c, emotion_tables, hex_codes)
done = []
for i in range(len(emotion_tables)):
    c.execute("SELECT * FROM {tn}".format(tn=emotion_tables[i]))
    r = c.fetchall()
    for item in r:
        done.append(item[0])

## OPEN FILE & GET COLOR DATA
for i in range(len(emotion_tables)):
    for j in range(1, 101):
        
        ## GET FILE NAME
        row = emotion_tables[i] + "_{:0>3}".format(j)
        if len(done) > 0:
            if row == done[0]:
                done.remove(row)
                continue
        if os.path.isfile("emotions/" + row + ".jpg"):
            fname = "emotions/" + row + ".jpg"
        elif os.path.isfile("emotions/" + row + ".png"):
            fname = "emotions/" + row + ".png"
        else:
            continue
        
        print(fname)
        ## Open image, resize to shorten analysis time
        im = Image.open(fname)
        pix = im.load()
        width,height = im.size
        smaller = min(im.size)
        if smaller > 100:
            scale = 100/smaller
            im.resize( (int(width*scale), int(height*scale)) )
        
        width,height = im.size
        total = width*height
        colors = [0]*len(rgb_codes)
        
        ## Pixel analysis
        for x in range(width):
            for y in range(height):
                rgb = pix[x,y]
                if isinstance(rgb, int):
                    rgb = (rgb, rgb, rgb)
                color = closest((rgb[0], rgb[1], rgb[2]), vals, rgb_codes)
                colors[color] += 1           
        
        ## Form and execute SQLite command
        comm = ""
        
        for k in range(len(colors)):
            colors[k] = colors[k]/total
            comm = comm + "{},".format(colors[k])
        
        comm = comm[:-1]
        print(comm)
        c.execute("INSERT INTO {tn} VALUES ('{key}',{val})"\
                  .format(tn=emotion_tables[i], key=row, val=comm) )
        
        ## COMMIT AFTER EVERY FUCKING LINE DEAR LORD
        conn.commit()

## CLOSE
conn.close()