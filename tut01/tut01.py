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
