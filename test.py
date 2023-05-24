import csv

data_main1 = list()

fmain1 = open("D:\\busbarandmain\main_data\\5.csv",'r')


rdata_main1 = csv.reader(fmain1)

for row in rdata_main1:
    data_main1.append(row)
fmain1.close
data_change = [["0" for j in range(6)] for i in range(132)]
n = 0
i = 1
for row in data_main1:
    
    if(n == 12):
        n = 0
        i += 1

    for x in range(0,6):
        data_change[12*i-n-1][5-x] = row[x]
    n += 1





#print(data)
with open('D:\\busbarandmain\main_data\\change5.csv','w', newline="") as file :

    write = csv.writer(file)
    write.writerows(data_change)



