import streamlit as st
import plotly.express as px
import numpy as np
import matplotlip.pyplot as plt

st.title("Data Visualization")

x = np.linspasce(0, 10, 100)
y = np.sin(x)

fig, ax = plt.subplots()
ax.plot(x, y)

st.pyplot(fig)
