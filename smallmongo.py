import streamlit as st
from pymongo import MongoClient

@st.experimental_singleton(suppress_st_warning=True)
def init_connection():
    return MongoClient("mongodb+srv://st.secrets.db_username:st.secrets.db_pswd@st.secrets.cluster_name.n4ycr4f.mongodb.net/?retryWrites=true&w=majority")

client = init_connection()

@st.experimental_memo(ttl=60)
def get_data():
    db = client.sample_guides #establish connection to the 'sample_guide' db
    items = db.small.find() # return all result from the 'planets' collection
    items = list(items)        
    return items
data = get_data()

for item in data:
    st.write(f"{data['name']} is the {data['orderFromSun']} from the sun")