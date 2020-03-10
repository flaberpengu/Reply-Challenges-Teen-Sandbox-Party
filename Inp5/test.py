f = open("test_file.txt")
lines = f.readlines()
sanLines = []
for a in range(len(lines)):
    if lines[a] != "\n":
        lines[a] = lines[a].split(' ')
        if len(lines[a]) > 1:
            for b in range(len(lines[a])):
                lines[a][b] = lines[a][b].strip('\n')
        else:
            lines[a][0] = lines[a][0].strip('\n')
        sanLines.append(lines[a])

#print(sanLines)

count = 0
while count < len(sanLines):
    if sanLines[count] == "\n":
        sanLines.pop(count)
        count -= 1
    else:
        count += 1

numCases = int(str(sanLines[0][0]).strip('\n'))
sanLines.pop(0)

for i in range(numCases):
    indexPos = i*2
    outputString = ""
    beautySum = 0
    for j in range(len(sanLines[indexPos+1])):
        if (int(sanLines[indexPos+1][j]) >= 0):
            beautySum += int(sanLines[indexPos+1][j])
    outputString += "Case #" + str(i+1) + ": " + str(beautySum) + "\n"
    fileOut = open("output_test.txt", "a+")
    fileOut.write(outputString)
    fileOut.close()
