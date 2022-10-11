from datetime import datetime
start_time = datetime.now()
#I have stored the total no of +1,-1,2,-2,3,-3,..are present in the those global variables.
x1 = 0
x2 = 0
x3 = 0
x4 = 0
y1 = 0
y2 = 0
y3 = 0
y4 = 0
#Help https://youtu.be/H37f_x4wAC0
def octant_longest_subsequence_count_with_range():
    try:
        import pandas as pd
        import numpy as np
        try:
        #now i am reading the excel file using the pandas.
            dataframe = pd.read_excel('input_octant_longest_subsequence_with_range.xlsx')
            #created this function to identify in which octant it belongs..
            def octant_identification(val,val1,val2):
                #using if and else conditons with 8conditions i have divided the octants value.
                global x1,x2,x3,x4,y1,y2,y3,y4
                if (val>0 and val1>0 and val2>0):
                    #increasing each timee the value of x1 globally..similarly x2,x3,y1,y2...etc
                    x1+=1
                    return "+1"
                elif (val<0 and val1>0 and val2>0):
                    # global x2
                    x2+=1
                    return "+2"
                elif (val<0 and val1<0 and val2>0):
                    # global x3
                    x3+=1
                    return "+3"
                elif (val>0 and val1<0 and val2>0):
                    # global x4
                    x4+=1
                    return "+4"
                elif (val>0 and val1>0 and val2<0):
                    # global y1
                    y1+=1
                    return "-1"
                elif (val<0 and val1>0 and val2<0):
                    # global y2
                    y2+=1
                    return "-2"
                elif (val<0 and val1<0 and val2<0):
                    # global y3
                    y3+=1
                    return "-3"
                elif (val>0 and val1<0 and val2<0):
                    # global y4
                    y4+=1
                    return "-4"
            #adding the columns accoridng it my use and intially keeping it empty.
