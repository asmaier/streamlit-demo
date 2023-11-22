# Streamlit Demos [![Open in Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://asmaier-streamlit-demo-errorbars-pxypmq.streamlitapp.com/)

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

https://asmaier-streamlit-demo-stocky-e8ty0w.streamlit.app/

## 2. Understanding error bars

This is a small educational application which aims 
to help it's readers to get a better understanding 
of the meaning of error bars. 

To access the app navigate to

https://errorbars.streamlit.app/

## 3. The blue marble

This is an app showing images from earth 
taken by the [Deep Space Climate Observatory](https://en.wikipedia.org/wiki/Deep_Space_Climate_Observatory)
positioned at the Lagrange point L1 in a distance of 1,475,207 km
from earth. It makes use of the [EPIC API](https://epic.gsfc.nasa.gov/about/api).

But in opposition to the NASA app this streamlit demo shows the latest
image closest to a given lat/lon-position.

To access the app navigate to

https://blue-marble.streamlit.app/


