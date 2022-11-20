try:
    from datetime import datetime as dt
    start_time = dt.now()
    import smtplib
    from email.mime.multipart import MIMEMultipart
    from email.mime.text import MIMEText
    from email.mime.base import MIMEBase
    from email import encoders
    import csv
    from numpy import NaN
    import pandas as pd
    import datetime 
    from random import randint
    from time import sleep
    from platform import python_version
    try:
        def attendance_report():
            #reading the input files using pandas.
            dataframe_attendance = pd.read_csv('input_attendance.csv')
            dataframe_registered = pd.read_csv('input_registered_students.csv')
            dataframe_attendance['Roll']=''
            dataframe_attendance['Name']=''
            deleted_rows = 0
            #Here i have made two separate columns for roll no,name which is divided from attednace column,later dropping the attendance column.
            for i in range(0,len(dataframe_attendance)):
                x = dataframe_attendance['Attendance'][i]
                if(type(x)==str):
                    y = x[0:8]
                    z = x[9:]
                    dataframe_attendance['Roll'][i]=y
                    dataframe_attendance['Name'][i]=z
                else:
                    deleted_rows+=1
                    dataframe_attendance['Roll'][i]=NaN
                    dataframe_attendance['Name'][i]=NaN
            dataframe_attendance.drop('Attendance',inplace=True,axis=1)
            #here aslo in the same way from the timestamp i am seprating both date and time using pandas.
            dataframe_attendance['Date']=''
            dataframe_attendance['Time']=''
            for i in range(0,len(dataframe_attendance)):
                x = pd.to_datetime(dataframe_attendance['Timestamp'][i],format = "%d-%m-%Y %H:%M")
                dataframe_attendance['Date'][i]=x.date()
                dataframe_attendance['Time'][i]=x.time()
                dataframe_attendance['Timestamp'][i]=x

            for j in range(0,len(dataframe_attendance)):
                start_date = dataframe_attendance['Timestamp'][j]
                break
            for j in range(0,len(dataframe_attendance)):
                end_date = dataframe_attendance['Timestamp'][j]  
            #lecture days are the days between start_date and end_date which includes all mondays and thursdays.
            #created this dictonaries to store no of lecture days between start date and end date.
            #lecture_days contains only valid dates(means mon,thur)
            lecture_days =  {}
            #total_days contains all the dates between start_date to end_date..but (mon,thur marked as 1, other marked as 0)
            total_days = {}
            while(start_date.date()<=end_date.date()):
                if(start_date.day_name()=="Monday" or start_date.day_name()=='Thursday'):
                    lecture_days[start_date.date()]=1
                    total_days[start_date.date()]=1
                else:
                    total_days[start_date.date()]=0
                #using pandas dateoffset i am iterating each date.
                start_date = start_date + pd.DateOffset(days=1)
            #now i am sorting the dataframe_attendance based on rol no date time so it would be convenient to compare with data of registered_students.
            sorted_df = dataframe_attendance.sort_values(by=['Roll','Date','Time'])
            sorted_df = sorted_df.reset_index()
            sorted_df.drop('index',inplace=True,axis=1)
            sorted_df.drop('Timestamp',inplace=True,axis=1)
            #storing the lecture dates in the list called dates_list.
            dates_list = []
