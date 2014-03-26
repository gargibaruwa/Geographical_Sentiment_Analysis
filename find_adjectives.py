import nltk
from nltk.tokenize import sent_tokenize
from nltk.tokenize import wordpunct_tokenize
from nltk.classify import NaiveBayesClassifier,DecisionTreeClassifier
from nltk.corpus import movie_reviews
import nltk.data

def words_bag(words):
    return dict([(word,True) for word in words])

#classifier = nltk.data.load('classifiers/movie_reviews_NaiveBayes.pickle')
neg_list = movie_reviews.fileids('neg')
pos_list = movie_reviews.fileids('pos')
 
negfeats = [(words_bag(movie_reviews.words(fileids=[f])), 'neg') for f in neg_list]
posfeats = [(words_bag(movie_reviews.words(fileids=[f])), 'pos') for f in pos_list]
 
negcutoff_train = len(negfeats)
poscutoff_train = len(posfeats)

#negcutoff_test = len(negfeats)*3/4
#poscutoff_test = len(posfeats)*3/4

training_data = negfeats[:negcutoff_train] + posfeats[:poscutoff_train]
#print str(training_data)
training_data = str(training_data).replace("True", " ")
training_data = str(training_data).replace("'", " ")
training_data = str(training_data).replace(":", " ")
training_data = str(training_data).replace(",", " ")

text = nltk.word_tokenize(str(training_data))
#print str(training_data)
b = nltk.pos_tag(text)

file_save = open("C:/Users/Gargi/Desktop/COURSES/Data mining/PROJECT/Final DM Project/wordcloud/tagged_file.txt", 'a')
for word_tag in b:
    tag = word_tag[1]
    if str(tag) == 'JJ':
        file_save.write(str(word_tag[0]))
        file_save.write(str("\n"))

#print b
'''
for word_tag in b:
    tag = word_tag[1]
    if str(tag) == 'JJ':
        print word_tag[0]
'''
        
'''
i = 0
a = []
for line in training_data:  #nltk.corpus.movie_reviews.words():
    print str(line) + "\n"
''' 
    

#print a
'''
file_write = open("C:/Users/Gargi/Desktop/COURSES/Data mining/PROJECT/Final DM Project/tagged_file", 'a')
b = nltk.pos_tag(a)
for word_tag in b:
    tag = word_tag[1]
    if str(tag) == 'JJ':
        file_write.write(str(word_tag[0]))
        file_write.write(str("\n"))

file_write.close()
'''
