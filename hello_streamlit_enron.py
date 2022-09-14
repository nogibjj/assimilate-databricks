"""

streamlit run hello_streamlit_enron.py --server.enableCORS=false
"""

import streamlit as st
from dblib.enron import pandas_load_enron

dataframe = pandas_load_enron()
st.table(dataframe.head())