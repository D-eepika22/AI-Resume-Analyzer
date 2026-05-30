import streamlit as st
from openai import OpenAI
from PyPDF2 import PdfReader

# OPENROUTER API
import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

print("API_KEY =", os.getenv("API_KEY"))

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=os.getenv("API_KEY")
)
# PAGE SETTINGS

st.set_page_config(
    page_title="AI Resume Analyzer",
    page_icon="📄",
    layout="wide"
)

# SIDEBAR

with st.sidebar:

    st.header("⚡ AI Resume Analyzer")

    st.write("Hackathon Project")

    st.info("""
Features:
✅ ATS Score
✅ Resume Analysis
✅ Missing Skills
✅ Matched Skills
✅ Interview Questions
✅ Improved Resume Generator
✅ Resume Paste Option
""")

# MAIN TITLE

st.title(" AI Resume Analyzer")
st.write("Upload your resume or paste resume text.")

# FILE UPLOAD

uploaded_file = st.file_uploader(
    "Upload Resume (PDF)",
    type=["pdf"]
)

# RESUME PASTE OPTION

st.subheader("OR Paste Resume Text")
pasted_resume = st.text_area(
    "Paste Your Resume Here",
    height=250
)

# JOB ROLE DROPDOWN

job_role = st.selectbox(
    " Select Target Job Role",
    [
        "📊 Data Analyst",
        "💻 Web Developer",
        "🤖 AI Engineer",
        "🧠 Machine Learning Engineer",
        "🎨 Frontend Developer",
        "⚙️ Backend Developer",
        "🌐 Full Stack Developer",
        "🐍 Python Developer",
        "🖥 Software Engineer",
        "🎭 UI/UX Designer",
        "📡 ECE Engineer",
        "⚡ Electrical Engineer",
        "🛠 Mechanical Engineer",
        "🏗 Civil Engineer",
        "📈 MBA",
        "💼 BBA"
    ]
)

# PDF TEXT EXTRACTION

def extract_text_from_pdf(file):
    pdf_reader = PdfReader(file)
    text = ""
    for page in pdf_reader.pages:
        extracted = page.extract_text()
        if extracted:
            text += extracted
    return text

# ANALYZE BUTTON

