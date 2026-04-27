from flask import Flask, render_template, request
from utils import extract_text
from model import analyze_resume

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    file = request.files['resume']
    job_desc = request.form['job_desc']

    resume_text = extract_text(file)
    score, missing_skills = analyze_resume(resume_text, job_desc)

    return render_template('index.html',
                           score=score,
                           missing_skills=missing_skills)

if __name__ == '__main__':
    app.run(debug=True)
