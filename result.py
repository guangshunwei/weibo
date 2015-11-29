# coding:gbk
import bayes_model
import creatData
import datetime

start = datetime.datetime.now()

def merge_data():
    testData1, testClass1, trainData1, trainClass1 = creatData.readData('suicide.txt')
    testData2, testClass2, trainData2, trainClass2 = creatData.readData('non_suicide.txt')
    trainData1.extend(trainData2)
    trainClass1.extend(trainClass2)
    testData1.extend(testData2)
    testClass1.extend(testClass2)
    return testData1, testClass1, trainData1, trainClass1

def merge_load_data():
    testData1, testClass1, trainData1, trainClass1 = creatData.loadData('10point.txt')
    testData2, testClass2, trainData2, trainClass2 = creatData.loadData('50point.txt')
    trainData1.extend(trainData2)
    trainClass1.extend(trainClass2)
    testData1.extend(testData2)
    testClass1.extend(testClass2)
    return testData1, testClass1, trainData1, trainClass1


testData, testClass, trainData, trainClass = merge_load_data()
print len(testClass) + len(trainClass)
vocabulary = creatData.createVocabList(trainData)
print len(vocabulary)
train_set, train_class = creatData.get_data(vocabulary, trainData, trainClass)
test_set, test_class = creatData.get_data(vocabulary, testData, testClass)

model = bayes_model.bayes(train_set, train_class) # get the model
# model = bayes_model.gaussianBayes(train_set,train_class)
# model = bayes_model.bernoulliBayes(train_set, train_class)
# model = bayes_model.treeClassification(train_set, train_class)
# model = bayes_model.svmClassification(train_set, train_class)


erro = 0
count =len(test_set)
for i in range(len(test_set)):
    result = model.predict(test_set[i])
    if result == '10':
        print 'the %dth result is: %s' %(i, 'bad')
    else:
        print 'the %dth result is: %s' %(i, 'good')
    if result != test_class[i]:
        erro += 1
erro_rate = erro / float(count)
print 'the erro rate is: %f' % erro_rate
end = datetime.datetime.now()

print 'spend time: '
print (end -start).seconds
