import streamlit as st
import pandas as pd
import requests
import json
from datetime import datetime
# import yfinance as yf

# Current date
current_date2 = datetime.today().strftime('%Y-%m-%d')
current_date2 = str(current_date2)


st.write("# MEINPS Finance")
st.write("## Data Science Web App")
st.write("### :green[SPECULATION]")

st.write("""
    ## Argentina and the limits of Data Analytics
    
    The Argentine economy has been suffering from a marked inflationary process for many 
    years. If we only look at the quantitative indicators of the market, we can come 
    to assume that the economy is in a marked process of growth, when its reality is 
    precisely the opposite.
    
    """)


try:
    st.write(f"Connecting API.")




except:
    st.write(f"No se puedo conectar a la API.")


st.write("")
st.write("")

st.write("_____________________")
st.write("##### MEINPS Project")
st.markdown(''':red[Development of Human Potential]''')
st.markdown('''Powered by :blue[AI]''')