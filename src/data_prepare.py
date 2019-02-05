import os
import pandas as pd
import re
from bs4 import BeautifulSoup
from nltk.corpus import stopwords

DEFAULT_DATA_PATH = os.path.abspath(
    os.path.join(__file__, '..', '..','data'))

def quote_str_to_list(txt):
    return BeautifulSoup(txt, "lxml").get_text()
	
	
def load_train_data(path_data=DEFAULT_DATA_PATH):
	post=pd.read_csv(os.path.join(path_data,"train\\post.csv"))
	thread=pd.read_csv(os.path.join(path_data,"train\\thread.csv"))
	post['quotes'] = post['quotes'].apply(quote_str_to_list)
	return post, thread

def load_test_data(path_data=DEFAULT_DATA_PATH):
	post=pd.read_csv(os.path.join(path_data,"test\\post.csv"))
	thread=pd.read_csv(os.path.join(path_data,"test\\thread.csv"))
	post['quotes'] = post['quotes'].apply(quote_str_to_list)
	return post, thread

def load_label_map(path_data=DEFAULT_DATA_PATH):
    label_map = pd.read_csv(os.path.join(path_data,'label_map.csv'), index_col="type_name")
    return label_map

def clean(raw_data):
    review_text = BeautifulSoup(raw_data).get_text() 
    letters_only = re.sub("[^a-zA-Z]", " ", review_text) 
    words = letters_only.lower().split()                             
    stops = set(stopwords.words("english"))  
    meaningful_words = [w for w in words if not w in stops]   
    return( " ".join( meaningful_words))
