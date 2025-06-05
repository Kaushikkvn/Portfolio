import streamlit as st
import pandas

st.set_page_config(layout="wide")
col1,col2=st.columns(2)

with col1:
    st.image("images/image.jpeg",width=350)
with (col2):
    st.title("Kaushik Kommineni")
    content="""
    Data-driven Computer Science graduate with strong analytical, 
    technical, and problem-solving skills. 
    Experienced in developing business insights, predictive models, and interactive dashboards. 
    Proficient in Python, SQL, and visualization tools, with proven experience in optimizing data workflows. 
    Seeking a Data Analyst role to leverage my expertise in statistical analysis, data visualization, and machine learning.
    """
    st.info(content)
content2="""
Below you can find some of the apps I have built in python. Feel free to contact me! 
"""
st.write(content2)
col3,empty_col,col4=st.columns([1.5,0.5,1.5])

df=pandas.read_csv("data.csv",sep=";")
with col3:
    for index,row in df[:10].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" +row["image"])
        st.write(f"[Source Code]({row['url']})")

with col4:
    for index,row in df[10:].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" +row["image"])
        st.write(f"[Source Code]({row['url']})")
