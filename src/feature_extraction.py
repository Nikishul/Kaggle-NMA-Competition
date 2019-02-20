import pandas as pd
import numpy as np


def get_unique_users(post):
    return post.groupby(['thread_num','user'],sort=False).size().reset_index('user').rename(index=str, columns={0: "number_of_posts"})
def avg_and_dev_in_posts_number(df):
    return df.groupby("thread_num",sort=False).mean(), df.groupby("thread_num",sort=False).std()
def normalize(s):
    return (s-s.mean())/s.max()




def get_quotes_data(post):
    quotes_data=post[["thread_num","quotes"]]
    a=quotes_data.groupby("thread_num",sort=False).size()
    b=quotes_data[quotes_data["quotes"]!=''].groupby("thread_num",sort=False).size()
    numb_quotes=pd.Series(index=a.index)
    for index,item in a.items():
        if index in b.index:
            numb_quotes[index]=b.loc[index]
        else:
            numb_quotes[index]=0
    q_perc=(numb_quotes/a).as_matrix()
    numb_quotes=normalize(numb_quotes.astype(int).as_matrix())

    return numb_quotes, q_perc

	
	
def get_features(post, thread, train_data_features):
	unique_users = get_unique_users(post)
	numb_unique=unique_users.groupby("thread_num",sort=False).nunique()["user"]
	numb_unique= normalize(numb_unique)

	avg_numb_of_posts, dev_numb_of_posts = avg_and_dev_in_posts_number(unique_users[["number_of_posts"]])
	numb_quotes, q_perc=get_quotes_data(post)
	number_posts=thread["thread_replies"].as_matrix()
	number_posts=normalize(number_train_posts)
	train_data_features=np.concatenate([number_train_posts.reshape(-1,1), numb_unique.as_matrix().reshape(-1,1),
                                     numb_quotes.reshape(-1,1),q_perc.reshape(-1,1),
                                     avg_numb_of_posts.as_matrix().reshape(-1,1),train_data_features],axis=1)
	return train_data_features