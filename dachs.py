import streamlit as st
import pandas_datareader.data as web
import seaborn as sns
import io

f = web.DataReader('^DAX', 'stooq')

# IDE says: "Statement seems to have no effect"
# But in fact this generates a table view of the dataframe
# in streamlit
f

dax = f[["Close"]]

col1, col2 = st.beta_columns(2)

with col1:
    # it is not yet possible to center the content
    st.write(dax.describe())

with col2:
    # By default info() does only return None
    # So we need some workaround to display the output
    # see https://stackoverflow.com/questions/39440253/how-to-return-a-string-from-pandas-dataframe-info
    buf = io.StringIO()
    dax.info(buf=buf, verbose=True)
    st.text(buf.getvalue())


st.line_chart(dax)

# How to work with pandas inbuilt plotting.
# It needs optional pandas dependency matplotlib
# One has to select the property ".figure" from the pandas
# output
st.pyplot(dax.plot().figure)

# hist returns a numpy array of subplots
# we need to select the first one
hist = dax.hist(bins=100)
st.pyplot(hist[0, 0].figure)

# we can also use seaborne
# set_theme will globally change the layout of matplotlib plots
sns.set_theme()

st.pyplot(sns.relplot(data=dax, kind="line"))


st.pyplot(sns.pairplot(data=f[["Close", "Volume"]], markers="+", kind="reg", diag_kind="kde"))

# dow
f = web.DataReader('^DJI', 'stooq')
dow = f[["Close"]]

daxdow = dax.merge(dow, left_index=True, right_index=True, suffixes=('_dax', '_dow'))

st.pyplot(sns.pairplot(data=daxdow, markers="+", kind="reg", diag_kind="kde"))


