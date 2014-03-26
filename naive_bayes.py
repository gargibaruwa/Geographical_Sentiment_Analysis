import nltk
from nltk.tokenize import sent_tokenize
from nltk.tokenize import wordpunct_tokenize
from nltk.classify import NaiveBayesClassifier,DecisionTreeClassifier
from nltk.corpus import movie_reviews
import nltk.data
import nltk.metrics
import collections

def words_bag(words):
    return dict([(word,True) for word in words])

neg_list = movie_reviews.fileids('neg')
pos_list = movie_reviews.fileids('pos')
 
negfeats = [(words_bag(movie_reviews.words(fileids=[f])), 'neg') for f in neg_list]
posfeats = [(words_bag(movie_reviews.words(fileids=[f])), 'pos') for f in pos_list]

'''gathering training and test data for naive bayes''' 
negcutoff_train = len(negfeats)
poscutoff_train = len(posfeats)
training_data = negfeats[:negcutoff_train] + posfeats[:poscutoff_train]

'''#commenting out the test data code that was used to find error rate'''
negcutoff_test = len(negfeats)
poscutoff_test = len(posfeats)
test_data = negfeats[:negcutoff_test] + posfeats[:poscutoff_test]


classifier_nb = NaiveBayesClassifier.train(training_data)
refsets = collections.defaultdict(set)
testsets = collections.defaultdict(set)

print "Naive Bayes"
print 'train on %d instances:' % (len(training_data))

'''
sentence_list = []

while 1:
    comments = raw_input("Enter a review comment ending with a dot :")
    sentence_list = sent_tokenize(comments)    
    for sentence in sentence_list:
        word_punct = wordpunct_tokenize(sentence)
        for words in word_punct:
            input_cl = words_bag(words)
        print sentence + "--->" + classifier_nb.classify(input_cl)
    user_input = raw_input("Do you want to continue? (Y/N) :")
    if user_input == 'N':
        break

'''
#classifier.show_most_informative_features()
'''#commenting out the test data code that was used to find error rate'''
accuracy_nb = nltk.classify.accuracy(classifier_nb, test_data)
error_nb = 1 - accuracy_nb
print "error rate of naive bayes :" + str(error_nb)

pos_precision = nltk.metrics.precision(refsets['pos'],refsets['pos'])
print pos_precision


