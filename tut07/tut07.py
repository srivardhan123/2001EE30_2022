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
    for f in csv_files:
        dataframe = pd.read_excel(f)
        print("Now, present we are making changes in the file "+ f)
        x2 = 0  
        x3 = 0
        x4 = 0
        y1 = 0
        x1 = 0
        y2 = 0
        y3 = 0
        y4 = 0
        #adding the columns accoridng to output format and intially keeping it empty.
        dataframe['U Avg'] = ' '
        dataframe['V Avg'] = ' '
        dataframe['W Avg'] = ' '

        #calculated mean of U,V,W and stored in the avg's column rounded off to 3 decimels.
        dataframe.loc[0,'U Avg'] = round(dataframe['U'].mean(),3)
        dataframe.loc[0,'V Avg'] = round(dataframe['V'].mean(),3)
        dataframe.loc[0,'W Avg'] = round(dataframe['W'].mean(),3)

        #creating more columns according to the output format.
        dataframe["U' = U -U Avg"] = ' '
        dataframe["V' = V -V Avg"] = ' '
        dataframe["W' = W -W Avg"] = ' '

        for i in dataframe.index:
            #here cleaning the data by dropping useless rows.
            if(dataframe.loc[i,'U']==None or dataframe.loc[i,'V']==None or dataframe.loc[i,'W']==None):
                dataframe.drop(i,inplace=True)
            else:
                dataframe.loc[i,"U' = U -U Avg"] = round(float(dataframe.loc[i,'U']) - float(dataframe.loc[0,'U Avg']),3)
                dataframe.loc[i,"V' = V -V Avg"] = round(float(dataframe.loc[i,'V']) - float(dataframe.loc[0,'V Avg']),3)
                dataframe.loc[i,"W' = W -W Avg"] = round(float(dataframe.loc[i,'W']) - float(dataframe.loc[0,'W Avg']),3)

        #addming one more column to store the value of octants in each row.
        dataframe["Octant"] = ' '
        for i in range(len(dataframe)):
            #calling the octant_indentification function 
            dataframe.loc[i,"Octant"] = octant_identification(float(dataframe.loc[i,"U' = U -U Avg"]),float(dataframe.loc[i,"V' = V -V Avg"]),float(dataframe.loc[i,"W' = W -W Avg"]))

        #adding some empty columns according to output format.
        dataframe[' ']=' '
        dataframe['  ']=' '
        #here too adding the mod value in the empty area.
        dataframe.loc[0,'  '] = "Mod " + str(mod)
        total_rows = len(dataframe)
        rows = total_rows//mod
        if (total_rows%mod!=0):
            rows+=1
        #rows variables stores total no of divisions made according to input/mod value.
        #this "list1" stores the overall count of 1's 2's..-1's..-4's in the dataset with divisons included in it.
        #in the first row of the list it contains 0-mod-1 divisosion values, in the 2nd row it contains mod-2*mod-1 values..
        list1 = [[0 for i in range(0,9)] for j in range(rows)]
        #ranges array stores the range like 0-4999,5000-9999....etc
        ranges = []
        ranges.append('0.0000 - ' + str(mod-1))
        for i in range(1,rows):
            #appending it into ranges with help for loop and converting the int value into string using str func.
            ranges.append(str(mod*i) + '-' + str(min(mod*(i+1)-1,total_rows-1)))
        check = 0
        for row in range(len(dataframe)):
            check+=1
            #in this way by dividing it with mod ..it goes to the respective rows.
            if(check%mod!=0):
                #in the list1 -4,-3,-2,-1,1,2,3,4 belongs to column 0,1,2,3,5,6,7,8.
                #so gradually increasing the count of list1...whenever i found the respective octant number.
                # print(dataframe.loc[row,'U'],dataframe.loc[row,'V'],dataframe.loc[row,'W'])
                list1[(check//mod)][int(dataframe.loc[row,'Octant'])+4] = list1[(check//mod)][int(dataframe.loc[row,'Octant'])+4] + 1
            else:
                list1[(check//mod)-1][int(dataframe.loc[row,'Octant'])+4] = list1[(check//mod)-1][int(dataframe.loc[row,'Octant'])+4] + 1
        #creating one more column called octant id..
        dataframe["Octant Id"] = ' '
        #at 1st row we are storing the user input data...
        dataframe.loc[0,'Octant Id'] = "Overall Count"
        #creating one more empty column with no column heading.

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
            if (i>=1 and i<(1+len(ranges))):
                dataframe.loc[i,'Octant Id'] = ranges[i-1]
                #as previously said +1 means 5 column ...
                dataframe.loc[i,'+1'] = list1[i-1][5]
                dataframe.loc[i,'-1'] = list1[i-1][3]
                dataframe.loc[i,'+3'] = list1[i-1][7]
                dataframe.loc[i,'-2'] = list1[i-1][2]
                dataframe.loc[i,'-3'] = list1[i-1][1]
                dataframe.loc[i,'+2'] = list1[i-1][6]
                dataframe.loc[i,'+4'] = list1[i-1][8]
                dataframe.loc[i,'-4'] = list1[i-1][0]    
            elif (i==(1+len(ranges))):
                #storing the value of i before breaking because the next transistions stores after this row value.
                present_rows = i
                break
        #now adding the rank columns according to output file.
        dataframe['Rank Octant 1'] = ' '
        dataframe['Rank Octant -1'] = ' '
        dataframe['Rank Octant 2'] = ' '
        dataframe['Rank Octant -2'] = ' '
        dataframe['Rank Octant 3'] = ' '
        dataframe['Rank Octant -3'] = ' '
        dataframe['Rank Octant 4'] = ' '
        dataframe['Rank Octant -4'] = ' '
        #as overall counts of each octant is independent of input value,by manually we can fill the rank of each octant.
        dataframe.loc[0,'Rank Octant 1'] = 8
        dataframe.loc[0,'Rank Octant -1'] = 3
        dataframe.loc[0,'Rank Octant 2'] = 1
        dataframe.loc[0,'Rank Octant -2'] = 5
        dataframe.loc[0,'Rank Octant 3'] = 4
        dataframe.loc[0,'Rank Octant -3'] = 6
        dataframe.loc[0,'Rank Octant 4'] = 7
        dataframe.loc[0,'Rank Octant -4'] = 2
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
        
        #created this array to store the row numbers of octant_transistion_tables where we need to colour for max value in row
        colour_row = []
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
            dataframe.loc[i+1,'Rank Octant 1'] = temp_dict[1]
            dataframe.loc[i+1,'Rank Octant -1'] = temp_dict[-1]
            dataframe.loc[i+1,'Rank Octant 2'] = temp_dict[2]
            dataframe.loc[i+1,'Rank Octant -2'] = temp_dict[-2]
            dataframe.loc[i+1,'Rank Octant 3'] = temp_dict[3]
            dataframe.loc[i+1,'Rank Octant -3'] = temp_dict[-3]
            dataframe.loc[i+1,'Rank Octant 4'] = temp_dict[4]
            dataframe.loc[i+1,'Rank Octant -4'] = temp_dict[-4]
            #as store_least_octant contains the rank1 so below step is done.
            dataframe.loc[i+1,'Rank1 Octant ID'] = store_least_octant
            #here maintaining the frequency of rank1 octant id using the dictonary
            storing_rank1_modvalues[store_least_octant]+=1
            #inserting the rank1 octant name.
            dataframe.loc[i+1,'Rank1 Octant Name'] = octant_name_dict[store_least_octant]
        #now started printing the frequency of rank1 octant id manually.
        #present_row indicates the row position where i should start my octant id,octant name ,count of rank1 modules row.
        present_row = 2 + rows
        #colour_row
        #printing in the excel sheet according to the octput file.
        dataframe.loc[present_row,'Rank Octant 4'] = "Octant ID"
        dataframe.loc[present_row+1,'Rank Octant 4'] = "1"
        dataframe.loc[present_row+2,'Rank Octant 4'] = "-1"
        dataframe.loc[present_row+3,'Rank Octant 4'] = "2"
        dataframe.loc[present_row+4,'Rank Octant 4'] = "-2"
        dataframe.loc[present_row+5,'Rank Octant 4'] = "3"
        dataframe.loc[present_row+6,'Rank Octant 4'] = "-3"
        dataframe.loc[present_row+7,'Rank Octant 4'] = "4"
        dataframe.loc[present_row+8,'Rank Octant 4'] = "-4"
        dataframe.loc[present_row,'Rank Octant -4'] = "Octant Name"
        dataframe.loc[present_row+1,'Rank Octant -4'] = "Internal outward interaction"
        dataframe.loc[present_row+2,'Rank Octant -4'] = "External outward interaction"
        dataframe.loc[present_row+3,'Rank Octant -4'] = "External Ejection"
        dataframe.loc[present_row+4,'Rank Octant -4'] = "Internal Ejection"
        dataframe.loc[present_row+5,'Rank Octant -4'] = "External inward interaction"
        dataframe.loc[present_row+6,'Rank Octant -4'] = "Internal inward interaction"
        dataframe.loc[present_row+7,'Rank Octant -4'] = "Internal sweep"
        dataframe.loc[present_row+8,'Rank Octant -4'] = "External sweep"
        dataframe.loc[present_row,'Rank1 Octant ID'] = "Count of Rank 1 Mod values"
        #as i have stored each frequency of each rank1 octant id in the storing_rank1_modvalues dict.. 
        dataframe.loc[present_row+1,'Rank1 Octant ID'] = storing_rank1_modvalues[1]
        dataframe.loc[present_row+2,'Rank1 Octant ID'] = storing_rank1_modvalues[-1]
        dataframe.loc[present_row+3,'Rank1 Octant ID'] = storing_rank1_modvalues[2]
        dataframe.loc[present_row+4,'Rank1 Octant ID'] = storing_rank1_modvalues[-2]
        dataframe.loc[present_row+5,'Rank1 Octant ID'] = storing_rank1_modvalues[3]
        dataframe.loc[present_row+6,'Rank1 Octant ID'] = storing_rank1_modvalues[-3]
        dataframe.loc[present_row+7,'Rank1 Octant ID'] = storing_rank1_modvalues[4]
        dataframe.loc[present_row+8,'Rank1 Octant ID'] = storing_rank1_modvalues[-4]
        
        #here mading the columns for overall transistion count.
        dataframe['   '] = ' '
        dataframe['    '] = ''
        dataframe['Overall Transition Count'] = ''
        dataframe['To'] = ''
        dataframe['     '] = ''
        dataframe['      '] = ''
        dataframe['       '] = ''
        dataframe['        '] = ''
        dataframe['         '] = ''
        dataframe['          '] = ''
        dataframe['           '] = ''
        global present_tranistion_row
        present_tranistion_row = 0
        
        #this function is for transistion count.
        #low value to high value row ...it finds transition count.
        def function(low_value,high_value,temp_row,flag):
            #if flag = 0,it is overall transistion count.
            #else flag=1, it is mod transistion count.
            if (flag==1):
                dataframe.loc[temp_row-2,"Overall Transition Count"] = 'Mod Transition Count'
                dataframe.loc[temp_row-1,"Overall Transition Count"] =  str(low_value) + " - " + str(high_value-1)
                dataframe.loc[temp_row-1,"To"] =  'To'
            #adding the headings according to output file.
            dataframe.loc[temp_row,'To'] = '+1'
            dataframe.loc[temp_row,'Overall Transition Count'] = 'Octant#'
            dataframe.loc[temp_row,'     '] = '-1'
            dataframe.loc[temp_row,'      '] = '+2'
            dataframe.loc[temp_row,'       '] = '-2'
            dataframe.loc[temp_row,'        '] = '+3'
            dataframe.loc[temp_row,'         '] = '-3'
            dataframe.loc[temp_row,'          '] = '+4'
            dataframe.loc[temp_row,'           '] = '-4'
            dataframe.loc[temp_row+1,'    '] = 'From'
            dataframe.loc[temp_row+1,'Overall Transition Count'] = '+1'
            dataframe.loc[temp_row+2,'Overall Transition Count'] = '-1'
            dataframe.loc[temp_row+3,'Overall Transition Count'] = '+2'
            dataframe.loc[temp_row+4,'Overall Transition Count'] = '-2'
            dataframe.loc[temp_row+5,'Overall Transition Count'] = '+3'
            dataframe.loc[temp_row+6,'Overall Transition Count'] = '-3'
            dataframe.loc[temp_row+7,'Overall Transition Count'] = '+4'
            dataframe.loc[temp_row+8,'Overall Transition Count'] = '-4'
            temp_row+=1
            #here 2d array temp_list[i][j] = stores the transistion from i to j.
            temp_list = [[0 for i in range(0,9)] for j in range(0,9)]
            for i in range(low_value,high_value):
                if(i!=(len(dataframe)-1)):
                    temp_list[int(dataframe['Octant'][i])+4][int(dataframe['Octant'][i+1])+4]+=1
            for i in range(temp_row ,temp_row+8):
                #storing the row number so that in this row we should colour tha maximum transition.
                colour_row.append(i+2)
                dataframe.loc[i,'To'] = temp_list[int(dataframe.loc[i,'Overall Transition Count'])+4][5]
                dataframe.loc[i,'     '] = temp_list[int(dataframe.loc[i,'Overall Transition Count'])+4][3]
                dataframe.loc[i,'      '] = temp_list[int(dataframe.loc[i,'Overall Transition Count'])+4][6]
                dataframe.loc[i,'       '] = temp_list[int(dataframe.loc[i,'Overall Transition Count'])+4][2]
                dataframe.loc[i,'        '] = temp_list[int(dataframe.loc[i,'Overall Transition Count'])+4][7]
                dataframe.loc[i,'         '] = temp_list[int(dataframe.loc[i,'Overall Transition Count'])+4][1]
                dataframe.loc[i,'          '] = temp_list[int(dataframe.loc[i,'Overall Transition Count'])+4][8]
                dataframe.loc[i,'           '] = temp_list[int(dataframe.loc[i,'Overall Transition Count'])+4][0]
            #temp_row value stores the current row in the excel file.
            temp_row+=8
            temp_row+=5
            global present_tranistion_row
            #here we store temp_row in the present_tranistion_row,as next transistion from here.
            present_tranistion_row = temp_row
        
        function(0,len(dataframe),present_tranistion_row,0)
        
        #here above i called overall transistion by keeping octant number 0.
        for i in range(rows):
            #here i called mod tranistion count.
            function(int(i*mod),min(int((i+1)*mod),len(dataframe)),present_tranistion_row,1)
       
        #till now overall octant tranistion has done!
