import streamlit as st
import pandas as pd

st.tile("Gioi thieu data")
df = pd.read_csv("animals.csv")

st.write(df)