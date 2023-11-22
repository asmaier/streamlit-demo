import streamlit as st
from math import sin, cos, sqrt, atan2, radians
import pandas as pd
import requests
from PIL import Image
import numpy as np

st.set_page_config(
    page_title="The blue marble",
    layout="wide",
    initial_sidebar_state="collapsed",
)

st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Quicksand');

    *{
         font-family: 'Quicksand', sans-serif;
     }
</style>
""", unsafe_allow_html=True)

st.title("The blue marble")

def distance(lat1,lon1,lat2,lon2):
    R = 6371.0088
    lat1,lon1,lat2,lon2 = map(np.radians, [lat1,lon1,lat2,lon2])

    dlat = lat2 - lat1
    dlon = lon2 - lon1
    a = np.sin(dlat/2)**2 + np.cos(lat1) * np.cos(lat2) * np.sin(dlon/2) **2
    c = 2 * np.arctan2(a**0.5, (1-a)**0.5)
    return R * c

@st.cache_data
def get_metadata():
    return pd.read_csv("epic_earth_rounded.csv")

df_images = get_metadata()

# lat = 52.531677
# lon = 13.381777

left, center, right = st.columns([0.25,0.5,0.25])
with center:
    if "url" in st.session_state:
        placeholder = st.image(st.session_state["url"], "loading...")
    else:    
        placeholder = center.image("black_background.jpg", "loading...")
with st.sidebar: 
    lat = st.slider("latitude", -90.0,90.0,value=52.531677)
    lon = st.slider("longitude", -180.0,180.0,value=13.381777)

    st.markdown("""

    ### About
    This is an app showing images from earth 
    taken by the [Deep Space Climate Observatory](https://en.wikipedia.org/wiki/Deep_Space_Climate_Observatory)
    positioned at the Lagrange point L1 in a distance of 1,475,207 km
    from earth. It makes use of the [EPIC API](https://epic.gsfc.nasa.gov/about/api).
    
    But in opposition to the NASA app this streamlit demo shows the latest
    image closest to a given lat/lon-position.
    """)

idxmin = df_images.apply(lambda x: distance(lat,lon,x.lat,x.lon), axis=1).idxmin()
image = df_images.iloc[idxmin]

url = "https://epic.gsfc.nasa.gov/archive/natural/" + image["date"].replace("-", "/") + "/jpg/" + image["name"] + ".jpg"

if url:
    # placeholder.image(url)
    placeholder.image(url, image["date"])
    st.session_state["url"] = url








