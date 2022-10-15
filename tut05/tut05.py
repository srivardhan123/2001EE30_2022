from datetime import datetime
start_time = datetime.now()

#i have stored the total no of +1,-1,2,-2,3,-3,..are present in the these global variables.
x1 = 0
x2 = 0  
x3 = 0
x4 = 0
y1 = 0
y2 = 0
y3 = 0
y4 = 0
#Help https://youtu.be/N6PBd4XdnEw
def octant_range_names(mod):
    octant_name_id_mapping = {"1":"Internal outward interaction", "-1":"External outward interaction", "2":"External Ejection", "-2":"Internal Ejection", "3":"External inward interaction", "-3":"Internal inward interaction", "4":"Internal sweep", "-4":"External sweep"}
    import pandas as pd
    import numpy as np
    #reading the excel file using the pandas.
    dataframe = pd.read_excel('octant_input.xlsx')
    #created this function to identify in which octant it belongs..
    def octant_identification(val,val1,val2):
        #using if and else conditons with 8 if and else conditions, i have divided the octants value.
        if (val>0 and val1>0 and val2>0):
            global x1
            #increasing each timee the value of x1 globally..similarly x2,x3,y1,y2...etc
            x1+=1
            return "+1"
        elif (val<0 and val1>0 and val2>0):
            global x2
            x2+=1
            return "+2"
        elif (val<0 and val1<0 and val2>0):
            global x3
            x3+=1
            return "+3"
        elif (val>0 and val1<0 and val2>0):
            global x4
            x4+=1
            return "+4"
        elif (val>0 and val1>0 and val2<0):
            global y1
            y1+=1
            return "-1"
        elif (val<0 and val1>0 and val2<0):
            global y2
            y2+=1
            return "-2"
        elif (val<0 and val1<0 and val2<0):
            global y3
            y3+=1
            return "-3"
        elif (val>0 and val1<0 and val2<0):
            global y4
            y4+=1
            return "-4"
