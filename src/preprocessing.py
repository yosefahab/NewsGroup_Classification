# lowercase
# email/URL replacement (regex) 
# replace numbers (regex) 
# remove symbols
# remove stopwords
# stemming
# lemmatization

import re
from string import printable
from nltk.stem import SnowballStemmer,LancasterStemmer
from nltk.corpus import stopwords
from textblob import TextBlob, Word
from nltk.corpus import words
from nltk.stem import PorterStemmer
import nltk
import string

def preprocess(dataframe):
    # chain of functions for preprocessing
    lowercase(dataframe)
    replace_email(dataframe)
    remove_symbols(dataframe)
    # remove_strangeChars(dataframe)
    replace_numbers(dataframe)
    # remove_gibberish(dataframe)

    remove_stopWords(dataframe)
    
    # Stemmer(dataframe, PorterStemmer())
    # Stemmer(dataframe, LancasterStemmer())
    # Stemmer(dataframe, SnowballStemmer())
    # porterStemmer(dataframe)
    # snowballStemmer(dataframe)
    # lemmatize(dataframe)

    
def lowercase(dataframe):
    dataframe['Article'] = dataframe['Article'].apply(lambda x: " ".join(x.lower() for x in x.split()))

def replace_email(dataframe):
    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    dataframe['Article'] = dataframe['Article'].apply(lambda x: (re.sub(regex, "emailadd", x)))

def remove_symbols(dataframe):
    # regex = r'[\p{P}\p{S}]'
    # dataframe['Article'] = dataframe['Article'].apply(lambda x: re.sub(regex,"",x))
    regex = r'\W+'
    dataframe['Article'] = dataframe['Article'].apply(lambda x: re.sub(regex," ",x))

def remove_strangeChars(dataframe):
    def checkChars(x):
        for c in x:
            if not c in string.printable:
                return False
        return True

    dataframe['Article'] = dataframe['Article'].apply(lambda x: " ".join(x if checkChars(x) else " "))
  
def replace_numbers(dataframe):
    regex = r'\d+[\.\-\d]*'
    dataframe['Article'] = dataframe['Article'].apply(lambda x: re.sub(regex,"number",x))

def remove_stopWords(dataframe):
    nltk.download('stopwords')
    stop = stopwords.words('english')
    dataframe['Article'] = dataframe['Article'].apply(lambda x: " ".join(x for x in x.split() if x not in stop))

def porterStemmer(dataframe):
    st = PorterStemmer()
    dataframe['Article'] = dataframe['Article'].apply(lambda x: " ".join([st.stem(word) for word in x.split()]))

def Stemmer(dataframe,st):
    dataframe['Article'] = dataframe['Article'].apply(lambda x: " ".join([st.stem(word) for word in x.split()]))

# def snowballStemmer(dataframe):
#     st = SnowballStemmer()
#     dataframe['Article'] = dataframe['Article'].apply(lambda x: " ".join([st.stem(word) for word in x.split()]))

def lemmatize(dataframe):
    dataframe['Article'] = dataframe['Article'].apply(lambda x: " ".join([Word(word).lemmatize() for word in x.split()]))

def remove_gibberish(dataframe):
    nltk.download('words')
    w = set(words.words())
    #w for w in nltk.wordpunct_tokenize(x) 
    dataframe['Article'] = dataframe['Article'].apply(lambda x: x if x in w else " ") 