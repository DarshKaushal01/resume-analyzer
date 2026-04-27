import streamlit as st
import pandas as pd
from utils import extract_text
from model import analyze_resume, extract_skills

st.set_page_config(page_title="Smart Resume Analyzer", layout="wide")

st.title("🚀 Smart Resume Analyzer")
st.write("AI-powered resume analysis with visual insights")

uploaded_file = st.file_uploader("📄 Upload Resume (PDF)", type=["pdf"])
job_desc = st.text_area("💼 Paste Job Description")

if st.button("🔍 Analyze Resume"):
    if uploaded_file and job_desc:
        resume_text = extract_text(uploaded_file)

        score, missing_skills = analyze_resume(resume_text, job_desc)
        resume_skills = extract_skills(resume_text)
        job_skills = extract_skills(job_desc)

        st.markdown("## 📊 Analytics Dashboard")

        # 🔹 Score Section
        st.subheader("📈 Match Score")
        st.metric("Score", f"{score}%")
        st.progress(int(score))

        # 🔹 Skill Comparison Data
        matched_skills = list(set(resume_skills) & set(job_skills))

        data = {
            "Category": ["Matched Skills", "Missing Skills"],
            "Count": [len(matched_skills), len(missing_skills)]
        }

        df = pd.DataFrame(data)

        # 📊 Bar Chart
        st.subheader("📊 Skills Comparison")
        st.bar_chart(df.set_index("Category"))

        # 📉 Pie Chart (using dataframe)
        pie_data = pd.DataFrame({
            "Type": ["Matched", "Missing"],
            "Values": [len(matched_skills), len(missing_skills)]
        })

        st.subheader("🥧 Skills Distribution")
        st.dataframe(pie_data)

        # 🔹 Detailed Sections
        col1, col2 = st.columns(2)

        with col1:
            st.subheader("✅ Matched Skills")
            for skill in matched_skills:
                st.write(f"✔️ {skill}")

        with col2:
            st.subheader("❌ Missing Skills")
            for skill in missing_skills:
                st.write(f"❌ {skill}")

    else:
        st.warning("⚠️ Upload resume and enter job description")
