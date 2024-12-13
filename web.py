import streamlit as st
import pandas as pd
import numpy as np
import altair as alt
import plotly.figure_factory as ff
import matplotlib
matplotlib.use('TkAgg')
matplotlib.get_backend()
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus']=False
st.title("Streamlit Web Example")
option = st.sidebar.selectbox(
    '请在下拉列表选择需要呈现的页面',
    ['Home','Matplotlib','Plotly','Altair'])
st.sidebar.write('You selected:',option)
