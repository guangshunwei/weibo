import creatData

testData, testClass, trainData, trainClass = creatData.readData('suicide.txt')
for line in trainData:
    for i in line:
        print i
