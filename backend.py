# -*- coding: utf-8 -*-
"""
Created on Fri Oct 28 15:31:00 2022

@author: ludov
"""

import streamlit as st
from supabase import create_client, Client
import pandas as pd

############################# CONNECTION FUNCTION ###########################
def init_connection():
    url = st.secrets["supabase_url"]
    key = st.secrets["supabase_key"]
    return create_client(url, key)
#############################################################################

############################### LOGIN FUNCTION ##############################
def login(supabase_conn, username, password):
    rows = supabase_conn.table("Users").select("*").execute()
    for row in rows.data:
        if username == row["Username"] and password == row["Password"]:
            return True
    return False
##############################################################################

############################## SIGNIN FUNCTION ###############################
def signin(supabase_conn, username, password, mail):
    #check if username or password or mail are empty or contains only whitespaced
    if username == "" or ' ' in username or password == "" or ' ' in password or mail == "" or ' ' in mail:
        return False

    rows = supabase_conn.table("Users").select("*").execute()
    for row in rows.data:
        if username == row["Username"]:
            return False

    supabase_conn.table("Users").insert({"Username":username , "Password":password, "Mail":mail}).execute()
    return True
##############################################################################


############################ PRINT DATAFRAME FUNC ############################
def get_Database_dataFrame(supabase_conn):
    return pd.DataFrame(supabase_conn.table("Messages").select("*").execute().data)
##############################################################################
