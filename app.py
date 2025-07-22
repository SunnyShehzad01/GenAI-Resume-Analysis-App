from dotenv import load_dotenv
load_dotenv() # Load the local variables
import streamlit as st
from pdf import process_pdf
from analysis import analyse_profile

# Create the frontend
st.header("Scan my CV.ai 📝", divider='green')
st.subheader('Tips for using the application')
notes = f""" 
1. Upload the resume (PDF Only)
2. Paste the **Job description**
3. Unleash the power of LLMs to derive insights about your resume.
"""

st.write(notes)

# Side bar
st.sidebar.title('Scan my CV.ai')
#st.sidebar.subheader('Upload the Resume 📝')
pdf_doc = st.sidebar.file_uploader(label='Upload the resume', type=['pdf'])
st.sidebar.write('Created by @SunnyShehzad')

# Main page - Job Description
st.subheader('Enter the Job Description', divider=True)
job_desc = st.text_area(label='Enter the Job Description:', max_chars=10000)
submit = st.button(label='Get AI Powered Insights')

if submit:
    st.markdown(analyse_profile(pdf_doc=pdf_doc, job_desc=job_desc))
    