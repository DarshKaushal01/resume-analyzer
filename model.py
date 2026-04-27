from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def analyze_resume(resume, job_desc):
    documents = [resume, job_desc]

    tfidf = TfidfVectorizer(stop_words='english')
    tfidf_matrix = tfidf.fit_transform(documents)

    similarity = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:2])
    score = round(similarity[0][0] * 100, 2)

   
    resume_words = set(resume.lower().split())
    job_words = set(job_desc.lower().split())

    missing = list(job_words - resume_words)[:10]

    return score, missing
