import streamlit as st
from utils import extract_text
from model import analyze_resume

st.set_page_config(page_title="Resume Analyzer", layout="centered")

st.title("📄 Smart Resume Analyzer")
st.write("Upload your resume and compare it with a job description")

uploaded_file = st.file_uploader("Upload Resume (PDF)", type=["pdf"])
job_desc = st.text_area("Paste Job Description")

if st.button("Analyze"):
    if uploaded_file and job_desc:
        resume_text = extract_text(uploaded_file)
        score, missing_skills = analyze_resume(resume_text, job_desc)

        st.subheader(f"📊 Match Score: {score}%")

        st.subheader("❌ Missing Skills:")
        for skill in missing_skills:
            st.write(f"- {skill}")
    else:
        st.warning("Please upload resume and enter job description")
