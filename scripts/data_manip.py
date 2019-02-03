import os
import pandas as pd

DEFAULT_DATA_PATH = os.path.abspath(
    os.path.join(__file__, '..', '..', '..', 'Kaggle-NMA-Competition\\data'))

def load_train_data(path_data=DEFAULT_DATA_PATH):
    post=pd.read_csv(os.path.join(path_data,"train\\post.csv"))
    thread=pd.read_csv(os.path.join(path_data,"train\\thread.csv"))
    return post, thread

def load_test_data(path_data=DEFAULT_DATA_PATH):
    post=pd.read_csv(os.path.join(path_data,"test\\post.csv"))
    thread=pd.read_csv(os.path.join(path_data,"test\\thread.csv"))
    return post, thread

def load_label_map(path_data=DEFAULT_DATA_PATH):
    label_map = pd.read_csv(os.path.join(path_data,'label_map.csv'), index_col="type_name")
    return label_map
