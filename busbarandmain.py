import csv

def TMX_HeadA_DataChange(spathinput):
    data_main = list()
    fmain = open(spathinput,'r')
    rdata_main = csv.reader(fmain)

    for row in rdata_main:
        data_main.append(row)
    fmain.close
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
    spathout = input("set file name: ")
    with open("D:\\busbarandmain\main_data\\" + spathout,'w', newline="") as file :

        write = csv.writer(file)
        write.writerows(data_change)

TMX_HeadA_DataChange("D:\\busbarandmain\main_data\\2.csv")


