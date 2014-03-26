import nltk
from nltk.tokenize import sent_tokenize
from nltk.tokenize import wordpunct_tokenize
from nltk.classify import NaiveBayesClassifier,DecisionTreeClassifier
from nltk.corpus import movie_reviews
import nltk.data

def words_bag(words):
    return dict([(word,True) for word in words])

neg_list = movie_reviews.fileids('neg')
pos_list = movie_reviews.fileids('pos')
 
negfeats = [(words_bag(movie_reviews.words(fileids=[f])), 'neg') for f in neg_list]
posfeats = [(words_bag(movie_reviews.words(fileids=[f])), 'pos') for f in pos_list]

'''gathering training and test data for decision trees''' 
negcutoff_train_dt = len(negfeats)
poscutoff_train_dt = len(posfeats)
training_data_dt = negfeats[:negcutoff_train_dt] + posfeats[:poscutoff_train_dt]

'''#commenting out the test data code that was used to find error rate
negcutoff_test_dt = len(negfeats)*1/5
poscutoff_test_dt = len(posfeats)*1/5
test_data_dt = negfeats[:negcutoff_test_dt] + posfeats[:poscutoff_test_dt]
'''

classifier_dt = DecisionTreeClassifier.train(training_data_dt)

print "Decision Trees"    
print 'train on %d instances:' % (len(training_data_dt))

sentence_list = []

#comments = "first half was good but oh boy the second was shit, overall good movie. no matter how many times I watch this, I still like it. must watch movie, i just want to touch the sweet panda"
while 1:
    comments = raw_input("Enter a review comment ending with a dot :")
    sentence_list = sent_tokenize(comments)
    for sentence in sentence_list:
        word_punct = wordpunct_tokenize(sentence)
        for words in word_punct:
            input_cl = words_bag(words)
        print sentence + "--->" + classifier_dt.classify(input_cl)
    user_input = raw_input("Do you want to continue? (Y/N) :")
    if user_input == 'N':
        break 

'''#commenting out the test data code that was used to find error rate
#classifier.show_most_informative_features()
accuracy_dt = nltk.classify.accuracy(classifier_dt, test_data_dt)
error_dt = 1 - accuracy_dt
print "error rate of Decision Trees :" + str(error_dt)
'''
