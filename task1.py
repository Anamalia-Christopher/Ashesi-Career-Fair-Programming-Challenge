import pandas as pd
import time
from datetime import timedelta
import numpy as np
df = pd.read_csv("sample_simple_ebola_data.csv", index_col=0)
#print(df.shape)
# print(list(df.columns.values))



# print (df)
# print(df.Date)
#print(len(df))
test= df.iloc[[57]]
#print(list(test.columns.values))
#print(test.Indicator=="cumulative_cases")
#print(test.loc[[0,"Date"]])
#print(test["Date"][0])
#print(time.strptime(test["Date"][0], "%d/%m/%Y"))


def change_file():
    # df["Rate"]= (df["Value"].diff())
    #print(pd.to_datetime(df["Date"], format='%d/%m/%Y').diff())
    df["diff_days"] = pd.to_datetime(df["Date"], format='%d/%m/%Y').diff()
    df["Deaths_and_cases"] = 0
    df["Rate"]=0
    df['Rate'] = df['Rate'].astype(float)

    #print(df)
    for i in range(0,len(df)):

        row = df.iloc[i][4]
        #print(row)
        #print(row == pd.Timedelta(0))
        try:
            if row == pd.Timedelta(0) and i>1:
                df.iat[i, 4] = df.iloc[i-1][4]

        except Exception as e:

            df.iat[i, 4] = df.iloc[i - 1][4]
            #print(i)
            pass

        if i >1:
            df.iat[i,5] = df.iloc[i][3] - df.iloc[i-2][3]

            w=np.timedelta64(1, 'D')
            df.iat[i, 6] = float(df.iat[i,5]/(df.iat[i, 4] /w*1.0))

    #rint(df.diff_days)


    #print(df["Rate"].dtype)
    #print(df)


#change_file()
def last_case_recorded():
    global df
    date_last = "01/01/2012"
    date_last = time.strptime(date_last, "%d/%m/%Y")

    for i in range(0, len(df), 1):
        row = df.iloc[[i]]
        date_compare = row["Date"][0]
        if (row.Indicator == "cumulative_cases").bool():
            if (time.strptime(date_compare, "%d/%m/%Y") > date_last):
                date_last = time.strptime(date_compare, "%d/%m/%Y")
                j=i
    #print(str(date_last.tm_mday)+"/"+str(date_last.tm_mon)+"/"+str(date_last.tm_year))
    print(df.iloc[j][2])
    return df.iloc[j][2]
last_case_recorded()

def last_death_recorded():
    global df
    date_last = "01/01/2012"
    date_last = time.strptime(date_last, "%d/%m/%Y")

    for i in range(0, len(df), 1):
        row = df.iloc[[i]]
        date_compare = row["Date"][0]
        if (row.Indicator == "cumulative_deaths").bool():
            if (time.strptime(date_compare, "%d/%m/%Y") > date_last):
                date_last = time.strptime(date_compare, "%d/%m/%Y")
                j=i
    #print(str(date_last.tm_mday)+"/"+str(date_last.tm_mon)+"/"+str(date_last.tm_year))

    print(df.iloc[j][2])
    return df.iloc[j][2]

last_death_recorded()


def ebola_free():
    change_file()
    last_date = last_case_recorded()
    days_to_ebola_free = 0

    for i in range(len(df)):
        row = df.iloc[[i]]

        if (row.Deaths_and_cases == 0).bool() and (row.Indicator == "cumulative_cases").bool():
            days_to_ebola_free += row.diff_days/np.timedelta64(1, 'D')
            if (days_to_ebola_free >= 42).bool():
                #print(df.iloc[i][2])
                print(df)
                return df.iloc[i][2]

        elif (row.Deaths_and_cases != 0).bool() and (row.Indicator == "cumulative_cases").bool():
            days_to_ebola_free = 0



#ebola_free()


def infection_rate_highest():
    change_file()
    highest_rate=0
    print(df.Rate.dtype)
    for i in range(len(df)):
        row = df.iloc[[i]]
        if (row.Indicator == "cumulative_cases").bool() and (row.Rate > highest_rate).bool():

            highest_rate = row.Rate
            j = i

    print("Between the dates " + df.iloc[j--2][2] + " and "+df.iloc[j][2] + ",the infection rate is highest")


#infection_rate_highest()


def death_rate_highest():
    change_file()
    highest_rate=0
    print(df.Rate.dtype)
    for i in range(len(df)):
        row = df.iloc[[i]]
        if (row.Indicator == "cumulative_deaths").bool() and (row.Rate > highest_rate).bool():

            highest_rate = row.Rate
            j = i

    print("Between the dates " + df.iloc[j--2][2] + " and " + df.iloc[j][2] + ",the deathn rate is highest")


#death_rate_highest()

def peaks_infection_rate():
    change_file()
    peaks=0
    date_occured=[]
    for i in range(len(df)):
        row = df.iloc[[i]]
        if (row.Rate > df.iloc[[i-1]].Rate).bool() and (row.Rate > df.iloc[[i+1]].Rate).bool() \
                and (row.Indicator == "cumulative_cases").bool():
            peaks += 1
            date_occured.append(df.iloc[i][2])#row[["Date"]])
    print(peaks, date_occured)

#peaks_infection_rate()


def peaks_death_rate():
    change_file()
    peaks = 0
    date_occured=[]
    for i in range(len(df)):
        row = df.iloc[[i]]
        if (row.Rate > df.iloc[[i-1]].Rate).bool() and (row.Rate > df.iloc[[i+1]].Rate).bool() \
                and (row.Indicator == "cumulative_deaths").bool():
            #  above the line, i used a strange character to skip a line and shift things to the next line.
            peaks += 1
            date_occured.append(df.iloc[i][2])
    print(peaks, date_occured)


peaks_death_rate()

#print(df.Deaths_and_cases)
