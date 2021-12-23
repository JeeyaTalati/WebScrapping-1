import csv
DataSet1=[]
DataSet2=[]
final_exoPlanet_data=[]
headers=[]
with open("final.csv","r") as f:
    csvReader=csv.reader(f)
    for row in csvReader:
        DataSet1.append(row)
with open("SortedNewData.csv","r") as f:
    csvReader=csv.reader(f)
    for row in csvReader:
        DataSet2.append(row)

headers.append(DataSet1[0]+DataSet2[0])
planetDataSet1=DataSet1[1:]
planetDataSet2=DataSet2[1:]

for index,data in enumerate(planetDataSet1):
    final_exoPlanet_data.append(planetDataSet1[index]+planetDataSet2[index])
with open("FinalData.csv", "w") as f:
        csvwriter = csv.writer(f)
        csvwriter.writerow(headers)
        csvwriter.writerows(final_exoPlanet_data)

