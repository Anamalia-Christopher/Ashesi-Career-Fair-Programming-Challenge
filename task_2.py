import csv
import sys
import datetime

start = datetime.datetime.now()
path1 = sys.argv[-2]
path2 = sys.argv[-1]


file_complex = open(path1, newline='')
reader_complex = csv.reader(file_complex)
dataset_complex = [row for row in reader_complex]

number_row_complex = len(dataset_complex)


file_1 = open(path2, encoding='utf-8-sig')
reader_1 = csv.reader(file_1)
dataset_1 = [row for row in reader_1]



values_list = []

for i in range(len(dataset_complex)):
    if [(dataset_complex[i][4])] in dataset_1:
        values_list.append(dataset_complex[i])



final = []
counter = 0
b=len(dataset_1)

keep_track = 0
for i in range(len(values_list)):

    if [values_list[i][4]] == dataset_1[keep_track]:
        keep_track += 1
        final.append(values_list[i])
    if keep_track == len(dataset_1):
        break
country_confirmer=[]
locality_confirmer=[]
indicator_confirmer= []

for i in final:

    country_confirmer.append(i[0])
    locality_confirmer.append(i[1])
    indicator_confirmer.append(i[2])


def mode(a):
    dic = {}
    for i in a:
        if i in dic:
            dic[i] = dic[i] + 1
        else:
            dic[i] = 1
    mode = max(dic.values())

    nmode = []
    for item in dic:
        if dic[item] == mode:
            nmode.append(item)
    return nmode

def correct_date_detector():
    for i in values_list:

        if i[0] == mode(country_confirmer)[0] and i[1]==mode(locality_confirmer)[0] and i[2]==mode(indicator_confirmer)[0] and [i[4]] == dataset_1[0]:

            return i[3]


stop = datetime.datetime.now()


time = stop-start
answers = open("task2_result-sample_partial_time_series.txt", "w")
answers.write(mode(country_confirmer)[0] + ' ' + mode(locality_confirmer)[0]+"\n")
answers.write(mode(indicator_confirmer)[0]+"\n")
answers.write(correct_date_detector()+"\n")
answers.write(str(time.microseconds/1000))