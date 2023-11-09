import streamlit as st
import pandas as pd
from sklearn import datasets
from sklearn.ensemble import RandomForestClassifier
import requests
import json
from datetime import datetime

st.write("""
# Medias Móviles Trading App

Esta app predice los resultados de una estrategia de trading!
""")

st.sidebar.header('Modificar parámetros')

def user_input_features():
    global data

    moving_avg = st.sidebar.slider('Media móvil', 10, 100, 50, 10)
    major_trend = st.sidebar.radio('Tendencia de LP', ('bull', 'bear'))

    data = {
        'Media movil': moving_avg,
        'Tendencia de LP': major_trend,

    }
    features = pd.DataFrame(data, index=[0])
    return features

df = user_input_features()

# Read the CSV file
df_apple = pd.read_csv('aapl_1d.csv')

# Now 'df_apple' is a DataFrame containing the data from 'aapl_1d.csv'


st.subheader('Parámetros ingresados por el usuario')
st.write(df)

#st.write(df_apple)

st.write("""
## Precio de cierre (1d)
""")

ma = f"ma-{data['Media movil']}"

st.line_chart(df_apple[['close', ma]])



"""
iris = datasets.load_iris()
X = iris.data
Y = iris.target

clf = RandomForestClassifier()
clf.fit(X, Y)

prediction = clf.predict(df)
prediction_proba = clf.predict_proba(df)

"""

st.subheader('Class labels and their corresponding index number')
#st.write(iris.target_names)

st.subheader('Predicción')
st.write(f"El algoritmo logrará alcanzar un 10% de incremento de precios en X días.")
#st.write(prediction)

st.subheader('Prediction Probability')
st.write(f"La probabilidad de lograrlo será de X %.")
#st.write(prediction_proba)