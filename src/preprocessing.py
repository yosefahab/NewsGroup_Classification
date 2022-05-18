# lowercase
# email/URL replacement (regex) 
# replace numbers (regex) 
# remove symbols
# remove stopwords
# stemming
# lemmatization

import re
import nltk
from nltk.stem import SnowballStemmer,LancasterStemmer,PorterStemmer
from nltk.corpus import stopwords
from textblob import Word

# chain of functions for preprocessing
def preprocess(dataframe):
    # cleaning
    lowercase(dataframe)
    replace_email(dataframe)
    remove_symbols(dataframe)
    replace_numbers(dataframe)
    remove_gibberish(dataframe)
  
    # preprocesing
    remove_stopWords(dataframe)

    # Stemmer(dataframe, PorterStemmer())
    # Stemmer(dataframe, LancasterStemmer())
    Stemmer(dataframe, SnowballStemmer("english"))

    # lemmatize(dataframe)

    
def lowercase(dataframe):
    dataframe['Article'] = dataframe['Article'].apply(lambda x: " ".join(x.lower() for x in x.split()))

def replace_email(dataframe):
    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    dataframe['Article'] = dataframe['Article'].apply(lambda x: (re.sub(regex, "emailadd", x)))

def remove_symbols(dataframe):
    # regex = r'[\p{P}\p{S}]'
    # regex = r'\W+'
    regex = r'[^a-zA-Z0-9]+'
    dataframe['Article'] = dataframe['Article'].apply(lambda x: re.sub(regex," ",x))

def replace_numbers(dataframe):
    regex = r'\d+[\.\-\d]*'
    dataframe['Article'] = dataframe['Article'].apply(lambda x: re.sub(regex,"number",x))

def remove_stopWords(dataframe):
    nltk.download('stopwords')
    stop = stopwords.words('english')
    dataframe['Article'] = dataframe['Article'].apply(lambda x: " ".join(x for x in x.split() if x not in stop))

def Stemmer(dataframe,st):
    dataframe['Article'] = dataframe['Article'].apply(lambda x: " ".join([st.stem(word) for word in x.split()]))

def lemmatize(dataframe):
    dataframe['Article'] = dataframe['Article'].apply(lambda x: " ".join([Word(word).lemmatize() for word in x.split()]))

def remove_gibberish(dataframe):
    nltk.download('words')
    words = set(nltk.corpus.words.words())
    dataframe['Article'] = dataframe['Article'].apply(lambda x: " ".join(w for w in nltk.wordpunct_tokenize(x) if w in words or not w.isalpha()))