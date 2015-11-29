# coding:gbk
from numpy import *
import jieba.analyse


def readData(filename):
    dataSet = []
    classSet = []
    with open(filename) as fr:
        title = fr.readline()
        lines = fr.readlines()
    for line in lines:
        str_line = line.strip().split('\t')
        words = jieba.analyse.extract_tags(str_line[1])
        dataSet.append(words)
        classSet.append(str_line[4])
    test = int(len(dataSet)*0.1)
    testData = dataSet[0:test]
    testClass = classSet[0:test]
    trainData =dataSet[test:len(dataSet)]
    trainClass = classSet[test:len(classSet)]
    return testData, testClass, trainData, trainClass


def loadData(filename):
    dataSet = []
    classSet = []
    with open(filename) as fr:
        lines = fr.readlines()
    for line in lines:
        if line != '\n':
            str_line = line.strip().split('\t')
            words = jieba.analyse.extract_tags(str_line[0],5)
            dataSet.append(words)
            classSet.append(str_line[1])
    test = int(len(dataSet)*0.1)
    testData = dataSet[0:test]
    testClass = classSet[0:test]
    trainData =dataSet[test:len(dataSet)]
    trainClass = classSet[test:len(classSet)]
    return testData, testClass, trainData, trainClass

def createVocabList(dataSet): # get a vocabulary list
    vocabSet = set([]) # create an empty set
    for document in dataSet:
        vocabSet = vocabSet | set(document)
    return list(vocabSet)


def setOfWords2Vec(vocabList, inputSet): # get the inputSet's word vector
    returnVec = [0]*len(vocabList)
    for word in inputSet:
        if word in vocabList:
            returnVec[vocabList.index(word)] = 1
    return returnVec


def get_data(vocabList, inputSet, inputclassSet):
    Data = []
    Class = []
    for line in inputSet:
        re_Vec = setOfWords2Vec(vocabList, line)
        Data.append(re_Vec)
    Class.extend(inputclassSet)
    return Data, Class
