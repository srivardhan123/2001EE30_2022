from datetime import datetime
start_time = datetime.now()

#if uh dont install numpy and pandas then it gives error and goes to except.. 
import pandas as pd
import numpy as np
import os
import glob
import openpyxl
from openpyxl import Workbook
from openpyxl.styles import Border,Side
from openpyxl.styles import PatternFill
x3 = 0
x4 = 0
y1 = 0
x1 = 0
y2 = 0
x2 = 0  
y3 = 0
y4 = 0
#above 8 global variables are useful to find the octant number.
present_tranistion_row = 0
#it stores the row number of mod tranisition count.
def octant_analysis(mod):
    # use glob to get all the csv files
    # store the path of input folder in it.
    path = "./input"
    #all the files in that folder is stored in csv_files.
    csv_files = glob.glob(os.path.join(path, "*.xlsx"))
    #keeping all the values 0 intially.
    global x2
    x2 = 0  
    global x3
    x3 = 0
    global x4
    x4 = 0
    global y1
    y1 = 0
    global x1
    x1 = 0
    global y2
    y2 = 0
    global y3
    y3 = 0
    global y4
    y4 = 0
    # print(csv_files)

    def octant_identification(val,val1,val2):
        #using if and else conditons with 8conditions i have divided the octants value.
        if (val>=0 and val1>=0 and val2>=0):
            global x1
            #increasing each timee the value of x1 globally..similarly x2,x3,y1,y2...etc
            x1+=1
            return "+1"
        elif (val<0 and val1>=0 and val2>=0):
            global x2
            x2+=1
            return "+2"
        elif (val<0 and val1<0 and val2>=0):
            global x3
            x3+=1
            return "+3"
        elif (val>=0 and val1<0 and val2>=0):
            global x4
            x4+=1
            return "+4"
        elif (val>=0 and val1>=0 and val2<0):
            global y1
            y1+=1
            return "-1"
        elif (val<0 and val1>=0 and val2<0):
            global y2
            y2+=1
            return "-2"
        elif (val<0 and val1<0 and val2<0):
            global y3
            y3+=1
            return "-3"
        elif (val>=0 and val1<0 and val2<0):
            global y4
            y4+=1
            return "-4"
        else:
            print('1')
