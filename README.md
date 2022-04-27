# Directories
## src/
Contains all .py files we'll be using.

## Backup/
Contains .tar files of original data

## Data/
/20news-18828 : raw document data with no cross-posts and only "From" and "Subject" headers (18828 documents)
 

<br>

# Definitions 
## Indexed Data Format: 
- The .data files are formatted "**docIdx** **wordIdx** **count**".
- The .label files are simply a list of label id's.
- The .map files map from label id's to label names.

    **docIdx** : which document contained this word instance.<br>
    **wordIdx** : Index of word in this document instance.<br>
    **count** : count of this word's instance in this docIdx<br>

<br>

# Src files
- **main**: driver code for the entire project
- **preprocessing**: contains all functions used to do preprocessing on data
- **feature_extraction**: contains functions that will extract features from data
- **model1.py**: contains logic for the 1st model
- **model2.py**: contains logic for the 2nd model
- **visualization**: contains functions which will be used to visualize results