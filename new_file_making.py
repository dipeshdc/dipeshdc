"""fw = open('dipesh.txt','w+')
fw.write("Who won match?")
fw.writelines("\nthe winner is portugal and \n 6-1 \n intresting match")
fw.close()


fo = open('dipesh.txt','r+')
print(fo.read())
fo.close()
"""


import csv
import os

filename = 'earthquake.csv'

lats,lons = [], []
epicentre,magnitudes = [],[]
timestrings = []

l=[]
#with statement automatically closes the file again when the block end
#next(reader) # Move to next Row, Ignore the header in this case.
'''
    fp=open('','r')
    ......
    ......
    fp.close()
'''

#'c:\python37\test.txt'

#with open(os.path.dirname(os.path.abspath(__file__))+'/'+filename) as f:

with open(filename) as f:  #file handler
    reader = csv.reader(f)
    #print(reader)
    #print(type(reader))
    for row in reader:
        print(row[-2])




