import streamlit as st
#import numpy as np
#import statistics as stat
import pandas as pd
#from streamlit_chat import message as st_message
from streamlit_chat import message
from datetime import datetime
import backend as be
from streamlit_autorefresh import st_autorefresh

# funzione da invocare all'inizio per creare connessione al database
supabase=be.init_connection()

#funzione da invocare per far si che la pagina si aggiorni ogni 1000 millisecondi
#(così le azioni come la stampa dei messaggi vedono i database aggiornati)
st_autorefresh(inerval=1000, key="dataframerefresh")

st.set_page_config(layout="centered")
st.markdown("""
<style>
.big-font {
    font-size:80px !important;
}
</style>
""", unsafe_allow_html=True)

st.markdown('<p class="big-font">Chat </p>', unsafe_allow_html=True)

df_users= pd.read_csv('C:/Users/ludov/Desktop/Chet_users.csv', sep=';')

with st.sidebar:
    st.title("Members")
    for x in df_users.iloc[:,0]:
        st.write(x)
st.session_state['Message'] = st.text_input("Message")
button =st.button("Send message")
if button: 
    #quando viene premuto il tasto invia messaggio deve essere invocata la funzione send message e successivamente svuotato st.session_state['Message']
    #come qui
    be.send_message (supabase, st.session_state['Message'], st.session_state['Username'], str(datetime.now().strftime(" %H:%M:%S")))
    st.session_state['Message'] = ""


df= be.get_Database_dataFrame(supabase)
for x in range(len(df.index)):
    message(message=(df.iloc[[x]].to_string( index=False, header=False)))
    
    
