try:    
     import pandas as pd
     import numpy as np
except:
     print("install and import pandas and numpy.")

#eading the excel file using the pandas.
try:
    dataframe = pd.read_excel('input_octant_transition_identify.xlsx')
    #i have stored the total no of +1,-1,2,-2,3,-3,..are present in the those variables.
    x2 = 0  
    x3 = 0
    x4 = 0
    y1 = 0
    x1 = 0
    y2 = 0
    y3 = 0
    y4 = 0

    #created this function to identify in which octant it belongs..
    def octant_identification(val,val1,val2):
        #using if and else conditons with 8conditions i have divided the octants value.
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
        #adding the columns accoridng it my use and intially keeping it empty.
    dataframe['U Avg'] = ' '
    dataframe['V Avg'] = ' '
    dataframe['W Avg'] = ' '

    #using pandas library mean function i have caluclated mean of U,V,W and assigned it in the column of U avg,V avg,W avg. 
    #inserting the averge values at first row using loc function.
    dataframe.loc[0,'U Avg'] = dataframe['U'].mean()
    dataframe.loc[0,'V Avg'] = dataframe['V'].mean()
    dataframe.loc[0,'W Avg'] = dataframe['W'].mean()
    #here creating some more columns which are given in the output..
    dataframe["U' = U -U Avg"] = ' '
    dataframe["V' = V -V Avg"] = ' '
    dataframe["W' = W -W Avg"] = ' '

    for i in dataframe.index:
        #here subtracting tow columns and storing it into the diff column by using iloc function!.
        #float function converts the data type.
        dataframe.loc[i,"U' = U -U Avg"] = float(dataframe.loc[i,'U']) - float(dataframe.loc[0,'U Avg'])
        dataframe.loc[i,"V' = V -V Avg"] = float(dataframe.loc[i,'V']) - float(dataframe.loc[0,'V Avg'])
        dataframe.loc[i,"W' = W -W Avg"] = float(dataframe.loc[i,'W']) - float(dataframe.loc[0,'W Avg'])

    #addming one more column to store the value of octants in each row.
    dataframe["Octant"] = ' '
    for i in range(len(dataframe)):
        #storing this by calling an octant_identification function which returns as char which it belomgs..
        dataframe.loc[i,"Octant"] = octant_identification(float(dataframe.loc[i,"U' = U -U Avg"]),float(dataframe.loc[i,"V' = V -V Avg"]),float(dataframe.loc[i,"W' = W -W Avg"]))

    #taking an input from the user manually..
