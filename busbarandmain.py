import csv

data_main1 = list()
data_main2 = list()
data_main3 = list()
data_main4 = list()
data_main5 = list()
data_sub1 = list()
data_sub2 = list()
data_sub3 = list()
data_sub4 = list()
data_sub5 = list()

fmain1 = open("D:\busbarandmain\main_data\1.csv",'r')
fmain2 = open("D:\busbarandmain\main_data\2.csv",'r')
fmain3 = open("D:\busbarandmain\main_data\1.csv",'r')
fmain4 = open("D:\busbarandmain\main_data\1.csv",'r')
fmain5 = open("D:\busbarandmain\main_data\1.csv",'r')

fsub1 = open("D:\busbarandmain\sub_data\1.csv",'r')
fsub2 = open("D:\busbarandmain\sub_data\2.csv",'r')
fsub3 = open("D:\busbarandmain\sub_data\3.csv",'r')
fsub4 = open("D:\busbarandmain\sub_data\4.csv",'r')
fsub5 = open("D:\busbarandmain\sub_data\5.csv",'r')

rdata_main1 = csv.reader(fmain1)
rdata_main2 = csv.reader(fmain2)
rdata_main3 = csv.reader(fmain3)
rdata_main4 = csv.reader(fmain4)
rdata_main5 = csv.reader(fmain5)

rdata_sub1 = csv.reader(fsub1)
rdata_sub2 = csv.reader(fsub2)
rdata_sub3 = csv.reader(fsub3)
rdata_sub4 = csv.reader(fsub4)
rdata_sub5 = csv.reader(fsub5)


for row in rdata_main1:
    data_main1.append(row)
fmain1.close
for row in rdata_main2:
    data_main2.append(row)
fmain2.close
for row in rdata_main3:
    data_main3.append(row)
fmain3.close
for row in rdata_main4:
    data_main4.append(row)
fmain4.close
for row in rdata_main5:
    data_main5.append(row)
fmain5.close

for row in rdata_sub1:
    data_sub1.append(row)
fsub1.close
for row in rdata_sub2:
    data_sub2.append(row)
fsub2.close
for row in rdata_sub3:
    data_sub3.append(row)
fsub3.close
for row in rdata_sub4:
    data_sub4.append(row)
fsub4.close
for row in rdata_sub5:
    data_sub5.append(row)
fsub5.close


