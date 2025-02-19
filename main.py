import streamlit as st
import pandas as pd

st.set_page_config(layout='wide')
col1, col2 = st.columns(2)

with col1:
    st.image('images/photo.png', width=275)

career_summary = """
As a seasoned Data Science professional with 16 years of comprehensive experience, 
I, Manoj Sharma, bring extensive expertise in transforming complex data challenges into 
actionable business solutions. My certification from the prestigious Indian School of Business, 
Hyderabad, underpins my technical proficiency across the entire data science spectrum.\n
I graduated in 2008 with a Master in Business & Administration from Indian Institute of 
Planning & Management, New Delhi with major in Finance followed by Advanced Management 
Professional in Business Analytics certification in 2018 from Indian School of Business, 
Hyderabad.\n
My core competencies span Data Analysis, Financial Analytics, and cutting-edge Artificial Intelligence 
applications. I specialize in building end-to-end data solutions, from robust Data 
Engineering pipelines to production-ready MLOps implementations. My experience extends to 
developing sophisticated Business Intelligence frameworks and pioneering Generative AI applications 
that drive innovation and business value.\n
Throughout my career, I have consistently leveraged diverse tools and advanced techniques to deliver scalable 
solutions that bridge the gap between technical complexity and business objectives. My approach combines 
analytical rigor with practical implementation, ensuring sustainable and impactful results.
"""

with col2:
    st.title("Manoj Sharma")
    st.info(career_summary)

content2 = """
Below are some of my projects I have worked on achieving diverse
     technical competencies. Please fee free to contact me!
"""
st.write(content2)

col3, col4 = st.columns(2)
df = pd.read_csv('data.csv', sep=";")

with col3:
    for idx, row in df[:10].iterrows():
        st.header(row['title'])


with col4:
    for idx, row in df[10:].iterrows():
        st.header(row['title'])