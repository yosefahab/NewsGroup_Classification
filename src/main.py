# Each project will include 4 main requirements:
# 1. Data preprocessing                                 -> preprocessing.py
# 2. Features extraction.                               -> feature_extraction.py
# 3. Model training and testing                         -> main.py
# 4. Results visualization.                             -> visualization.py
# Attention!: Highest project accuracy will be rewarded

# import preprocessing.py
# import feature_extraction.py
# import visualization.py
# import model1.py
# import model2.py

import pandas as pd

Paths = {
    "data": r"../Data",
    "raw_data_train": r"../Data/20news-bydate-unprocessed/20news-bydate-train", # subdirectories!
    "raw_data_test": r"../Data/20news-bydate-unprocessed/20news-bydate-test",   # subdirectories!
    "indexed_data": r"../Data/20news-bydate/matlab", # .data, .label, .map, vocabulary.txt (tab separated files)
}
# read data using given path
def read_data(path):
    data = pd.read_csv(path,sep='\s+').astype(int)
    return data

def main():
    print(read_data(Paths["indexed_data"]+"/test.data"))
    pass

if __name__ == "__main__":
    main()