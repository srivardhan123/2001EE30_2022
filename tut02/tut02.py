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
    mod  = int(5000)
    #total no of rows present in the dataset.
    total_rows = len(dataframe)
    try:
        rows = total_rows//mod
        if (total_rows%mod!=0):
            rows+=1
        #rows vairiables stores total no of divisions made...

        #this list stores the overall count of 1's 2's..-1's..-4's in the dataset with divisons included in it.
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
            if(check%5000!=0):
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
        #creating this function to avoid printing mod transistion counts each time for each range of numbers.
        #so we can just call the function for each set of ranges...
        #lowvalue means from which row we are going to start our dataset..
        #highvalue means which row we are ending our dataset.
        #temp_pres_row(local variable inside the func) is the present row which i am going to add in dataframe or print in the excel.
        #flag is the variable which will be helpful to us to differetiate us whether it is overall transition count or mod tranistion count.
        def functions(lowvalue,highvalue,temp_pres_row,flag):
            #adding +2 becuase between each mod transistion table there are two lines gap..
            temp_pres_row+=2
            #intitally adding to,from,Overall Transition Count or Mod Transition Count in the respetives places acrdng to temp_pres_row.
            if(flag==0):
                dataframe.loc[temp_pres_row,' '] = "Overall Transition Count"
            else :
                dataframe.loc[temp_pres_row,' '] = "Mod Transition Count"
            temp_pres_row+=1
            #here if flag is not zero means its a mod tranistion count 
            if(flag!=0 and flag!=1):
                dataframe.loc[temp_pres_row,' '] = str(lowvalue) + " - " + str(highvalue-1)
            if(flag==1):
                dataframe.loc[temp_pres_row,' '] = "0.000" + " - " + str(highvalue-1)
            dataframe.loc[temp_pres_row,'+1'] = "To"
            temp_pres_row+=1
            #created this 2d list which stores the values like a transistion table which shown in output file 
            #-4,-3,-2,-1,1,2,3,4 indicates 0,1,2,3,5,6,7,8 respectively in the indexes of 2d list
            #-4 to 1 transition indicates list1[0][5]...
            temp_list = [[0 for i in range(0,9)] for j in range(0,9)]
            # range of for loop is just from lowvalue to highvalue because we need for only the particular transition..
            for i in range(lowvalue,highvalue):
                #added this if conditon because last transition wont possible 29744 to 29745..
                #in the range low to high value....(highvalue-1 to highvalue is also included in the transition)
                if(i!=29744):
                    temp_list[int(dataframe['Octant'][i])+4][int(dataframe['Octant'][i+1])+4]+=1

            #now here at present temp_pres_row i am storing all the headings count,+1,....-4..
            dataframe.loc[temp_pres_row,' '] = "Count"
            dataframe.loc[temp_pres_row,'+1'] = '+1'
            dataframe.loc[temp_pres_row,'+2'] = '+2'
            dataframe.loc[temp_pres_row,'+3'] = '+3'
            dataframe.loc[temp_pres_row,'+4'] = '+4'
            dataframe.loc[temp_pres_row,'-1'] = '-1'
            dataframe.loc[temp_pres_row,'-2'] = '-2'
            dataframe.loc[temp_pres_row,'-3'] = '-3'
            dataframe.loc[temp_pres_row,'-4'] = '-4'
            temp_pres_row+=1
            #increasing the temp_pres_row becuase in the next row we have to print according to output file.
            #i have wrote temp_pres_rpw,+1,+2...so on becuase in the particular columns in each row i have printed accrdng to output file.
            dataframe.loc[temp_pres_row,'Octant Id'] = 'From'
            dataframe.loc[temp_pres_row,' '] = '1'
            dataframe.loc[temp_pres_row+1,' '] = '-1'
            dataframe.loc[temp_pres_row+2,' '] = '2'
            dataframe.loc[temp_pres_row+3,' '] = '-2'
            dataframe.loc[temp_pres_row+4,' '] = '3'
            dataframe.loc[temp_pres_row+5,' '] = '-3'
            dataframe.loc[temp_pres_row+6,' '] = '4'
            dataframe.loc[temp_pres_row+7,' '] = '-4'

            #now printing the mod transistion values which are stored in the temp_list..
            #printing it in the excel sheet in the rows accoridng to the output file with help of temp_pres_row to temp_pres_row+8.
            for i in range(temp_pres_row ,temp_pres_row+8):
                    dataframe.loc[i,'+1'] = temp_list[int(dataframe.loc[i,' '])+4][5]
                    dataframe.loc[i,'-1'] = temp_list[int(dataframe.loc[i,' '])+4][3]
                    dataframe.loc[i,'+2'] = temp_list[int(dataframe.loc[i,' '])+4][6]
                    dataframe.loc[i,'-2'] = temp_list[int(dataframe.loc[i,' '])+4][2]
                    dataframe.loc[i,'+3'] = temp_list[int(dataframe.loc[i,' '])+4][7]
                    dataframe.loc[i,'-3'] = temp_list[int(dataframe.loc[i,' '])+4][1]
                    dataframe.loc[i,'+4'] = temp_list[int(dataframe.loc[i,' '])+4][8]
                    dataframe.loc[i,'-4'] = temp_list[int(dataframe.loc[i,' '])+4][0]
            #increasing the temp_pres_row value by 8...
            temp_pres_row= temp_pres_row + 8
            #now storing the temp_pres_row in the global variable present_rows
            global present_rows
            present_rows = temp_pres_row
                  #calling the the function here to print overall tranistion count!.
        #overall transition count is range from 0 to 29745... and present_rows indicate the row value where our table is start going to print.
        functions(0,29745,present_rows,0)

        for i in range(rows):
                #total no of transitons is equal to rows value.
                #low value,high value would be from 0 to mod-1,mod to 2*mod-1...so on..
                #present_rows value changes globally....
                functions(int(i*mod),min(int((i+1)*mod),29745),present_rows,i+1)

        #finally exporting this into output file by keeping index=False becuase we dont need the index column.
        dataframe.to_excel('output_octant_transition_identify.xlsx',index=False)
    except:
        print("you have taken input as zero.")
except:
        print("input file is not present in the same folder")


