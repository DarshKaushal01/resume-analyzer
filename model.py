from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Predefined skill set (you can expand this)
SKILLS_DB = [
    "python", "java", "c++", "machine learning", "deep learning",
    "nlp", "data analysis", "pandas", "numpy", "tensorflow",
    "keras", "scikit-learn", "sql", "excel", "power bi",
    "flask", "django", "html", "css", "javascript",
    "react", "nodejs", "git", "docker", "aws"
]

def extract_skills(text):
    text = text.lower()
    found_skills = []

    for skill in SKILLS_DB:
        if skill in text:
            found_skills.append(skill)

    return list(set(found_skills))


def analyze_resume(resume, job_desc):
    documents = [resume, job_desc]

    tfidf = TfidfVectorizer(stop_words='english')
    tfidf_matrix = tfidf.fit_transform(documents)

    similarity = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:2])
    score = round(similarity[0][0] * 100, 2)

    resume_skills = set(extract_skills(resume))
    job_skills = set(extract_skills(job_desc))

    missing_skills = list(job_skills - resume_skills)

    return score, missing_skills
