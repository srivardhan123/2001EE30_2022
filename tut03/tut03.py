try:
    import pandas as pd
    import numpy as np
    try:
        #now i am reading the excel file using the pandas.
        dataframe = pd.read_excel('input_octant_transition_identify.xlsx')
        #i have stored the total no of +1,-1,2,-2,3,-3,..are present in the those variables.
        x1 = 0
        x2 = 0
        x3 = 0
        x4 = 0
        y1 = 0
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

        #adding 4new columns in the dataframe.
        dataframe[' '] = ' '
        #this indicates the +1,-1,+2,-2,...-4
        dataframe['count'] = ' '
        #this stores the longest subsequence length..
        dataframe['Longest Subsequence Length'] = ' '
        #this stores the no of sequences which has length equal to maxi length
        dataframe['Count'] = ' '

        #creating the two dictonaries one stores the max length of continous subsequence the other stores the present sequence length,,
        store_dict = {1:0,2:0,3:0,4:0,-1:0,-2:0,-3:0,-4:0}
        max_store_dict = {1:0,2:0,3:0,4:0,-1:0,-2:0,-3:0,-4:0}
        for i in range(len(dataframe)):
            store_dict[int(dataframe.loc[i,"Octant"])]+=1
            #when i found any octant number then i increase the count of that octant number.
            #and remaining octant number count i will make it to zero.!
            if (int(dataframe.loc[i,"Octant"])!=1):
                store_dict[1]=0
            if (int(dataframe.loc[i,"Octant"])!=2):
                store_dict[2]=0
            if (int(dataframe.loc[i,"Octant"])!=3):
                store_dict[3]=0
            if (int(dataframe.loc[i,"Octant"])!=4):
                store_dict[4]=0
            if (int(dataframe.loc[i,"Octant"])!=-1):
                store_dict[-1]=0
            if (int(dataframe.loc[i,"Octant"])!=-2):
                store_dict[-2]=0
            if (int(dataframe.loc[i,"Octant"])!=-3):
                store_dict[-3]=0
            if (int(dataframe.loc[i,"Octant"])!=-4):
                store_dict[-4]=0
            #here i am storing the count if it is greater than previous_max_coun...
            max_store_dict[int(dataframe.loc[i,"Octant"])] = max(max_store_dict[int(dataframe.loc[i,"Octant"])],store_dict[int(dataframe.loc[i,"Octant"])])

        #so we got longest subsequence length in the form dictonary named max_store_dict.

        #now i have created new 2 dictonaries..which stores the intial count 0.
        #store_dict1 will store the current sequence length.
        #store_dict2 will store the frequecny of longest subsequence length.
        store_dict1 = {1:0,2:0,3:0,4:0,-1:0,-2:0,-3:0,-4:0}
        store_dict2 = {1:0,2:0,3:0,4:0,-1:0,-2:0,-3:0,-4:0}
        for i in range(len(dataframe)):
            #same logic like above.
            store_dict1[int(dataframe.loc[i,"Octant"])]+=1
            if (int(dataframe.loc[i,"Octant"])!=1):
                store_dict1[1]=0
            if (int(dataframe.loc[i,"Octant"])!=2):
                store_dict1[2]=0
            if (int(dataframe.loc[i,"Octant"])!=3):
                store_dict1[3]=0
            if (int(dataframe.loc[i,"Octant"])!=4):
                store_dict1[4]=0
            if (int(dataframe.loc[i,"Octant"])!=-1):
                store_dict1[-1]=0
            if (int(dataframe.loc[i,"Octant"])!=-2):
                store_dict1[-2]=0
            if (int(dataframe.loc[i,"Octant"])!=-3):
                store_dict1[-3]=0
            if (int(dataframe.loc[i,"Octant"])!=-4):
                store_dict1[-4]=0
            #if present freq is equal to max freq then increase it by 1.
            if(store_dict1[int(dataframe.loc[i,"Octant"])]==max_store_dict[int(dataframe.loc[i,"Octant"])]):
                store_dict2[int(dataframe.loc[i,"Octant"])]+=1

        arr = ['+1','-1','+2','-2','+3','-3','+4','-4']

        # now printing the columns of count,longest subsequence length,count...from their dictonaries.
        for i in range(8):
            dataframe.loc[i,'count'] = arr[i]
            dataframe.loc[i,'Longest Subsequence Length'] = max_store_dict[int(arr[i])]
            dataframe.loc[i,'Count'] = store_dict2[int(arr[i])]

        #finally exporting this into output file by keeping index=False becuase we dont need the index column.
        dataframe.to_excel('output_octant_longest_subsequence.xlsx',index=False)
    except:
        print("input file doesnot exists/compilation error")
except:
    print("install pandas,numpy and import it")
