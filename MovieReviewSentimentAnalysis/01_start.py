import nltk.classify.util
from nltk.classify import NaiveBayesClassifier
from nltk.corpus import movie_reviews

def word_feats(words):
    return dict([(word, True) for word in words])

def write_file(file_name, list_name) :
    f = open(file_name, "w")
    for i in list_name :
        for j in i :
            #print j
            f.write(j+"\n")

    f.close()

#----------------------------------------------------------------------------------------
negids = movie_reviews.fileids('neg')
posids = movie_reviews.fileids('pos')

#print negids, posids

#neg_words = [movie_reviews.words(fileids=[f]) for f in negids]
pos_words = [movie_reviews.words(fileids=[f]) for f in posids]
#print words

#write_file("nltk_neg_movie_reviews.txt", neg_words)
write_file("nltk_pos_movie_reviews.txt", pos_words)

exit(0)

negfeats = [(word_feats(movie_reviews.words(fileids=[f])), 'neg') for f in negids]
posfeats = [(word_feats(movie_reviews.words(fileids=[f])), 'pos') for f in posids]


classifier = NaiveBayesClassifier.train(negfeats + posfeats)

test_ip = [ ({ 'The' : True,
        'movie' : True,
        'was' : True, 
        'not' : True, 
        'bad' : True

    }), 
    ({ 'The' : True,
        'movie' : True,
        'was' : True, 
        'awesome' : True

    })
]


test = {'love': False, 'deal': False, 'tired': False, 'feel': False, 'is': True, 'am': False, 'an': False, 'sandwich': False, 'ca': False, 'best': True, '!': True, 'what': False, 'i': True, '.': False, 'amazing': False, 'horrible': False, 'sworn': False, 'awesome': False, 'do': False, 'good': False, 'very': False, 'boss': False, 'beers': False, 'not': False, 'with': False, 'he': False, 'enemy': False, 'about': False, 'like': False, 'restaurant': False, 'this': True, 'of': False, 'work': False, "n't": False, 'these': False, 'stuff': False, 'place': False, 'my': False, 'view': False}
#print 'accuracy:', nltk.classify.util.accuracy(classifier, test_ip)
#classifier.show_most_informative_features()


print classifier.classify(test_ip)
'''
x = [ movie_reviews.words(fileids=[f]) for f in negids ]
for i in x[0] : 
    print i
'''
