import creatData
def merge_data():
    testData1, testClass1, trainData1, trainClass1 = creatData.readData('suicide.txt')
    testData2, testClass2, trainData2, trainClass2 = creatData.readData('non_suicide.txt')
    trainData1.extend(trainData2)
    trainClass1.extend(trainClass2)
    testData1.extend(testData2)
    testClass1.extend(testClass2)
    return testData1, testClass1, trainData1, trainClass1

testData, testClass, trainData, trainClass = merge_data()
vocabulary = creatData.createVocabList(trainData)
train_set, train_class = creatData.get_data(vocabulary, trainData, trainClass)
test_set, test_class = creatData.get_data(vocabulary, testData, testClass)
print len(test_set[0])+1
with open('E:/machine learning/data/train.data','w') as fw:
    for i in range(len(train_set)):
        for d in train_set[i]:
            fw.write(str(d))
            fw.write(',')
        fw.write(train_class[i])
        fw.write('\n')

with open('E:/machine learning/data/test.data','w') as fw:
    for i in range(len(test_set)):
        for w in test_set[i]:
            fw.write(str(w))
            fw.write(',')
        fw.write(test_class[i])
        fw.write('\n')