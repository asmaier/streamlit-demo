import streamlit as st
import pandas_datareader.data as web

f = web.DataReader('^DAX', 'stooq')

f


