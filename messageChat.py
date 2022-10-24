import streamlit as st
#import numpy as np
#import statistics as stat
import pandas as pd
#from streamlit_chat import message as st_message
from streamlit_chat import message

st.title("Chat")

df_users= pd.read_csv('C:/Users/ludov/Desktop/Chet_users.csv', sep=';')

with st.sidebar:
    st.title("Members")
    for x in df_users.iloc[:,0]:
        st.write(x)

def utente():
    st.session_state["userID"]
message(message=st.text_input("Message:"))


