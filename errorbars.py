
# "For anyone willing to justify the “science” in their data science job title,
# learning when and how to use error bars is inevitable."
# https://towardsdatascience.com/the-quick-and-easy-way-to-plot-error-bars-in-python-using-pandas-a4d5cca2695d
import streamlit as st
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt
from matplotlib.transforms import Affine2D

st.title("Understanding error bars")
st.subheader("[Andreas Maier](https://maierandi.com)")
st.markdown("""
Although often neglected (e.g. weather forecasts), 
uncertainty in results is customarily represented by error bars. 
But despite their common usage in science, a lot of misconceptions
persist about their relation to statistical significance. 
Especially these question are less trivial than most people including
scientists think: "If two error bars 
overlap, does that mean the difference in the results is not 
significant?" and "If two error bars don't overlap, does that mean 
the difference in the results is significant?"
 
The answer to both question is: "It depends." It depends on many things.
First and foremost there a three scores which are commonly used to
compute and visualize an error bar: the standard deviation (std), 
the standard error of the mean (sem) and the 95% confidence interval (ci95). 

To get a feeling how these different types of error bars relate to statistical 
significance we developed an interactive chart showing the relation between
the overlap of the different types of error bars and the statistical significance
in form of the p-value. The chart shows two samples with different mean 
(default value: 10 and 11) and the same standard deviation (std=1.0). 
For each sample all three types of error bars are plotted. With the sliders 
you can change the difference in the means and the sample size. This will 
influence the p-value. In addition you can also change the confidence level
(default value: 95%) for the computation of the confidence interval.  

Your tasks are:
 
1. Try and find the p-value where one of the error bars (std, sem or ci) 
touch each over just barely. 
2. Try and find the confidence level, where the sem and ci error bar have the same size.
3. For a p-value of 0.05, try and find the confidence level, 
where the ci error bar touch each over. 

The chances are high, that you will be surprised by the answers, which are 
listed below the chart. 

""")

mean_diff = st.slider("Difference of means", 0.0, 3.0, 1.0)
sample_size = st.slider("Sample size", 2, 100, 10)
c_level = st.slider("Confidence level (%)", 1, 100, 95)

sample_mean = 10.0
sample_std = 1.0

sample_sem = sample_std/np.sqrt(sample_size)

# see https://stackoverflow.com/questions/15033511/compute-a-confidence-interval-from-sample-data
sample_ci = stats.t.interval(c_level / 100, sample_size - 1, scale=sample_sem)[1]


sample_2_mean = sample_mean + mean_diff
sample_2_std = sample_std
sample_2_size = sample_size
sample_2_sem = sample_sem
sample_2_ci_95 = sample_ci

# Calculate the T-test for the means of two independent samples
# This test assumes both samples are gaussian distributed,
# have the same sample size and have the same variance/standard deviation
p_value = stats.ttest_ind_from_stats(
    sample_mean, sample_std, sample_size,
    sample_2_mean, sample_std, sample_size)[1]


x = ["std", "sem", "ci"]
y1 = [sample_mean, sample_mean, sample_mean]
y2 = [sample_2_mean, sample_2_mean, sample_2_mean]
yerr1 = [sample_std, sample_sem, sample_ci]
yerr2 = [sample_2_std, sample_2_sem, sample_2_ci_95]

fig, ax = plt.subplots()
fig.suptitle(f"p-value: {p_value:.5f}")
ax.axis(ymin=8.9, ymax=13.1)
# see https://stackoverflow.com/questions/58009069/how-to-avoid-overlapping-error-bars-in-matplotlib
trans1 = Affine2D().translate(-0.1, 0.0) + ax.transData
trans2 = Affine2D().translate(+0.1, 0.0) + ax.transData
err1 = ax.errorbar(x, y1, yerr=yerr1, fmt='o', capsize=5, transform=trans1)
err2 = ax.errorbar(x, y2, yerr=yerr2, fmt='o', capsize=5, transform=trans2)


st.pyplot(fig)

with st.expander("Answers"):
    st.subheader("Answer 1")
    st.table({"error bar": ["std", "sem", "ci95"], "p-value": [0.0003, 0.17, 0.005]})
    st.subheader("Answer 2")
    st.markdown("SEM and CI error bar have the same size for a confidence level of 68% (for large sample sizes).")
    st.subheader("Answer 3")
    st.markdown("For a p-value of 0.05 the CI error bars touch each other at a confidence level of 83%")

    st.markdown("""The answers might come to a surprise for many. It therefor seems, that none of 
    the commonly used error bars are intuitive. To improve the situation scientists must stop using the commonly used
    error bars (std, sem and ci95). 
    Instead we all should adopt the convention to show the CI error bars with the confidence level 
    at the desired level of significance (e.g. 83% for p=0.05). """)


st.header("References")
st.markdown("""
- https://www.nature.com/articles/nmeth.2659
- https://chris-said.io/2014/12/01/independent-t-tests-and-the-83-confidence-interval-a-useful-trick-for-eyeballing-your-data/
""")
