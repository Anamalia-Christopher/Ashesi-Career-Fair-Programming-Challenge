import csv
import datetime 
import sys
import task1

start_work= datetime.datetime.now()
start = datetime.datetime.now()
date=datetime.datetime
path = sys.argv[-1]
file = open(path)
read = csv.reader(file)

dataset = [raw for raw in read]
answer= open("task1_answers-sample_simple_ebola_data.txt", "w")
times= open ("task1_times-sample_simple_ebola_data.txt", 'w')
#print(dataset)
numb_raw =len(dataset)
list_date = []
#print (dataset)
stop= datetime.datetime.now()
pre_processing_time= stop-start
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
'''Question a the last case of Ebola'''
start = datetime.datetime.now()
def lastcase():
    date_list = []
    for n in range (numb_raw):
        if dataset[n][2]=="cumulative_cases":
            date_list.append(dataset[n][3])
    a = date_list[-1]
    return (a)
lastcase()
stop= datetime.datetime.now()
a_runtime= stop-start
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
'''Question b: the last death case'''
start = datetime.datetime.now()
def lastdeath():
    date_list = []
    for n in range (numb_raw):
        if dataset[n][2]=="cumulative_deaths":
            date_list.append(dataset[n][3])
    a = date_list[-1]
    return a
lastdeath()
stop= datetime.datetime.now()
b_runtime= stop-start
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
''' Question c: Date to be declared Ebola free'''

start = datetime.datetime.now()
def dateFree():
    dateformat = "%d/%m/%Y"
    n = 0
    formated_data = []
    standard_date = []
    cases_list = []
    for i in range(1,numb_raw):
        if dataset[i][2] == 'cumulative_cases':
            formated_data.append(dataset[i][3])
            a = formated_data[n]
            date = datetime.datetime.strptime(a, "%d/%m/%Y")
            standard_date.append(date)
            cases_list.append(dataset[i][4])
            n = n+1
        #print(cases_list)    
            
    date_counter = 1
    for m in range(len(standard_date)-1):
        difference_date = standard_date[m+1]-standard_date[m]
        difference_case = int(cases_list[m+1])-int(cases_list[m])
        if difference_date >= datetime.timedelta(42) and difference_case==0:        
            return ("Guinea could have been declared Ebola-free  on " + str(standard_date[m]))
        date_counter = date_counter + 1

#dateFree()
stop= datetime.datetime.now()
c_runtime= stop-start
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
'''Question d: Between which dates was the infection rate the highest?'''

start = datetime.datetime.now()
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

    ans= "Between " + dataset[j-2][3] + " and " + dataset[j][3]
    return ans
stop= datetime.datetime.now()
d_runtime= stop-start
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
'''Question e: Between which dates was the infection rate the highest?'''
start = datetime.datetime.now()
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

    ans= "Between " + dataset[j-2][3] + " and " + dataset[j][3]
    return ans
stop= datetime.datetime.now()
e_runtime= stop-start
#death_rate_peak()
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------
'''Question f the '''
start = datetime.datetime.now()
def case_peaks():
    case_list = []
    case_rate = []
    case_date = []
    difference_date = []
    formated_data = []
    standard_date = []
    case_pairs =[]
    n = 0
    for i in range(1,numb_raw):
        if dataset[i][2]=="cumulative_cases":
            case_list.append(dataset[i][4])
            formated_data.append(dataset[i][3])
            a = formated_data[n]
            date = datetime.datetime.strptime(a,"%d/%m/%Y")
            standard_date.append(date)
            n =n+1

    for m in range(1,len(standard_date)):
        case_pairs.append([])
        case_pairs[m-1].append(standard_date[m-1])
        case_pairs[m-1].append(standard_date[m])
        differences = case_pairs[m-1][1]-case_pairs[m-1][0]
        difference_date.append(differences)


            
        
    for n in range(len(case_list)-1):
        case_rate.append((int(case_list[n+1])-int(case_list[n]))/((int(differences/datetime.timedelta(1))/86400000)))
    a=0
    list_peaks = []
    peaks_dates = []
    for n in range(len(case_rate)-1):
        b=a+1
        c=a+2
        if case_rate[b]>case_rate[a] and case_rate[b]>case_rate[c]:
            list_peaks.append(case_rate[b])
            peaks_dates.append(standard_date[b])
        a=a+1
    ans= "There were "+str(len(list_peaks))+" case peaks which occured on the folloing dates:" +"\n"
    for i in range(len(peaks_dates)):
           ans+= str(peaks_dates[i])+"\n"
  
    return ans #("There were "+str(len(list_peaks))+" case peaks which occured on the folloing dates:" +"\n")
