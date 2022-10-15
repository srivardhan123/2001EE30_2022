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
   #creating more columns according to the output file.
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
    #total no of rows present in the dataset.
    total_rows = len(dataframe)
    rows = total_rows//mod
    if (total_rows%mod!=0):
        rows+=1
    #rows vairiables stores total no of divisions made according to input/mod value.
    #this "list1" stores the overall count of 1's 2's..-1's..-4's in the dataset with divisons included in it.
    #in the first row of the list it contains 0-mod-1 divisosion values, in the 2nd row it contains mod-2*mod-1 values..
    list1 = [[0 for i in range(0,9)] for j in range(rows)]
    #ranges array stores the range like 0-4999,5000-9999....etc
    ranges = []
    ranges.append('0.0000 - ' + str(mod-1))
    for i in range(1,rows):
        #appending it into ranges with help forloop and converting the int value into string using str func.
        ranges.append(str(mod*i) + '-' + str(min(mod*(i+1)-1,total_rows-1)))
    check = 0
    for row in range(len(dataframe)):
        check+=1
        #in this way by dividing it with mod .....it goes to the respective rows.
        if(check%mod!=0):
            #in the list1 -4,-3,-2,-1,1,2,3,4 belongs to column 0,1,2,3,5,6,7,8.
            #so gradually increasing the count of list1...whenever i found the respective octant number.
            list1[(check//mod)][int(dataframe.loc[row,'Octant'])+4] = list1[(check//mod)][int(dataframe.loc[row,'Octant'])+4] + 1
        else:
            list1[(check//mod)-1][int(dataframe.loc[row,'Octant'])+4] = list1[(check//mod)-1][int(dataframe.loc[row,'Octant'])+4] + 1
    #creating one more column called octant id..
    dataframe["Octant Id"] = ' '
    #at 1st row we are storing the user input data...
    dataframe.loc[1,'Octant Id'] = "user input"
    #creating one more empty column with no column heading.
    dataframe[' '] = ' '
    dataframe.loc[0,' '] = 'Overall Count'
    dataframe.loc[1,' '] = 'Mod '+ str(mod)
    #adding the empty columns +1,-1.... in the dataset .
    dataframe['+1'] = ' '
    dataframe['-1'] = ' '
    dataframe['+2'] = ' '
    dataframe['-2'] = ' '
    dataframe['+3'] = ' '
    dataframe['-3'] = ' '
    dataframe['+4'] = ' '
    dataframe['-4'] = ' '
    #here storing the overall count of 1's,2's..-4's in the dataframe at respective indexes.
    dataframe.loc[0,'+1'] = x1
    dataframe.loc[0,'+2'] = x2
    dataframe.loc[0,'+3'] = x3
    dataframe.loc[0,'+4'] = x4
    dataframe.loc[0,'-1'] = y1
    dataframe.loc[0,'-2'] = y2
    dataframe.loc[0,'-3'] = y3
    dataframe.loc[0,'-4'] = y4
    ### present_rows (THIS VARIABLE STORE THE VALUE OF ROW AT PRESENT WE ARE GOING TO WRITE IN THE DATAFRAME(EXCEL))
    present_rows = 0
    #here now adding the no of 1's,2's....-4's in the respective ranges from list into the dataframe..
    for i in range(len(dataframe)):
        if (i>=2 and i<(2+len(ranges))):
            dataframe.loc[i,' '] = ranges[i-2]
            #as previously said +1 means 5 column ...
            dataframe.loc[i,'+1'] = list1[i-2][5]
            dataframe.loc[i,'-1'] = list1[i-2][3]
            dataframe.loc[i,'+3'] = list1[i-2][7]
            dataframe.loc[i,'-2'] = list1[i-2][2]
            dataframe.loc[i,'-3'] = list1[i-2][1]
            dataframe.loc[i,'+2'] = list1[i-2][6]
            dataframe.loc[i,'+4'] = list1[i-2][8]
            dataframe.loc[i,'-4'] = list1[i-2][0]    
        elif (i==(2+len(ranges))):
            #storing the value of i before breaking because the next transistions stores after this row value.
            present_rows = i
            break
    #now adding the rank columns according to output file.
    dataframe['Rank 1'] = ' '
    dataframe['Rank 2'] = ' '
    dataframe['Rank 3'] = ' '
    dataframe['Rank 4'] = ' '
    dataframe['Rank 5'] = ' '
    dataframe['Rank 6'] = ' '
    dataframe['Rank 7'] = ' '
    dataframe['Rank 8'] = ' '
    #as overall counts of each octant is independent of input value,by manually we can fill the rank of each octant.
    dataframe.loc[0,'Rank 1'] = 8
    dataframe.loc[0,'Rank 2'] = 3
    dataframe.loc[0,'Rank 3'] = 1
    dataframe.loc[0,'Rank 4'] = 5
    dataframe.loc[0,'Rank 5'] = 4
    dataframe.loc[0,'Rank 6'] = 6
    dataframe.loc[0,'Rank 7'] = 7
    dataframe.loc[0,'Rank 8'] = 2
    #adding more column according to output file.
    dataframe['Rank1 Octant ID'] = ' '
    dataframe['Rank1 Octant Name'] = ' '
    #here also for overall count i have added manually.
    dataframe.loc[0,'Rank1 Octant ID'] = 2
    dataframe.loc[0,'Rank1 Octant Name'] = "External Ejection"
    #create this dict to respctive octant id to respctve octant name.
    octant_name_dict = {1:"Internal outward interaction",-1:"External outward interaction",2:"External Ejection",-2:"Internal Ejection",3:"External inward interaction",-3:"Internal inward interaction",4:"Internal sweep",-4:"External sweep"}
    #here i am storing the count of each octant in the rank1 octant id using the dictonary with intial count = 0
    storing_rank1_modvalues = {1:0,-1:0,2:0,-2:0,3:0,-3:0,4:0,-4:0}
    for i in range(rows):
        #each iteration indicates each particular division of total_rows.
        list2 = []
        #in the list2 i am appending pair of integers..(count of octant id for that particular division,octant id).
        list2.append((list1[i][0],-4))
        list2.append((list1[i][1],-3))
        list2.append((list1[i][2],-2))
        list2.append((list1[i][3],-1))
        list2.append((list1[i][5],1))
        list2.append((list1[i][6],2))
        list2.append((list1[i][7],3))
        list2.append((list1[i][8],4))
        #here i am sorting the list2 , according to ascending order for count of  octant id.
        list2.sort()
        #in the temo_dict i am storing the rank of each octant in the integer form.
        temp_dict = {-1:0,-2:0,-3:0,-4:0,1:0,2:0,3:0,4:0}
        flag = 8
        #store_least_octant variable  will store the rank1 octant id.
        store_least_octant = 0
        #created the temps varaible to identify that right now we are rank1 octant id.
        temps = 0
        #iterating the list2 with pair of integers where a = count of octant id in this mod division, b = octant id
        for a,b in list2:
            temps+=1
            if (temps==8):
                store_least_octant = b
            temp_dict[b] = flag
            flag-=1
        #now writing the values in their respetive column and row using loc func,
        dataframe.loc[i+2,'Rank 1'] = temp_dict[1]
        dataframe.loc[i+2,'Rank 2'] = temp_dict[-1]
        dataframe.loc[i+2,'Rank 3'] = temp_dict[2]
        dataframe.loc[i+2,'Rank 4'] = temp_dict[-2]
        dataframe.loc[i+2,'Rank 5'] = temp_dict[3]
        dataframe.loc[i+2,'Rank 6'] = temp_dict[-3]
        dataframe.loc[i+2,'Rank 7'] = temp_dict[4]
        dataframe.loc[i+2,'Rank 8'] = temp_dict[-4]
        #as store_least_octant contains the rank1 so below step is done.
        dataframe.loc[i+2,'Rank1 Octant ID'] = store_least_octant
        #here maintaining the frequency of rank1 octant id using the dictonary
        storing_rank1_modvalues[store_least_octant]+=1
        #inserting the rank1 octant name.
        dataframe.loc[i+2,'Rank1 Octant Name'] = octant_name_dict[store_least_octant]

    #now started printing the frequency of rank1 octant id manually.
    #present_row indicates the row position where i should start my octant id,octant name ,count of rank1 modules row.
    present_row = 5 + rows
    #printing in the excel sheet according to the octput file.
    dataframe.loc[present_row,'+1'] = "Octant ID"
    dataframe.loc[present_row+1,'+1'] = "1"
    dataframe.loc[present_row+2,'+1'] = "-1"
    dataframe.loc[present_row+3,'+1'] = "2"
    dataframe.loc[present_row+4,'+1'] = "-2"
    dataframe.loc[present_row+5,'+1'] = "3"
    dataframe.loc[present_row+6,'+1'] = "-3"
    dataframe.loc[present_row+7,'+1'] = "4"
    dataframe.loc[present_row+8,'+1'] = "-4"
    dataframe.loc[present_row,'-1'] = "Octant Name"
    dataframe.loc[present_row+1,'-1'] = "Internal outward interaction"
    dataframe.loc[present_row+2,'-1'] = "External outward interaction"
    dataframe.loc[present_row+3,'-1'] = "External Ejection"
    dataframe.loc[present_row+4,'-1'] = "Internal Ejection"
    dataframe.loc[present_row+5,'-1'] = "External inward interaction"
    dataframe.loc[present_row+6,'-1'] = "Internal inward interaction"
    dataframe.loc[present_row+7,'-1'] = "Internal sweep"
    dataframe.loc[present_row+8,'-1'] = "External sweep"
    dataframe.loc[present_row,'+2'] = "Count of Rank 1 Mod values"
    #as i have stored each frequency of each rank1 octant id in the storing_rank1_modvalues dict.. 
    dataframe.loc[present_row+1,'+2'] = storing_rank1_modvalues[1]
    dataframe.loc[present_row+2,'+2'] = storing_rank1_modvalues[-1]
    dataframe.loc[present_row+3,'+2'] = storing_rank1_modvalues[2]
    dataframe.loc[present_row+4,'+2'] = storing_rank1_modvalues[-2]
    dataframe.loc[present_row+5,'+2'] = storing_rank1_modvalues[3]
    dataframe.loc[present_row+6,'+2'] = storing_rank1_modvalues[-3]
    dataframe.loc[present_row+7,'+2'] = storing_rank1_modvalues[4]
    dataframe.loc[present_row+8,'+2'] = storing_rank1_modvalues[-4]
    #now converting whole dataframe into excel format.
    dataframe.to_excel('octant_output_ranking_excel.xlsx',index=False)

    from platform import python_version
    ver = python_version()

    if ver == "3.8.10":
        print("Correct Version Installed")
    else:
        print("Please install 3.8.10. Instruction are present in the GitHub Repo/Webmail. Url: https://pastebin.com/nvibxmjw")

mod=5000 
octant_range_names(mod)
    #This shall be the last lines of the code.
end_time = datetime.now()
print('Duration of Program Execution: {}'.format(end_time - start_time))















