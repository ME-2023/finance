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
# Medias Móviles Trading App

Esta app predice los resultados de una estrategia de trading!
""")

st.sidebar.header('Modificar parámetros')

def user_input_features():
    global data
    global ticker

    moving_avg = st.sidebar.slider('Media móvil', 10, 100, 50, 10)
    major_trend = st.sidebar.radio('Tendencia de LP', ('bull market', 'bear market'))
    ticker_symbol = st.sidebar.selectbox(
    "Seleccionar ticker",
    ["AAPL", "BAC", "AXP", 
    "CVX", "KO",],
    )

    if ticker_symbol == 'AAPL':
        ticker = 'aapl_1d_3.csv'
    if ticker_symbol == 'BAC':
        ticker = 'bac_1d.csv'
    if ticker_symbol == 'AXP':
        ticker = 'axp_1d.csv'
    if ticker_symbol == 'CVX':
        ticker = 'cvx_1d.csv'
    if ticker_symbol == 'KO':
        ticker = 'ko_1d.csv'

    data = {
        'Ticker': ticker_symbol,
        'Media movil': moving_avg,
        'Tendencia de LP': major_trend,
    }
    features = pd.DataFrame(data, index=[0])
    return features

df = user_input_features()

# Read the CSV file
#df_apple = pd.read_csv('aapl_1d.csv')
df_selected = pd.read_csv(ticker)

# Now 'df_apple' is a DataFrame containing the data from 'aapl_1d.csv'


st.subheader('Parámetros ingresados por el usuario')
st.write(df)

#st.write(df_apple)
st.write(df_selected.head(5))

st.write("""
## Precio de cierre (1d)
""")

ma = f"ma-{data['Media movil']}"

# st.line_chart(df_apple[['close', ma]])

st.line_chart(df_selected[['close', ma]])

st.subheader('Análisis en el período seleccionado')

# Assuming apple_daily['days_to_10'] is your data
#data2 = df_selected['days_to_10']

# Create a histogram
#sns.histplot(data2, kde=False, bins=int(np.sqrt(1454)))

# Use pyplot to generate the plot
#plt.show()

# Use Streamlit's pyplot functionality to display the plot
#st.pyplot(plt)

# iris = datasets.load_iris()
#X = iris.data
#Y = iris.target

#clf = RandomForestClassifier()
#clf.fit(X, Y)

#prediction = clf.predict(df)
#prediction_proba = clf.predict_proba(df)



st.subheader('Class labels and their corresponding index number')
#st.write(iris.target_names)

st.subheader('Predicción')
st.write(f"El algoritmo logrará alcanzar un 10% de incremento de precios en X días.")
#st.write(prediction)

st.subheader('Prediction Probability')
st.write(f"La probabilidad de lograrlo será de X %.")
#st.write(prediction_proba)