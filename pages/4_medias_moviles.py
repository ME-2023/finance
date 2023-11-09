import streamlit as st
import pandas as pd
from sklearn import datasets
from sklearn.ensemble import RandomForestClassifier

st.write("""
# Medias Móviles Trading App

Esta app predice los resultados de una estrategia de trading!
""")

st.sidebar.header('Modificar parámetros')

def user_input_features():
    moving_avg = st.sidebar.slider('Media móvil', 10, 100, 10, 10)
    major_trend = st.sidebar.radio('Tendencia de LP', ('bull', 'bear'))

    data = {
        'Media móvil': moving_avg,
        'Tendencia de LP': major_trend,

    }
    features = pd.DataFrame(data, index=[0])
    return features

df = user_input_features()

st.subheader('Parámetros ingresados por el usuario')
st.write(df)

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