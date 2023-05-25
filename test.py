import csv

data_main = list()

fmain1 = open("D:\\busbarandmain\main_data\\2.csv",'r')


rdata_main = csv.reader(fmain1)

for row in rdata_main:
    data_main.append(row)
fmain1.close
data_change = [["0" for j in range(6)] for i in range(len(data_main))]
n = 0
i = 1
for row in data_main:
    
    if(n == 12):
        n = 0
        i += 1

    for x in range(0,6):
        data_change[12*i-n-1][5-x] = row[x]
    n += 1





#print(data)
with open('D:\\busbarandmain\main_data\\change7.csv','w', newline="") as file :

    write = csv.writer(file)
    write.writerows(data_change)



