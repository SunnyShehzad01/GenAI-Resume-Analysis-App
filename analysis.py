import google.generativeai as genai
from pdf import process_pdf
import os
import streamlit as st
from dotenv import load_dotenv
load_dotenv()

# Configure genai and model
genai.configure(api_key=os.getenv("google_api_key"))

model = genai.GenerativeModel(model_name='gemini-1.5-flash')

def analyse_profile(job_desc, pdf_doc):
    if pdf_doc is not None:
        pdf = process_pdf(pdf_doc)
        st.sidebar.markdown('Upload Success ✅')
    else:
        st.warning("Upload the resume")

    good_fit=model.generate_content(f"Compare the {job_desc} and the resume {pdf}\
                                    and suggest am i a good fit for the role in the job description ?")
    ats_score=model.generate_content(f"Compare the {job_desc} with the resume {pdf}\
                                      and suggest the ATS Score of the Resume")
    prob=model.generate_content(f"Compare the {job_desc} with the resume {pdf}\
                                      and suggest the probability of getting selected in percentage")
    swot_analysis=model.generate_content(f"Compare the {job_desc} with the resume {pdf}\
                                      and provide the SWOT analysis report followed by actional insights in bullet points for the resume")
    keyword_analysis=model.generate_content(f"Compare the {job_desc} with the resume {pdf}\
                                            and mention the keyword and give me a list of the keywords \
                                            shown in job description but missing from the Resume")
    projects=model.generate_content(f"Compare the {job_desc} with the resume {pdf}\
                                      and give me a list of ML competitions and projects that are aligned\
                                     with the job description and the role in bullet points along with the \
                                    chances of getting selected in percentage")
    return ((st.write(good_fit.text)), 
            (st.write(ats_score.text)), 
            (st.write(prob.text)), 
            (st.write(keyword_analysis.text)), 
            (st.write(swot_analysis.text)), 
            (st.write(projects.text)))