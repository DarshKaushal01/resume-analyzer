import streamlit as st
from utils import extract_text
from model import analyze_resume, extract_skills

st.set_page_config(page_title="Smart Resume Analyzer", layout="wide")

# Custom CSS for better UI
st.markdown("""
<style>
.main {
    background-color: #0E1117;
    color: white;
}
.stButton>button {
    background-color: #4CAF50;
    color: white;
    border-radius: 8px;
    padding: 10px 20px;
}
</style>
""", unsafe_allow_html=True)

st.title("🚀 Smart Resume Analyzer")
st.write("AI-powered resume analysis with skill insights")

col1, col2 = st.columns(2)

with col1:
    uploaded_file = st.file_uploader("📄 Upload Resume (PDF)", type=["pdf"])

with col2:
    job_desc = st.text_area("💼 Paste Job Description")

if st.button("🔍 Analyze Resume"):
    if uploaded_file and job_desc:
        resume_text = extract_text(uploaded_file)

        score, missing_skills = analyze_resume(resume_text, job_desc)
        extracted_skills = extract_skills(resume_text)

        st.markdown("## 📊 Results")

        col1, col2 = st.columns(2)

        with col1:
            st.metric("Match Score", f"{score}%")

            st.subheader("🧠 Extracted Skills")
            for skill in extracted_skills:
                st.write(f"✅ {skill}")

        with col2:
            st.subheader("❌ Missing Skills")
            for skill in missing_skills:
                st.write(f"🔴 {skill}")

    else:
        st.warning("⚠️ Upload resume and job description")
