# Each project will include 4 main requirements:
# 1. Data preprocessing                                 -> preprocessing.py
# 2. Features extraction.                               -> feature_extraction.py
# 3. Model training and testing                         -> main.py
# 4. Results visualization.                             -> visualization.py
# Attention!: Highest project accuracy will be rewarded

from pathlib import Path
from preprocessing import preprocess
from sklearn import preprocessing
# from model1 import linear
# from model2 import naive, naive_bayes
from sklearn.metrics import accuracy_score

from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn import model_selection, preprocessing, linear_model, naive_bayes, metrics

import pandas as pd
import os

Paths = {
    "data": r"../Data/20news-18828",  # contains subdirectories!
    "data_train": r"../Data/train",  # contains subdirectories!
    "data_test": r"../Data/test",  # contains subdirectories!
}


def load_data(path):
    data = pd.DataFrame(columns=["Label", "Article"])
    dirs = os.listdir(path)
    for dir in dirs:
        for file in os.listdir(os.path.join(path, dir)):
            with open(os.path.join(path, dir, file)) as f:
                row = pd.DataFrame([{"Label": dir, "Article": f.read()}])
                data = pd.concat([data, row])
    return data


def read_data(path):
    dataframe = load_data(path)
    dataframe = dataframe.sample(frac=1, random_state=45).reset_index()

    return dataframe


def train_model(classifier, feature_vector_train, label, feature_vector_valid,
                valid_y):
    # fit the training dataset on the classifier
    classifier.fit(feature_vector_train, label)
    # predict the labels on validation dataset
    predictions = classifier.predict(feature_vector_valid)
    return metrics.accuracy_score(predictions, valid_y)


def main():
    # df = read_data(Paths["data"])
    df = pd.read_csv("../Data/data.csv")
    # df = df.sample(frac=1, random_state=1).reset_index()

    # df.to_csv("../Data/data.csv", index=False)

    preprocess(df)

    train_x, valid_x, ytrain, ytest = model_selection.train_test_split(
        df['Article'], df['Label'])

    encoder = preprocessing.LabelEncoder()
    ytrain = encoder.fit_transform(ytrain)
    ytest = encoder.fit_transform(ytest)

    tfidf_vect = TfidfVectorizer(analyzer='word', token_pattern=r'\w+')
    tfidf_vect.fit(df['Article'])
    xtrain = tfidf_vect.transform(train_x)
    xtest = tfidf_vect.transform(valid_x)

    accuracy = train_model(naive_bayes.MultinomialNB(alpha=1e-10), xtrain,
                           ytrain, xtest, ytest)
    print("Accuracy: ", accuracy)
    accuracy = train_model(linear_model.LogisticRegression(max_iter=1000),
                           xtrain, ytrain, xtest, ytest)
    print("Accuracy: ", accuracy)


if __name__ == "__main__":
    main()