stop= datetime.datetime.now()
f_runtime= stop-start

#case_peaks()
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------
'''Question g the death peaks '''
start = datetime.datetime.now()
def death_peaks():
    death_list = []
    death_rate = []
    death_date = []
    difference_date = []
    formated_data = []
    standard_date = []
    death_pairs =[]
    n = 0
    for i in range(1,numb_raw):
        if dataset[i][2] == "cumulative_deaths":
            death_list.append(dataset[i][4])
            formated_data.append(dataset[i][3])
            a = formated_data[n]
            date = datetime.datetime.strptime(a,"%d/%m/%Y")
            standard_date.append(date)
            n =n+1

    for m in range(1, len(standard_date)):
        death_pairs.append([])
        death_pairs[m-1].append(standard_date[m-1])
        death_pairs[m-1].append(standard_date[m])
        differences = death_pairs[m-1][1]-death_pairs[m-1][0]
        difference_date.append(differences)

    for n in range(len(death_list)-1):
        death_rate.append((int(death_list[n+1])-int(death_list[n]))/((int(differences/datetime.timedelta(1))*86400000)))
    a=0
    list_peaks = []
    peaks_dates = []
    for n in range(len(death_rate)-1):
        b = a+1
        c = a+2
        if death_rate[b] > death_rate[a] and death_rate[b] > death_rate[c]:
            list_peaks.append(death_rate[b])
            peaks_dates.append(standard_date[b+1])#####

        a=a+1
    print(peaks_dates)
    ans = "There were " + str(len(list_peaks)) + " case peaks which occured on the folloing dates:" + "\n"
    # return ("There were",len(list_peaks),"death peaks which occured on the folloing dates:")

    for i in range(len(peaks_dates)):
        ans += str(peaks_dates[i]) + "\n"

    return ans#("There were "+str(len(list_peaks))+" death peaks which occured on the folloing dates:")
stop= datetime.datetime.now()
g_runtime= stop-start

end_work= datetime.datetime.now()
overall_time= end_work- start_work
#death_peaks()
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    
        
answer.write("(a) " +lastcase() + "\n")
answer.write("(b) " +lastdeath() + "\n")
answer.write("(c) " +dateFree() + "\n")
answer.write("(d) " +cases_rate_peak() + "\n")
answer.write("(e) " +death_rate_peak() + "\n")
answer.write("(f) " +case_peaks() + "\n")
answer.write("(g) " +death_peaks() + "\n")
    
times.write("file_reading and pre-processing= " +str(pre_processing_time.microseconds/1000)+ "\n")
times.write("'a' runtime= " +str(a_runtime.microseconds/1000)+ "\n")
times.write("'b' runtime= " +str(b_runtime.microseconds/1000)+ "\n")
times.write("'c' runtime= " +str(c_runtime.microseconds/1000)+ "\n")
times.write("'d' runtime= " +str(d_runtime.microseconds/1000)+ "\n")
times.write("'e' runtime= " +str(e_runtime.microseconds/1000)+ "\n")
times.write("'f' runtime= " +str(f_runtime.microseconds/1000)+ "\n")
times.write("'g' runtime= " +str(g_runtime.microseconds/1000)+ "\n")
times.write("overall runtime= " +str(overall_time.microseconds/1000)+ "\n")