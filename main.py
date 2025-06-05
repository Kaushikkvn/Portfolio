import streamlit as st
from PIL.ImageFont import Layout

st.set_page_config(layout="wide")
col1,col2=st.columns(2)

with col1:
    st.image("images/image.jpeg",width=350)
with col2:
    st.title("Kaushik Kommineni")
    content="""
    Data-driven Computer Science graduate with strong analytical, 
    technical, and problem-solving skills. 
    Experienced in developing business insights, predictive models, and interactive dashboards. 
    Proficient in Python, SQL, and visualization tools, with proven experience in optimizing data workflows. 
    Seeking a Data Analyst role to leverage my expertise in statistical analysis, data visualization, and machine learning.
    """
    st.info(content)