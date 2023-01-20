import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.title("Function Grapher")

# Get user input for the function
fn_string = st.text_input("Enter a function (y = f(x))", "x**2")

# Create a graph
x = np.linspace(-10, 10, num=100)
y = eval(fn_string)
plt.plot(x, y)
plt.xlabel("x")
plt.ylabel("y")
st.pyplot()