import streamlit as st
import numpy as np
import pandas as pd
from sklearn import datasets


def app():
    st.title('Dashoard to Visualize Data')

    st.write("This is the Dashborad for data page of the multi-page app.")

    st.write("The following is the DataFrame of the `Africa twitter` dataset.")
    number = st.number_input("Enter the number of rows and press enter: ", min_value=None, max_value=None, value=0,
                             step=None, format=None, key=None, help=None, on_change=None, args=None, kwargs=None, disabled=False)
    df = pd.read_csv('./processed_tweet_data.csv', nrows=number)



    st.write(df)