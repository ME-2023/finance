import streamlit as st
import pandas as pd
import requests
import json
from datetime import datetime
# import yfinance as yf
from sklearn.ensemble import RandomForestClassifier
import requests
import json
from datetime import datetime
#import seaborn as sns
#import matplotlib.pyplot as plt
import numpy as np

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
    merval_ars = 'merval_ars.csv'
    merval_usd = 'merval_usd.csv'

    df_merval_ars = pd.read_csv(merval_ars)
    df_merval_usd = pd.read_csv(merval_usd)

    st.write('### Caso of study')

    st.write('##### From: 2010-02-22 to: 2023-04-20')

    st.write("""
    ### Merval - USD
    """)  
    st.line_chart(df_merval_usd[['id', 'cierre']])

    st.write("""
    ### Merval - ARS
    """)
    st.line_chart(df_merval_ars[['id', 'MERVAL']])

    st.write("### Business analysis")
    st.write("""
    ...
    ...
    ...
    """)

except:
    st.write(f"No API connection.")

st.write("")
st.write("")

st.write("_____________________")
st.write("##### MEINPS Project")
st.markdown(''':red[Development of Human Potential]''')
st.markdown('''Powered by :blue[AI]''')






