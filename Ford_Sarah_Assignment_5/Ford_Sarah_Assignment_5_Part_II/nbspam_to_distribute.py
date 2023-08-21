#Construct a Spam filter using Naive Bayes Classifier



#Some code for parsing a string into a list of words--removing 'stop words'
#in the process, and converting everything to lower case.  The stopwords list
#is copied from the NLP toolkit for
#Python. You might want to use this to help break lines in the training and
#test files into lists of words.

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
 

#This is part of the pre-processing to clean the data, just to show
#how it was done.  You don't need to include this in the assignment,
#as it has already been executed for you.

#This reads the original data in spam2.csv,
#and produces two files, one ham, one spam, with one message per line.  The
#lines themselves will be purged of punctuation and stop words. 
def clean():
    f=open('spam2.csv','r')
    ham=open('ham_sms.txt','w')
    spam=open('spam_sms.txt','w')
    for s in f:
        start=s.index(',')
        u=s[start+1:]
        ulist=text_process(u)
        if s[:3]=='ham':
            ham.write(" ".join(ulist)+'\n')
        else:
            spam.write(" ".join(ulist)+'\n')
    ham.close()
    spam.close()

#Once again, this is part of the pre-processing , and don't need to include
#this in the assignment,
#as it has already been executed for you.
    
#The ham file has 4827 messages, one per line.  The spam file has 747 messages,
#one per line.  Let's split these in two, making a training file and a test file
#for each class of messages.

def separate():
    f=open('ham_sms.txt','r')
    g1=open('ham_sms_training','w')
    g2=open('ham_sms_test','w')
    for j in range(2413):
        s=f.readline()
        g1.write(s)
    for j in range(2414):
        s=f.readline()
        g2.write(s)
    g1.close()
    g2.close()
    f=open('spam_sms.txt','r')
    g1=open('spam_sms_training','w')
    g2=open('spam_sms_test','w')
    for j in range(373):
        s=f.readline()
        g1.write(s)
    for j in range(374):
        s=f.readline()
        g2.write(s)
    g1.close()
    g2.close()

#Build the bags of words; we need to do both
#at the same time to get the total vocabulary count.
#The function should return a 2-tuple of Python dictionaries.
#In each dictionary, a key value pair has a word as a key
#and its smoothed probability (or rather the logarithm of
#the smoothed probability) as the value.

    
def build_models():
    x=0
    
#The message is a string that has already been
#parsed into non-stop words, such as one of the lines
#of the training or test files.  The model is a dictionary
#modeling a class, as returned by build_model. prior is
#the prior probability of membership in the class
    
def score(msg,model,prior):
    x=0


#Now evaluate the classifier. Do 1000 trials or randomly selecting
#a message from the entire test corpus  (2414 ham messages, 374 spam).
#Score each message to classify it as ham or spam.  Print out four
#values--the proportion of ham messages correctly identified as ham,
#misidentified as spam, and the proportion of spam messages correctly
#identified as spam, and misidentified as ham:
    
def evaluate():
    x=0

                      
    
    


    
    
