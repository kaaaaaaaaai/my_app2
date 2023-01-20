import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

def plot_func(a, b, c):
    x = np.linspace(-10, 10, 100)
    y = a*x**2 + b*x + c
    plt.plot(x, y)
    plt.show()

st.title("Function Plotter")

a = st.sidebar.slider("a", -10.0, 10.0, 1.0)
b = st.sidebar.slider("b", -10.0, 10.0, 2.0)
c = st.sidebar.slider("c", -10.0, 10.0, 1.0)

st.write("y = a*x^2 + b*x + c")

if st.button("Plot"):
    plot_func(a, b, c)