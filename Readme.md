# Streamlit Demos [![Open in Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://asmaier-streamlit-demo-errorbars-ndntyu.streamlitapp.com/)

This is a repository holding some demo code 
for the https://www.streamlit.io/ framework. 

## 1. Stocky

It's main application is the `Stocky` app. 
It computes the correlation of the percentage 
change of two stock market symbols over a 
rolling time window (between 5 and 365 days).

The stock market data is updated automatically.
It is retrieved with the help 
of [pandas-datareader](https://github.com/pydata/pandas-datareader) 
from https://stooq.com/ . 

To access the app navigate to

https://asmaier-streamlit-demo-stocky-99iqsj.streamlitapp.com/

## 2. Understanding error bars

This is a small educational application which aims 
to help it's readers to get a better understanding 
of the meaning of error bars. 

To access the app navigate to

https://asmaier-streamlit-demo-errorbars-ndntyu.streamlitapp.com/


# Development Notes 
To generate the `requirements.txt` file from 
the `Pipfile` do the following:

    pipenv lock --requirements > requirements.txt

