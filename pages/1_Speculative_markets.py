import streamlit as st
import pandas as pd
import requests
import json
from datetime import datetime
# import yfinance as yf

# Current date
current_date = datetime.today().strftime('%Y-%m-%d')
current_date = str(current_date)


st.write("# MEINPS Finance")
st.write("## Data Science Web App")
st.write("### :green[SPECULATIVE MARKETS]")

st.write("""
    ## Argentina: Merval index
    
    Companies that make up the Merval index and are listed on the U.S. Stock Exchange(ADRs)
                
    """)

#ticker_symbol = 'YPF'
ticker_symbol = st.selectbox(
    "Seleccionar ticker",
    ["BBAR", "BMA", "CEPU", 
    "CRESY", "EDN", "GGAL",
    "LOMA", "PAM", "SUPV", 
    "TGS", "TX", "YPF"],
    )

st.write(f"You selected: {ticker_symbol}")
st.write(f'From: 2018-01-09 to: {current_date}')

try:
    # Authentication
    # Pass your API key in the query string like follows:
    api_url = f'https://api.polygon.io/v2/aggs/ticker/{ticker_symbol}/range/1/day/2018-01-09/{current_date}?apiKey=LOpAdL70TOrSPQh9t3UaYAFpr2Dq34po'

    # Login, para generar un token
    # Un token es un identificador único que se le da al usuario para poder realizar las solicitudes necesarias

    response = requests.get(api_url)
    consulta=response.json()

    df_ypf = pd.DataFrame.from_dict(consulta)
    df_normalized = pd.json_normalize(df_ypf['results'])
    df_normalized = df_normalized.rename(columns={'c': 'close', 'o': 'open', 'h': 'high', 'l':'low', 'v': 'volume'})

    st.write("""
    ## Close (1d)
    """)
    st.line_chart(df_normalized.close)
    st.write("""
    ## Volume
    """)
    st.line_chart(df_normalized.volume)

except:
    st.write(f"No se puedo conectar a la API.")

st.write("")
st.write("")

st.write("_____________________")
st.write("##### MEINPS Project")
st.markdown(''':red[Development of Human Potential]''')
st.markdown('''Powered by :blue[AI]''')