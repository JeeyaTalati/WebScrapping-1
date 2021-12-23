import csv
data=[]
with open("NewData.csv","r") as f:
    csvReader=csv.reader(f)
    for row in csvReader:
        data.append(row)

headers=data[0]
planetData=data[1:]
for dataPoints in planetData:
    dataPoints[0].lower()
planetData.sort(key=lambda planetData:planetData[0])
with open("SortedNewData.csv","a+") as f:
    csvWriter=csv.writer(f)
    csvWriter.writerow(headers)
    csvWriter.writerows(planetData)