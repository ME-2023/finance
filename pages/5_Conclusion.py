import streamlit as st
import pandas as pd
# from sklearn import datasets
from sklearn.ensemble import RandomForestClassifier
import requests
import json
from datetime import datetime
#import seaborn as sns
#import matplotlib.pyplot as plt
import numpy as np


st.write("""
# Conclusion
""")

st.write("""

Our research led us to the choice of a new dataset where there was less 
interference from political factors and allowed an analysis with a more 
stable economic background. For this task, we chose the main companies 
in the fund managed by Warren Buffett and Charlie Münger (recently 
deceased) because they are "buy and hold" investors, who buy and hold 
their positions for very long periods of time, giving the market 
enormous stability. Within this portfolio, we have worked throughout 
this process with the companies Apple and Bank of America.

The results obtained for the target 'days to reach an increase of 10%' 
are found in the tab called 'investment markets'
         
         """)

st.write("")
st.write("")

st.write("_____________________")
st.write("##### MEINPS Project")
st.markdown(''':red[Development of Human Potential]''')
st.markdown('''Powered by :blue[AI]''')