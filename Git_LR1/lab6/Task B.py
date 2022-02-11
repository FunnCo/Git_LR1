a = int(input())
b = int(input())
k = int(input())

listOfRows = []
currentCount = 1
currentNum = 1
for i in range(b):
    row = ""
    for j in range(1, currentCount+1):
        row += str(currentNum) + " "
        currentNum += 1
    row = row[:-1]
    listOfRows.append(row)
    currentCount += 1

for i in range(len(listOfRows)):
    tempRow = list(listOfRows[i].split(' '))
    for j in range(k):
        tempRow[j] = int(tempRow[j])
    listOfRows[i] = tempRow


print(listOfRows)
