# App to compute correlation between two stock symbols.
# Inspired by
# https://algotrading101.com/learn/python-correlation-guide/

import streamlit as st
import pandas as pd
import pandas_datareader.data as web


@st.cache
def get_data_from_stooq(symbol):
    return web.DataReader(symbol, 'stooq')


st.title("Stocky")

first = st.text_input("First stock symbol, e.g. '^DAX'", "^DAX")
second = st.text_input("Second stock symbol, e.g. '^DJI", "^DJI")

df_first = get_data_from_stooq(first)[["Close"]]
df_second = get_data_from_stooq(second)[["Close"]]

df_first = df_first.rename(columns={"Close": first})
df_second = df_second.rename(columns={"Close": second})

col1, col2 = st.columns(2)

with col1:
    st.line_chart(df_first)

with col2:
    st.line_chart(df_second)


df = pd.merge(df_first.pct_change(), df_second.pct_change(), left_index=True, right_index=True)
df = df.rename(columns={first + "_x": first, second + "_y": second})

st.header("Daily change (%)")
st.line_chart(df)

st.header("Correlation")

my_slot = st.empty()
window = st.slider("Rolling window size in days", 5, 365, 50)
df_corr = df[first].rolling(str(window) + "d").corr(df[second])
my_slot.line_chart(df_corr[abs(df_corr) < 0.999])



