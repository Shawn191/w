import pandas as pd
import streamlit as st
import plotly.express as px
from PIL import Image

st.set_page_config(page_title='Plastic Pollution Data Visualisations')
st.title("Earthlly")
st.header("How much plastic does the world produce?")
st.caption(
    "The chart shows the increase of global plastic production, measured in tonnes per year, from 1950 through to 2015.")
st.caption(
    "In 1950 the world produced only 2 million tonnes per year. Since then, annual production has increased nearly 200-fold, reaching 381 million tonnes in 2015. For context, this is roughly equivalent to the mass of two-thirds of the world population.")
st.caption(
    "The short downturn in annual production in 2009 and 2010 was predominantly the result of the 2008 global financial crisis — a similar dent is seen across several metrics of resource production and consumption, including energy.")

if st.checkbox('Show Global Plastic Production Graph'):
    csv_file = "global-plastics-production.csv"
    df = pd.read_csv(csv_file)
    st.line_chart(df)

st.header("Cumulative production")
st.caption("How much plastic has the world produced cumulatively?\nThe chart shows that by 2015, the world had produced 7.8 billion tonnes of plastic — more than one tonne of plastic for every person alive today.")

if st.checkbox('Show Cumulative Plastic Production Graph'):
    csv_file = "cumulative-global-plastics.csv"
    df = pd.read_csv(csv_file)
    st.line_chart(df)

hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

