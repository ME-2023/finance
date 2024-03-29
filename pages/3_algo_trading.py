import streamlit as st
import pandas as pd
import requests
import json
from datetime import datetime
# import yfinance as yf

# Current date
current_date = datetime.today().strftime('%Y-%m-%d')
current_date = str(current_date)

# SIDEBAR
# Interactive Streamlit elements, like these sliders, return their value.
# This gives you an extremely simple interaction model.
st.sidebar.header('Modify parameters')
investment = st.sidebar.slider("Investmet (US$)", 100, 10000, 1000, 100)
commiss = st.sidebar.slider("Taxes (%)", 0.0, 4.0, 0.65)
taxes = st.sidebar.slider("Financial rent tax (%)", 0, 50, 15)

st.write("""
    ## Algorithmic trading
    
    Companies that make up the Merval index and are listed on the
    US stock market (ADRs).
                
    """)

#ticker_symbol = 'YPF'
ticker_symbol = st.selectbox(
    "Seleccionar ticker",
    ["BBAR", "BMA", "CEPU", 
    "CRESY", "EDN", "GGAL",
    "LOMA", "PAM", "SUPV", 
    "TGS", "TX", "YPF"],
    )

st.write(f"Selected ticker: {ticker_symbol}")
st.write(f'From: 2018-01-09 to: {current_date}')

try:
    # Authentication
    # Pass your API key in the query string like follows:
    api_url = f'https://api.polygon.io/v2/aggs/ticker/{ticker_symbol}/range/1/day/2018-01-09/{current_date}?apiKey=LOpAdL70TOrSPQh9t3UaYAFpr2Dq34po'

    # Login, para generar un token
    # Un token es un identificador único que se le da al usuario para poder realizar las solicitudes necesarias

    response = requests.get(api_url)
    consulta=response.json()

    df = pd.DataFrame.from_dict(consulta)
    df_normalized = pd.json_normalize(df['results'])
    df_normalized = df_normalized.rename(columns={'c': 'close', 'o': 'open', 'h': 'high', 'l':'low', 'v': 'volume'})
    df_normalized['ma-10'] = df_normalized['close'].rolling(window=10).mean()
    df_normalized['ma-10'] = df_normalized['ma-10'].fillna(df_normalized['close'])

    st.write("""
    ## Close (1d)
    """)
    st.line_chart(df_normalized.close)
except:
    st.write(f"No API connection.")


st.write(f"## Algorithmic Trading for 10 days moving average")

money = investment
stocks = {'BBAR': 0, 'BMA': 0, 'CEPU': 0, 'CRESY': 0, 'EDN': 0,
            'GGAL': 0,'LOMA': 0,'PAM': 0,'SUPV': 0,
            'TGS': 0,'TX': 0,'YPF': 0}
total_commissions = 0

def buy_c(stock, close):
    global money
    global total_commissions
    global commiss
    if money >= close and close > 0:
        n_shares = round(money / close)
        commission = (close * n_shares) * (commiss / 100)
        money -= (close * n_shares) - commission
        stocks[stock] += n_shares
        total_commissions += commission

def sell_c(stock, close):
    global money
    global total_commissions
    global commiss
    commission = (stocks[stock] * close) * (commiss / 100)
    money += (stocks[stock] * close) - commission
    stocks[stock] = 0
    total_commissions += commission

# Valor inicial de la variable
position = False

def algo_trading3(df):
    global position
    for index, row in df.iterrows():
        if row['close'] > row['ma-10']:
            if position == False:
                c = round(row.close, 2)
                position = True
                buy_c(ticker_symbol, row.close)

        elif row['close'] < row['ma-10']:
            if position == True:
                c = round(row.close, 2)
                position = False
                sell_c(ticker_symbol, row.close)

try:
    algo_trading3(df_normalized)

    taxes = money * taxes / 100
    money -= taxes

    st.write(f"Initial investment: $ {investment}.")
    #st.write(f"Stocks: {stocks}.")
    st.write(f"Money in account: $ {round(money, 2)}.")
    st.write(f"Amount of money paid in commissions: $ {round(total_commissions, 2)}")
    st.write(f"ADRs: They pay 15% Cedular tax on financial income but not Personal Assets: $ {round(taxes, 2)}")
    st.write(f"(Dividends have not been included, although they pay taxes.)")
except:
    st.write(f"There was a connection failure. Refresh the page.")

st.write("")
st.write("")

st.write("_____________________")
st.write("##### MEINPS Project")
st.markdown(''':red[Development of Human Potential]''')
st.markdown('''Powered by :blue[AI]''')