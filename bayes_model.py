import sklearn.naive_bayes
from sklearn.naive_bayes import GaussianNB
from sklearn.naive_bayes import BernoulliNB
from sklearn import tree
from sklearn import svm

def bayes(train_set, train_class):
    clf = sklearn.naive_bayes.MultinomialNB()
    clf.fit(train_set, train_class)
    return clf


def gaussianBayes(train_set, train_class):
    clf = GaussianNB()
    clf.fit(train_set, train_class)
    return clf


def bernoulliBayes(train_set, train_class):
    clf = BernoulliNB(train_set, train_class)
    clf.fit(train_set, train_class)
    return clf

def treeClassification(train_set, train_class):
    clf = tree.DecisionTreeClassifier()
    clf.fit(train_set, train_class)
    return clf


def svmClassification(train_set, train_class):
    clf = svm.SVC()
    clf.fit(train_set, train_class)
    return clf
