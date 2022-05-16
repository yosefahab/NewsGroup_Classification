# lowercase
# email replacement (regex)
# replace numbers
# remove symbols
# remove stopwords
# stemming
# lemmatization

import pandas as pd
import re

def lowercase(dataframe):
    dataframe['Article'] = dataframe['Article'].apply(lambda x: " ".join(x.lower() for x in x.split()))

def replace_email(dataframe):
    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    regex_2 = r'b[w-.]+?@w+?.w{2,4}b'
    dataframe['Article'] = dataframe['Article'].apply(lambda x: " ".join(re.sub(regex, "emailadd", x)))

def replace_url(dataframe):
    regex = r'(http[s]?S+)|(w+.[A-Za-z]{2,4}S*)'
    dataframe['Article'] = dataframe['Article'].apply(lambda x: " ".join(re.sub(regex, "urladd", x)))

#def remove_symbols(dataframe):
    #regex = r'W+'
    #dataframe['Article'] = dataframe['Article'].apply(lambda x: " ".join())