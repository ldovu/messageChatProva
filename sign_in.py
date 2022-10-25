# -*- coding: utf-8 -*-
"""
Created on Tue Oct 25 21:51:50 2022

@author: ludov
"""
import streamlit as st


st.title("Sign in")
col1, col2 = st.columns(2)
with col1: 
    user = st.text_input("Username")

with col2:
    st.title("")
    st.title("")
    st.write("")
    
    if st.checkbox('Hide password'):
        with col1: st.text_input("Password", max_chars=(30),
                      type="password")
    else:
        with col1: st.text_input("Password", max_chars=(30))
        
st.button(label='Submit')




