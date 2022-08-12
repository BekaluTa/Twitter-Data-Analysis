import pandas as pd
import pandas as pd
import numpy as np
import psycopg2
from sqlalchemy import create_engine
import psycopg2.extras as extras
import time


df=pd.read_csv('processed_tweet_data.csv')
print("Data Loaded")

conn=psycopg2.connect(database='twitter-analysis',user='postgres',host='localhost',port='5432',password='1234')
print("database Connected")
cursor=conn.cursor()
conn.autocommit=True

cursor.execute("DROP TABLE IF EXISTS Twitter")


#Creating Tables
sql='''CREATE Table Twitter 
(created_at text NOT NULL,
source text,
original_text text,
polarity int,
subjectivity int,
lang text,
favourite_count int,
retweet_count int,
original_author text,
followers_count int,
friends_count int,
possibly_sensitive text,
hashtags text,
user_mentions text,
place text)'''

print("Tabele Created")

insert_query_execute_val = f"""insert into Twitter(created_at,source,original_text,polarity,subjectivity,lang,favourite_count
,retweet_count,original_author,followers_count,friends_count,possibly_sensitive,hashtags,user_mentions,place
                    ) 
                    values %s """
                    
psycopg2.extras.execute_values(cursor, insert_query_execute_val, df.values)

print("CSV Loaded into Database Table")
