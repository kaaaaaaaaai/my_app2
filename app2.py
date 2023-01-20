import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

def plot_line(m, b):
    x = np.linspace(-10, 10, 100)
    y = m*x + b
    plt.plot(x, y)
    plt.show()

st.title("Linear Function Plotter")
m = st.slider("m", -10.0, 10.0, 0.5)
b = st.slider("b", -10.0, 10.0, 0)

if st.button("Plot"):
    plot_line(m, b)