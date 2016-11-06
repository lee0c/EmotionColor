##Color Analysis in Emotion Images

An analysis of the colors present in Google Image search results for common emotions.

The emotions analyzed were Robert Plutchik's 8 Primary Emotions. 
Images were gathered via a program called [Bulk Image Downloader](http://bulkimagedownloader.com/).
There were 216 colors used as the color categories, decided as every possible combination of the hex values [00, 33, 66, 99, CC, FF] in an RGB 3-tuple.

---

Included resources:

* Python code to generate data from images and store it in an SQLite file
* CSV data dumps of said SQLite file
* Images from which data was gathered
* Utility file (Python) that reads in CSV files
* Python code to translate CSV files into netCDF
* Python code to make data easily usable in Processing, including basic parsing and color sorting
* Processing sketchbook with Processing file and visualization image

---

References:

* Processing PieChart method from https://processing.org/examples/piechart.html
* Python function to sort colors smoothly from http://www.alanzucconi.com/2015/09/30/colour-sorting/