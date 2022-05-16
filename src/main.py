# Each project will include 4 main requirements:
# 1. Data preprocessing                                 -> preprocessing.py // Abdelrahman Omar, Yousef
# 2. Features extraction.                               -> feature_extraction.py // Seif, Soliman
# 3. Model training and testing                         -> main.py // all ()
# 4. Results visualization.                             -> visualization.py //
# Attention!: Highest project accuracy will be rewarded

# import preprocessing.py
# import feature_extraction.py
# import visualization.py
# import model1.py
# import model2.py

from pathlib import Path
import pandas as pd
import os
import shutil
import random 

# global data # contains main data
global train, y_train
global x_test, y_test 

Paths = {
    "data": r"../Data/20news-18828",# contains subdirectories!
    "data_train": r"../Data/train", # contains subdirectories!
    "data_test": r"../Data/test",   # contains subdirectories!
}
# read data using given path
def load_train():
    train = pd.DataFrame(columns=["Label", "Article"])
    dirs = os.listdir(Paths["data_train"])
    for dir in dirs:
        for file in os.listdir(os.path.join(Paths["data_train"], dir)):
            with open(os.path.join(Paths["data_train"], dir, file)) as f:
                row = pd.DataFrame([{"Label": dir, "Article": f.read()}])
                train = pd.concat([train, row])
    train.to_csv('../Data/train.csv', index=False)

def split_data():
    def splitArticles(label):
        articles = os.listdir(os.path.join(Paths["data"],label))
        random.shuffle(articles)
        articlesTest = articles[:int(len(articles)*0.3)]
        articlesTrain = articles[int(len(articles)*0.3):]
       
        # copy 70% of articles to Data/train
        for i in range(len(articlesTrain)):
            src = os.path.join(Paths["data"],label,articlesTrain[i])
            dest = os.path.join(Paths["data_train"],label)
            if not os.path.isdir(dest):
                os.makedirs(dest)
            shutil.copy2(src,dest)
        # copy 30% of articles to Data/test
        for i in range(len(articlesTest)):
            src = os.path.join(Paths["data"],label,articlesTrain[i])
            dest = os.path.join(Paths["data_test"],label)
            if not os.path.isdir(dest):
                os.makedirs(dest)
            shutil.copy2(src,dest)

    if not os.path.isdir(Paths["data_train"]):
        os.makedirs(Paths["data_train"])
    
    if not os.path.isdir(Paths["data_test"]):
        os.makedirs(Paths["data_test"])

    labels = os.listdir(Paths["data"])
    for label in labels:
        splitArticles(label)

def main():
    #split_data()
    load_train()

if __name__ == "__main__":
    main()