import string
from collections import Counter
import math
import random

def text_process(text):
    stopwords={'ourselves', 'hers', 'between', 'yourself', 'but', 'again',\
       'there', 'about', 'once', 'during', 'out', 'very', 'having',\
       'with', 'they', 'own', 'an', 'be', 'some', 'for', 'do', 'its',\
       'yours', 'such', 'into', 'of', 'most', 'itself', 'other',\
       'off', 'is', 's', 'am', 'or', 'who', 'as', 'from', 'him', \
       'each', 'the', 'themselves', 'until', 'below', 'are', 'we', \
       'these', 'your', 'his', 'through', 'don', 'nor', 'me', 'were',\
       'her', 'more', 'himself', 'this', 'down', 'should', 'our', 'their',\
       'while', 'above', 'both', 'up', 'to', 'ours', 'had', 'she', 'all',\
       'no', 'when', 'at', 'any', 'before', 'them', 'same', 'and', 'been',\
       'have', 'in', 'will', 'on', 'does', 'yourselves', 'then', 'that',\
       'because', 'what', 'over', 'why', 'so', 'can', 'did', 'not', 'now',\
       'under', 'he', 'you', 'herself', 'has', 'just', 'where', 'too',\
       'only', 'myself', 'which', 'those', 'i', 'after', 'few', 'whom',\
       't', 'being', 'if', 'theirs', 'my', 'against', 'a', 'by', 'doing',\
       'it', 'how', 'further', 'was', 'here', 'than'}
    text = text.translate(string.maketrans('', ''), string.punctuation)
    #print text
    text = [word.lower() for word in text.split() if word.lower() not in stopwords]
    return text


# Creates a list of all the words in the ham training file
def ham_word_list():
    s=[]
    for line in ham:
        for word in text_process(line):
            s.append(word)
    return s

# Creates a list of all the words in the spam training file
def spam_word_list():
    s=[]
    for line in spam:
        for word in text_process(line):
            s.append(word)
    return s


# Creates a list of all the messages in the spam test file
def spam_test_list():
    s = []
    spam_test = open('spam_sms_test','r')
    
    for line in spam_test:
        s.append(line)

    return s

# Creates a list of all the messages in the ham test file
def ham_test_list():
    h = []
    ham_test = open('ham_sms_test','r')

    for line in ham_test:
        h.append(line)

    return h


# Creates a list of all the messages in the spam test and ham test files combined
def master_test_list():
    s = spam_test_list()
    h = ham_test_list()
    m = s + h

    return m


# Builds a dictionary of word frequency for both the spam and ham training files
# Returns both dictionaries
def build_models():
    x = spam_word_list()
    x_length = len(x)
    y = ham_word_list()
    y_length = len(y)

    global c
    c = Counter(x)
    global c_len
    c_len = len(c)
    for word in c:
        c[word]+=1
    for word in y:
        if word not in c:
            c[word]=1

    #print c['prize']
    #print "Number of unique words in both sets combined: ", len(c)
    #print "Number of total words in spam: ", x_length

    for word in c:
        c[word] = float(c[word]) / (x_length + len(c))

    #print "The smoothed probability is: ", c['prize']

    ###################

    global s
    s = Counter(y)
    global s_len
    s_len = len(s)
    for word in y:
        s[word]+=1
    for word in x:
        if word not in s:
            s[word]=1

    #print s['prize']
    #print "Number of unique words in both sets combined: ", len(s)
    #print "Number of total words in ham: ", y_length

    for word in s:
        s[word] = float(s[word]) / (y_length + len(s))

    #print "The smoothed probability is: ", s['prize']

    return c, s


# Returns a spam score given a msg and prior

def spam_score(msg,prior):
    spam_sum = 0
    for word in text_process(msg):
        if word in c:
            spam_sum += math.log(c[word])

    return spam_sum + math.log(prior)

# Returns a ham score given a msg and prior

def ham_score(msg,prior):
    ham_sum = 0
    for word in text_process(msg):
        if word in s:
            ham_sum += math.log(s[word])
        
    return ham_sum + math.log(prior)

# Returns either a spam or ham score given a msg, model, and prior

def score(msg,model,prior):
    if model == "spam":
        return spam_score(msg,prior)
    else:
        return ham_score(msg,prior)


# Selects 1000 random messages from the comined spam and ham test files and
# evaluates the proportion of times our model, based on our calculated scores,
# correctly guessed the message type
def evaluate():
    spam_prob = 0.134
    ham_prob = 0.866
    s = spam_test_list()
    h = ham_test_list()
    spam_right = 0
    ham_right = 0
    spam_wrong = 0
    ham_wrong = 0
    for x in range(0,1001):
        m = master_test_list()
        index = len(m)-1
        rand_int = random.randint(0,index)
        msg = m[rand_int]
        if msg in s:
            correct_ans = "spam"
        elif msg in h:
            correct_ans = "ham"

        spam_score = score(msg,"spam",spam_prob)
        ham_score = score(msg,"ham",ham_prob)

        if spam_score > ham_score:
            guess = "spam"

        elif ham_score > spam_score:
            guess = "ham"

        
        if correct_ans == "spam":
            if guess == correct_ans:
                spam_right+=1
            else:
                spam_wrong+=1

        elif correct_ans == "ham":
            if guess == correct_ans:
                ham_right+=1
            else:
                ham_wrong+=1

    print "Number of spam messages correctly classified is: ",spam_right
    print "Number of spam messages incorrectly classified is: ",spam_wrong
    print "Number of ham messages correctly classified is: ",ham_right
    print "Number of ham messages incorrectly classified is: ",ham_wrong
    print
    print "The percentage of spam messages correctly classified is: ",((float(spam_right))/(spam_right+spam_wrong))*100,"%"
    print "The percentage of ham messages correctly classified is: ",((float(ham_right))/(ham_right + ham_wrong))*100,"%"
    return ""
##################################################### MAIN

ham = open('ham_sms_training','r')
spam = open('spam_sms_training','r')


build_models()

print evaluate()