if st.button("Analyze Resume"):
   
    # CHECK INPUT
   
    if uploaded_file is not None or pasted_resume != "":
        with st.spinner("Analyzing Resume..."):

            # GET RESUME TEXT
         
            if uploaded_file is not None:
                resume_text = extract_text_from_pdf(uploaded_file)
            else:
                resume_text = pasted_resume
            resume_lower = resume_text.lower()
            job_role_lower = job_role.lower()
 
            # ROLE-BASED SKILLS     

            if "web developer" in job_role_lower:
                skills_keywords = [
                    "html",
                    "css",
                    "javascript",
                    "react",
                    "node",
                    "mongodb",
                    "express",
                    "bootstrap",
                    "api",
                    "git"
                ]

            elif "data analyst" in job_role_lower:

                skills_keywords = [
                    "python",
                    "sql",
                    "excel",
                    "power bi",
                    "tableau",
                    "pandas",
                    "numpy",
                    "statistics",
                    "data visualization",
                    "machine learning"
                ]

            elif "ai engineer" in job_role_lower:

                skills_keywords = [
                    "python",
                    "tensorflow",
                    "pytorch",
                    "machine learning",
                    "deep learning",
                    "nlp",
                    "computer vision",
                    "streamlit",
                    "numpy",
                    "pandas"
                ]

            elif "ece engineer" in job_role_lower:

                skills_keywords = [
                    "embedded systems",
                    "vlsi",
                    "verilog",
                    "matlab",
                    "pcb",
                    "arduino",
                    "microcontroller",
                    "iot",
                    "c programming",
                    "digital electronics"
                ]

            else:

                skills_keywords = [
                    "communication",
                    "leadership",
                    "problem solving"
                ]

            # SKILL MATCHING
            
            matched_skills = []
            missing_skills = []

            matched_count = 0

            for skill in skills_keywords:

                if skill.lower() in resume_lower:

                    matched_count += 1
                    matched_skills.append(skill)

                else:

                    missing_skills.append(skill)

            total_skills = len(skills_keywords)

            skills_score = (
                matched_count / total_skills
            ) * 40

            # EXPERIENCE ANALYSIS   

            experience_keywords = [
                "internship",
                "experience",
                "developer",
                "engineer",
                "worked",
                "company"
            ]

            experience_matches = 0

            for word in experience_keywords:

                if word in resume_lower:

                    experience_matches += 1

            experience_score = (
                experience_matches / len(experience_keywords)
            ) * 20
            
            # PROJECT ANALYSIS
        
            project_keywords = [
                "project",
                "github",
                "api",
                "dashboard",
                "web app",
                "streamlit"
            ]

            project_matches = 0

            for word in project_keywords:

                if word in resume_lower:

                    project_matches += 1

            project_score = (
                project_matches / len(project_keywords)
            ) * 20
     
            # EDUCATION ANALYSIS
        
            education_keywords = [
                "b.tech",
                "college",
                "university",
                "cgpa"
            ]

            education_matches = 0

            for word in education_keywords:

                if word in resume_lower:

                    education_matches += 1

            education_score = (
                education_matches / len(education_keywords)
            ) * 10
    
            # ACHIEVEMENT ANALYSIS
          
            achievement_keywords = [
                "developed",
                "created",
                "built",
                "designed"
            ]

            achievement_matches = 0

            for word in achievement_keywords:

                if word in resume_lower:

                    achievement_matches += 1

            achievement_score = (
                achievement_matches / len(achievement_keywords)
            ) * 10
            
            # FINAL ATS SCORE
           
            ats_score = int(
                skills_score +
                experience_score +
                project_score +
                education_score +
                achievement_score
            )

            if ats_score > 100:
                ats_score = 100

            # AI PROMPT
           
            prompt = f"""
You are an expert ATS Resume Analyzer.

Analyze this resume for the role: {job_role}

Resume:
{resume_text}

Provide:
1. Professional Summary
2. Missing Skills
3. Strengths
4. Weaknesses
5. Improvement Suggestions
6. 5 Interview Questions
"""
           
            # AI RESPONSE
            
            completion = client.chat.completions.create(
                model="meta-llama/llama-3-8b-instruct",
                messages=[
                    {
                        "role": "user",
                        "content": prompt
                    }
                ]
            )

            result = completion.choices[0].message.content
          
            # RESULTS
        
            st.success("Analysis Complete!")

            st.subheader(" ATS Scan Results")

            col1, col2 = st.columns([1, 2])

            with col1:

                st.metric(
                    "Overall ATS Score",
                    f"{ats_score}/100"
                )

                st.progress(ats_score)

                
                # ATS FEEDBACK

                if ats_score >= 90:

                    st.success(" Excellent Resume!")

                elif ats_score >= 75:

                    st.info(" Good Resume!")

                elif ats_score >= 50:

                    st.warning(" Average Resume")

                else:

                    st.error(" Low ATS Score")

            with col2:

                st.info(f"""
Resume analyzed successfully for:
{job_role}

ATS score based on:
 Skills
 Education
 Experience
 Projects
 Resume Keywords
""")

            # MATCHED SKILLS
           

            st.subheader(" Matched Skills")

            for skill in matched_skills:

                st.success(skill)

            # MISSING SKILLS
        

            st.subheader(" Missing Skills")

            for skill in missing_skills:

                st.error(skill)

           
            # AI ANALYSIS
        

            st.subheader(" AI Resume Analysis")

            st.write(result)

            # DOWNLOAD REPORT
           

            st.download_button(
                label=" Download Analysis Report",
                data=result,
                file_name="resume_analysis.txt",
                mime="text/plain"
            )

    else:

        st.warning("Please upload PDF or paste resume text.")