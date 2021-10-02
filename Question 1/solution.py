import csv

inputFile = r"..\input\question-1\main.csv"

rows = []
headers = []
with open(inputFile, 'r') as ipFile:
    inputReader = csv.reader(ipFile)
    headers = next(inputReader)
    for row in inputReader:
        rows.append(row)
headers = headers[:2] + headers[3:]
headers[0] = ""


for i in range(len(rows)):
    rowValues = []
    for j in range(len(rows[i])):
        if not j == 2:
            rowValues.append(int(rows[i][j]))
    rows[i] = rowValues
id = 0
outputRows = []
for row in rows:
    if id == 0:
        outputRows.append(row)
    else:
        for j in range(len(row[1:])):
            outputRows[-1][j+1] += row[j+1]
    id = (id + 1) % 10


outputFile = r"..\output\answer-1\main.csv"
with open(outputFile, 'w') as opFile:
    outputWriter = csv.writer(opFile)
    outputWriter.writerow(headers)
    outputWriter.writerows(outputRows)
