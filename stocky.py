# App to compute correlation between two stock symbols.
# Inspired by
# https://algotrading101.com/learn/python-correlation-guide/

import streamlit as st
import pandas as pd
import pandas_datareader.data as web

st.title("Stocky")

first = st.text_input("First stock symbol, e.g. '^DAX'", "^DAX")
second = st.text_input("Second stock symbol, e.g. '^DJI", "^DJI")

df_first = web.DataReader(first, 'stooq')[["Close"]]
df_second = web.DataReader(second, 'stooq')[["Close"]]

df_first = df_first.rename(columns={"Close": first})
df_second = df_second.rename(columns={"Close": second})

col1, col2 = st.beta_columns(2)

with col1:
    st.line_chart(df_first)

with col2:
    st.line_chart(df_second)


df = pd.merge(df_first.pct_change(), df_second.pct_change(), left_index=True, right_index=True)
df = df.rename(columns={first + "_x": first, second + "_y": second})

st.header("Daily change (%)")
st.line_chart(df)

days = len(df.index)
correlations = []
while days > 0:
    df_temp = df.head(days)
    correlation = df_temp[first].corr(df_temp[second])

    correlations.append((days, correlation))

    days = days-1

df_corr = pd.DataFrame(correlations, columns=["days", "correlation"])
df_corr = df_corr.set_index("days")

st.header("Correlation in the last X days")
st.line_chart(df_corr.head(n=-5))

correlations = []
while days < len(df.index):
    correlation = df[first].corr(df[second].shift(-days))

    # st.write(correlation)

    correlations.append((days, correlation))

    days = days + 1

df_corr = pd.DataFrame(correlations, columns=["days", "correlation"])
df_corr = df_corr.set_index("days")
# df_corr = df_corr.head(n=-5)

st.header("Correlation second symbol X days behind first symbol")
st.line_chart(df_corr.head(n=100))



