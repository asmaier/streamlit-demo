# Stocky

This is a repository holding some demo code 
for the https://www.streamlit.io/ framework. 

It's main application is the `Stocky` app. 
It computes the correlation of the percentage 
change of two stock market symbols over a 
rolling time window (between 5 and 365 days).

The stock market data is updated automatically.
It is retrieved with the help 
of [pandas-datareader](https://github.com/pydata/pandas-datareader) 
from https://stooq.com/ . 

# Development Notes 
To generate the `requirements.txt` file from 
the `Pipfile` do the following:

    pipenv lock --requirements > requirements.txt

