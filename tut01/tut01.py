import csv
import os
os.system('clear')

# here i am reading the input csv file line by line 
with open('octant_input.csv', 'r') as file:
    reader = csv.reader(file,delimiter='\t')
    #creating U,V,W_totalsum variable to store total sum all U,V,W respectively.
    U_totalsum = 0 
    #U_count is used to count the  total no of rows present in the octant_input.csv file
    U_count = 0
    V_totalsum = 0
    W_totalsum = 0
    for row in reader:
        #used this if condition because the first row contains heading so to exclude that row
       if(row[0]!='Time'):
            #adding each u,v,w in the respective variables.
            U_totalsum = U_totalsum + float(row[1])
            U_count = U_count + 1
            V_totalsum = V_totalsum + float(row[2])
            W_totalsum = W_totalsum + float(row[3])
    #storing the U,V,W avg in U_avg,V_avg,W_avg respective varaibles.
    U_avg = U_totalsum/U_count
    V_avg = V_totalsum/U_count
    W_avg = W_totalsum/U_count

#created this each varaible to store overall count of octant no 1,2,3,4,-1,-2,-3,-4.
octant_pos_1 = 0
octant_pos_2 = 0
octant_pos_3 = 0
octant_pos_4 = 0
octant_neg_1 = 0
octant_neg_2 = 0
octant_neg_3 = 0
octant_neg_4 = 0

#created this function to detect it in such a way that in which octant number it belongs.
#this functions returns the octant number of particular row.

def octant_identification(val,val1,val2):
    #val = U-Uavg
    #val1 = V-Vavg
    #val2 = W-Wavg
    if (val>0 and val1>0 and val2>0):
        #as we are storing no of 1's present in the octant_pos_1, similarly other elif conditions
        #declare the varaible globally because i have stored the count of octant numbers individually in those variables.
        global octant_pos_1
        #increasing the octant_pos_1 by 1 because this particular row belongs to octant no 1
        octant_pos_1 =  octant_pos_1 + 1
        return int(1)
    elif (val<0 and val1>0 and val2>0):
        global octant_pos_2
        octant_pos_2 = octant_pos_2 + 1
        return int(2)
    elif (val<0 and val1<0 and val2>0):
        global octant_pos_3
        octant_pos_3 = octant_pos_3 + 1
        return int(3)
    elif (val>0 and val1<0 and val2>0):
        global octant_pos_4
        octant_pos_4 = octant_pos_4 + 1
        return int(4) 
    elif (val>0 and val1>0 and val2<0):
        global octant_neg_1
        octant_neg_1 = octant_neg_1 + 1
        return int(-1)
    elif (val<0 and val1>0 and val2<0):
        global octant_neg_2
        octant_neg_2 = octant_neg_2 + 1
        return int(-2)
    elif (val<0 and val1<0 and val2<0):
        global octant_neg_3
        octant_neg_3 = octant_neg_3 + 1
        return int(-3)
    elif (val>0 and val1<0 and val2<0):
        global octant_neg_4
        octant_neg_4 = octant_neg_4 + 1
        return int(-4)

#created this variable to check total no of rows present.
total_rows = 0

#This duplicate_input file contains pre-processed data which includes U',V',W' and octant number.
#opening the input file in read mode and printing the output in (duplicate_input.csv) file.

with open('octant_input.csv','r') as file:
    with open('duplicate_input.csv', 'w') as file1:
        writer = csv.writer(file1)
        #check variables stores the present row number in the for loop.
        check = 0
        #used the delimiter to seprate the each column
        for row in csv.reader(file,delimiter='\t'):
            check = check + 1
            total_rows = total_rows + 1
            #(check==1) means that we are in the first which should contain headings of the dataset.
            if (check == 1) :
                writer.writerow(row+["U Avg", "V Avg","W Avg","U'=U - U avg","V'=V-V avg","W'=W - W avg","Octant"])
            elif (check == 2) :
 #check==2 means the 2nd row, here we have separated this becuase in only 2nd row we should print u_avg,v_avg,w_avg and remaining rows should be left empty.
                writer.writerow(row+[U_avg,V_avg,W_avg,float(row[1])-U_avg,float(row[2])-V_avg,float(row[3])-W_avg,octant_identification(float(row[1])-U_avg,float(row[2])-V_avg,float(row[3])-W_avg)])
            else :
                writer.writerow(row + [' ',' ',' ',float(row[1])-U_avg,float(row[2])-V_avg,float(row[3])-W_avg,octant_identification(float(row[1])-U_avg,float(row[2])-V_avg,float(row[3])-W_avg)])

#subtracting one row because that one row conatians a heading!
total_rows = total_rows - 1

#taking an user input, so that accordingly we divide the dataset and calculate individual octant number count.
mod = 5000
mod = int(mod)


rows = total_rows//mod
if (total_rows%mod!=0) :
    rows+=1

#here i have created 2D list which stores the count of octant no 1,-1,2,-2,3,-3,4,-4 in each interval of their mod value.
#here we storiing for a particular input how many divisions the data set is made into, to count the frequency of each octant no in the particular divison(0-4999,5000-9999..).
#intializing the 2d array with zero in all the cells.
list1 = [[0 for i in range(0,9)] for j in range(rows)]

#reading the duplicate_input file and storing the the each division value in a 2d list.
with open('duplicate_input.csv', 'r') as file:
    reader = csv.reader(file,delimiter=',')
    #check stores the present number of the row.
    check = 0
    for row in reader:
        #I have excluded this row because it contains headings.
      if (row[10]!='Octant'):
        check+=1
        #check//val divides into 0-4999,5000-9999,10000-14999 ... of numbers into 0,1,2,... respective indexs.
        list1[(check//mod)][int(row[10])+4] = list1[(check//mod)][int(row[10])+4] + 1

#here in this variable i am storing overall count of all octant numbers.
total_sum = octant_pos_1 + octant_pos_2 + octant_pos_3 + octant_pos_4 + octant_neg_1 + octant_neg_2 + octant_neg_3 + octant_neg_4
