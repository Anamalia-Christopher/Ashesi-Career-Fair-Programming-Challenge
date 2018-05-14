import csv
import datetime 
import time
path = "sample_simple_ebola_data.csv"
file = open(path)
read = csv.reader(file)
date=datetime.datetime
dataset = [raw for raw in read]

#print(dataset)
numb_raw =len(dataset)
list_date = []
#print (dataset)
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
'''Question a the last case of Ebola'''
def lastcase():
    idxlastraw = numb_raw - 1
    return (dataset[idxlastraw][3])
lastcase()
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
'''Question b: the last death case'''    
def lastdeath():
    date_list = []
    for n in range (numb_raw):
        if dataset[n][2]=="cumulative_deaths":
            date_list.append(dataset[n][3])

    return (date_list[-1])
lastdeath()
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
''' Question c: Date to be declared Ebola free'''

def dateFree():
    dateformat = "%d/%m/%Y"
    n = 0
    formated_data = []
    standard_date = []
    for i in range(1,numb_raw):
        if dataset[i][2] == 'cummulative_cases':
            formated_data.append(dataset[i][3])
            a = formated_data[n]
            date = datetime.datetime.strptime(a, "%d/%m/%Y")
            standard_date.append(date)
            n = n+1
    date_counter = 1
    for m in range(len(standard_date)-1):
        difference_date = standard_date[m+1]-standard_date[m]
        if difference_date >= datetime.timedelta(42):        
            print("Guinea could have been declared Ebola-free  on",standard_date[m])
        date_counter = date_counter + 1
dateFree()
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
'''Question d: Between which dates was the infection rate the highest?'''

def cases_rate_peak():
    rate= 0
    for i in range(3, len(dataset)):
        if dataset[i][2] == "cumulative_cases":


            time2= date.strptime(dataset[i][3], "%d/%m/%Y") - date.strptime(dataset[i-2][3], "%d/%m/%Y")

            value_diff= int(dataset[i][4]) - int(dataset[i-2][4])
            rate_of_cases = value_diff/(time2/datetime.timedelta(1))

            if rate_of_cases>rate:
                rate= rate_of_cases
                j=i
    print(rate)
    ans= "Between " + dataset[j-2][3] + " and " + dataset[j][3]
    print(ans)

cases_rate_peak()


#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
'''Question e: Between which dates was the infection rate the highest?'''
def death_rate_peak():
    rate= 0
    for i in range(3, len(dataset)):
        if dataset[i][2] == "cumulative_deaths":

            time1= date.strptime((dataset[i-2][3]), "%d/%m/%Y")
            time12=date.strptime(dataset[i][3], "%d/%m/%Y")

            time2= date.strptime(dataset[i][3], "%d/%m/%Y") - date.strptime(dataset[i-2][3], "%d/%m/%Y")

            value_diff= int(dataset[i][4]) - int(dataset[i-2][4])
            rate_of_death = value_diff/(time2/datetime.timedelta(1))

            if rate_of_death>rate:
                rate= rate_of_death
                j=i
    print(rate)
    ans= "Between " + dataset[j-2][3] + " and " + dataset[j][3]
    print(ans)

death_rate_peak()


#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------
'''Question f the '''

def infection_peaks():
    
    case_list = []
    infection_rate = []
    infection_date = []
    for i in range(1,numb_raw):
        if dataset[i][2]=="cumulative_cases":
            case_list.append(dataset[i][4])
            infection_date.append(dataset[i][3])
    #print (case_list)
    for n in range(len(case_list)-1):
        infection_rate.append(int(case_list[n+1])-int(case_list[n]))

    inbetween_infection_date = []
    for m in range(1,len(infection_date)):
        inbetween_infection_date.append([])
        inbetween_infection_date[m-1].append(infection_date[m-1]) #I created a list of lists(pair dates) to store in between days.
        inbetween_infection_date[m-1].append(infection_date[m])
    
    a=0
    list_peaks = []
    peaks_dates = []
    for n in range(len(infection_rate)-1):
        b=a+1
        c=a+2
        if infection_rate[b]>infection_rate[a] and infection_rate[b]>infection_rate[c]:
            list_peaks.append(infection_rate[b])
            peaks_dates.append(inbetween_infection_date[b])
        a=a+1
    print ("There were",len(list_peaks),"infection peaks which occured on the folloing date:")
    for i in range(len(peaks_dates)):
           print('between',peaks_dates[i][0],'and', peaks_dates[i][1])  
    
    
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------
'''Question g the death peaks '''

def death_peaks():
    death_list = []
    death_rate = []
    death_date = []
    for i in range(1,numb_raw):
        if dataset[i][2]=="cumulative_deaths":
            death_list.append(dataset[i][4])
            death_date.append(dataset[i][3])
    #print (case_list)
    for n in range(len(death_list)-1):
        death_rate.append(int(death_list[n+1])-int(death_list[n]))

    inbetween_death_date = []
    for m in range(1,len(death_date)):
        inbetween_death_date.append([])
        inbetween_death_date[m-1].append(death_date[m-1]) #I created a list of lists(pair dates) to store in between days.
        inbetween_death_date[m-1].append(death_date[m])
    
    a=0
    list_peaks = []
    peaks_dates = []
    for n in range(len(death_rate)-1):
        b=a+1
        c=a+2
        if death_rate[b]>death_rate[a] and death_rate[b]>death_rate[c]:
            list_peaks.append(death_rate[b])
            peaks_dates.append(inbetween_death_date[b])
        a=a+1
    print ("There were",len(list_peaks),"death peaks which occured on the folloing date:")
    for i in range(len(peaks_dates)):
           print('between',peaks_dates[i][0],'and', peaks_dates[i][1])

#death_peaks()

#print(dataset)

