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
            dataframe["Octant"] = ' '
            for i in range(len(dataframe)):
                #storing this by calling an octant_identification function which returns as char which it belomgs..
                dataframe.loc[i,"Octant"] = octant_identification(float(dataframe.loc[i,"U' = U -U Avg"]),float(dataframe.loc[i,"V' = V -V Avg"]),float(dataframe.loc[i,"W' = W -W Avg"]))            #adding 4new columns in the dataframe.
            dataframe[' '] = ' '
            #this indicates the +1,-1,+2,-2,...-4
            dataframe['Count'] = ' '
            #this stores the longest subsequence length..
            dataframe['Longest Subsequence Length'] = ' '
            #this stores the no of sequences which has length equal to maxi length
            dataframe['Count '] = ' '
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
            #so we got longest subsequence length in the form dictonary named max_store_dict
            #now i have created new 2 dictonaries..which stores the intial count 0.
            #store_dict1 will store the current sequence length.
            #store_dict2 will store the frequecny of longest subsequence length.
            store_dict1 = {1:0,2:0,3:0,4:0,-1:0,-2:0,-3:0,-4:0}
            store_dict2 = {1:0,2:0,3:0,4:0,-1:0,-2:0,-3:0,-4:0}
            #i have created this 8_arrays, each array stores the ending time of longest subsequence length.
            range_list1 = []
            #the above list stores the ending time '+1' of longest subsequence length.
            range_list2 = []
            #the above list stores the ending time '+2' of longest subsequence length.
            range_list3 = []
            range_list4 = []
            #the above list stores the ending time '+4' of longest subsequence length.
            range_list_minus1 = []
            range_list_minus2 = []
            #the above list stores the ending time '-2' of longest subsequence length.
            range_list_minus3 = []
            range_list_minus4 = []
            #the above list stores the ending time '-4' of longest subsequence length.
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
             #here when present_freq == max_freq then it means this is the end point of longest subseqnce, so i am storing the time at this row in the array.
             #i am stroing it in the respective array accordingly.     
                    if (int(dataframe.loc[i,"Octant"])==1):
                        range_list1.append(float(dataframe.loc[i,"Time"]))
                    elif (int(dataframe.loc[i,"Octant"])==2):
                        range_list2.append(float(dataframe.loc[i,"Time"]))
                    elif (int(dataframe.loc[i,"Octant"])==3):
                        range_list3.append(float(dataframe.loc[i,"Time"]))
                    elif (int(dataframe.loc[i,"Octant"])==4):
                        range_list4.append(float(dataframe.loc[i,"Time"]))
                    elif (int(dataframe.loc[i,"Octant"])==-1):
                        range_list_minus1.append(float(dataframe.loc[i,"Time"]))
                    elif (int(dataframe.loc[i,"Octant"])==-2):
                        range_list_minus2.append(float(dataframe.loc[i,"Time"]))
                    elif (int(dataframe.loc[i,"Octant"])==-3):
                        range_list_minus3.append(float(dataframe.loc[i,"Time"]))
                    elif (int(dataframe.loc[i,"Octant"])==-4):
                        range_list_minus4.append(float(dataframe.loc[i,"Time"]))
            arr = ['+1','-1','+2','-2','+3','-3','+4','-4']
            # now printing the columns of count,longest subsequence length,count...from their dictonaries.
            for i in range(8):
                dataframe.loc[i,'Count'] = arr[i]
                dataframe.loc[i,'Longest Subsequence Length'] = max_store_dict[int(arr[i])]
                dataframe.loc[i,'Count '] = store_dict2[int(arr[i])]

            #here i have created the columns according to output_file.
            dataframe['     '] = ' '
            dataframe['Count  '] = ' '
            dataframe['Longest Subsequence Length '] = ' '
            dataframe['Count      '] = ' '
            #this index maintains the current row in the output file.(where we have to print)
            j = 0
            for i in range(8):
                #here there are total 8divisions like +1,-1,+2,-2,+3,-3,+4,-4.
                flag = 0
                #with help of flag variable i have differentiated that in the first 2rows of ach division i should print from to etc
                #and in the remaining rows need to print from time to to time
                for xxx in range(store_dict2[int(arr[i])]+2):
                    flag+=1
                    if (flag==1):
                        dataframe.loc[j,'Count  '] = arr[i]
                        dataframe.loc[j,'Longest Subsequence Length '] = max_store_dict[int(arr[i])]
                        dataframe.loc[j,'Count      '] = store_dict2[int(arr[i])]
                    elif (flag==2):
                        dataframe.loc[j,'Count  '] = "Time"
                        dataframe.loc[j,'Longest Subsequence Length '] = "From"
                        dataframe.loc[j,'Count      '] = "To"
                    else:
                        #in the Count        column according to 1,-1,2,-2,3,-3,4,-4 i should take the respective array of time.
                        if (i==0):
                            #difference between each particular division is 0.01 so to find start time, we need to subtract the longest squbsqnce length*0.01 from end time.
                            dataframe.loc[j,'Longest Subsequence Length '] = range_list1[flag-3] - (0.01)*(max_store_dict[int(arr[i])]-1)
                            #can store the directly array value as it is end time.
                            dataframe.loc[j,'Count      '] = range_list1[flag-3]
                        elif (i==1):
                            dataframe.loc[j,'Longest Subsequence Length '] = range_list_minus1[flag-3] - (0.01)*(max_store_dict[int(arr[i])]-1)
                            dataframe.loc[j,'Count      '] = range_list_minus1[flag-3]                
                        elif (i==2):
                            dataframe.loc[j,'Longest Subsequence Length '] = range_list2[flag-3] - (0.01)*(max_store_dict[int(arr[i])]-1)
                            dataframe.loc[j,'Count      '] = range_list2[flag-3]
                        elif (i==3):
                            dataframe.loc[j,'Longest Subsequence Length '] = range_list_minus2[flag-3] - (0.01)*(max_store_dict[int(arr[i])]-1)
                            dataframe.loc[j,'Count      '] = range_list_minus2[flag-3]
                        elif (i==4):
                            dataframe.loc[j,'Longest Subsequence Length '] = range_list3[flag-3] - (0.01)*(max_store_dict[int(arr[i])]-1)
                            dataframe.loc[j,'Count      '] = range_list3[flag-3]
                        elif (i==5):
                            dataframe.loc[j,'Longest Subsequence Length '] = range_list_minus3[flag-3] - (0.01)*(max_store_dict[int(arr[i])]-1)
                            dataframe.loc[j,'Count      '] = range_list_minus3[flag-3]
                        elif (i==6):
                            dataframe.loc[j,'Longest Subsequence Length '] = range_list4[flag-3] - (0.01)*(max_store_dict[int(arr[i])]-1)
                            dataframe.loc[j,'Count      '] = range_list4[flag-3]
                        elif (i==7):
                            dataframe.loc[j,'Longest Subsequence Length '] = range_list_minus4[flag-3] - (0.01)*(max_store_dict[int(arr[i])]-1)
                            dataframe.loc[j,'Count      '] = range_list_minus4[flag-3]
                    j+=1  
            #increase j by 1 as we are going to next row...   
                        #finally exporting this into output file by keeping index=False becuase we dont need the index column.
            dataframe.to_excel('output_octant_longest_subsequence_with_range.xlsx',index=False)   
        except:
            print("Input file doesnot exists/Compilation error")
    except:
        print("Install pandas,numpy and import it")


###Code

from platform import python_version
ver = python_version()

if ver == "3.8.10":
    print("Correct Version Installed")
else:
    print("Please install 3.8.10. Instruction are present in the GitHub Repo/Webmail. Url: https://pastebin.com/nvibxmjw")


octant_longest_subsequence_count_with_range()

#This shall be the last lines of the code.
end_time = datetime.now()
print('Duration of Program Execution: {}'.format(end_time - start_time))
