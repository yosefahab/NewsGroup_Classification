# Each project will include 4 main requirements:
# 1. Data preprocessing                                 -> preprocessing.py // Abdelrahman Omar, Badr
# 2. Features extraction.                               -> feature_extraction.py // Seif, 
# 3. Model training and testing                         -> main.py // all
# 4. Results visualization.                             -> visualization.py //
# Attention!: Highest project accuracy will be rewarded

# import preprocessing.py
# import feature_extraction.py
# import visualization.py
# import model1.py
# import model2.py

import pandas as pd

global data # contains main data
global x_train, y_train
global x_test, y_test 

Paths = {
    "data": r"../Data/20news-18828",# contains subdirectories!
    "data_train": r"../Data/train", # contains subdirectories!
    "data_test": r"../Data/test",   # contains subdirectories!
}
# read data using given path
def read_data(path):
    data = pd.read_csv(path,sep='\s+').astype(int)
    return data

def main():
    pass

if __name__ == "__main__":
    main()