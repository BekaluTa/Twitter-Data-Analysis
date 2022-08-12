import psycopg2
import pandas as pd

import streamlit as st

data=pd.read_csv('')
# creating Database connectivity with Postgresql

conn=psycopg2.connect(database='twitter-analysis',user='postgres',host='localhost',port='5432',password='1234')
#Creating Cursoer Enviroment

cursor=conn.cursor()
conn.autocommit=True

#checking the existance of table in the Database

# check the existance of Table Challenege before Creating
cursor.execute("DROP TABLE IF EXISTS Twitter")

#Creating Tables
sql='''CREATE Table challenege 
(name CHAR(20) NOT NULL,
id int,
education CHAR(20),
Sex CHAR(20))'''

# Excuting Queires
cursor.execute(sql)
print("table Created Scuessfully")


#inserting Data in to Datbase Table
insert_query_execute_val = f"""insert into Twitter(Region, 
                    Population,
                    Males Population
                    ) 
                    values %s """
                    
psycopg2.extras.execute_values(cursor, insert_query_execute_val, data.values)

# Data is Pandas Variable

print("Data Loadeded Sucessfully")