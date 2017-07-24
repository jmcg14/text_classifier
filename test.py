import os
import glob
import TextDataSet
from TextDataSet import get_file_cat
import sklearn
from sklearn.naive_bayes import MultinomialNB
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import AdaBoostClassifier
from sklearn.svm import SVC


#def get_file_cat(filename):
#    return filename.split('/')[-2].split('-')[0]


def main():
    arg = '/home/josh/Documents/COSC/projects/ML/datasets/bbc_processed'
    #arg2 = '/home/josh/Documents/COSC/projects/ML/datasets/bbc'

    data = TextDataSet.TextDataSet(arg)

    print "filenames"
    files = data.get_filenames()
    flat_files = [x for y in files for x in y]
    #data_tuples = []
    #for x in flat_files:
        #data_tuples.append((x, data.get_tag(get_file_cat(x))))

    labels = []
    for x in flat_files:
        labels.append(data.get_tag(get_file_cat(x)))



    #print labels
    #print len(flat_files)

    count_vect = CountVectorizer(input=u'filename')
    tf_vect = TfidfVectorizer(input=u'filename')
    features = tf_vect.fit_transform(flat_files)

    print features

    features_train, features_test, labels_train, labels_test = train_test_split(
        features, labels, test_size=0.25, random_state=45)


    print "MultiNomialNB"

    NBclf = MultinomialNB()
    NBclf.fit(features_train, labels_train)
    pred1 = NBclf.predict(features_test)
    acc1 = accuracy_score(labels_test, pred1)

    print acc1

    print '\n'

    print "DecisionTree"

    DTclf = DecisionTreeClassifier(min_samples_split = 20, max_depth = 20)
    DTclf.fit(features_train, labels_train)
    pred2 = DTclf.predict(features_test)
    acc2 = accuracy_score(labels_test, pred2)

    print acc2

    print '\n\n'

    print "SVM"
    SVclf = SVC(C=100.0, kernel='rbf')
    SVclf.fit(features_train, labels_train)
    pred3 = SVclf.predict(features_test)
    acc3 = accuracy_score(labels_test, pred3)

    print acc3

    print '\n\n'

    print "Adaboost"
    ABclf = AdaBoostClassifier(learning_rate=2)
    ABclf.fit(features_train, labels_train)
    pred4 = ABclf.predict(features_test)
    acc4 = accuracy_score(labels_test, pred4)

    print acc4



if __name__ == "__main__":
    main()
