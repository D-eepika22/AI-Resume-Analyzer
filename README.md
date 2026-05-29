#  AI Resume Analyzer #

An AI-powered ATS Resume Analyzer built using Python, Streamlit, OpenRouter API, and LLMs.

This project helps users analyze resumes for multiple job roles and provides:
- ATS Score
- Resume Feedback
- Missing Skills
- Interview Questions
- Resume Improvements
- AI-generated Suggestions

The system supports both:
- PDF Resume Upload
- Direct Resume Text Paste

##Features

##  Dynamic ATS Score Calculation
The ATS score is calculated dynamically using:
- Skills Matching
- Experience Detection
- Projects Analysis
- Education Analysis
- Achievements Detection
- Resume Formatting


##  AI-Powered Resume Analysis
The AI provides:
- Professional Summary
- Resume Strengths
- Resume Weaknesses
- Missing Skills
- Improvement Suggestions
- Recommended Projects
- Interview Questions


## Multi-Domain Support
Supports resumes for:

###  Tech Roles
- Web Developer
- Frontend Developer
- Backend Developer
- Full Stack Developer
- Python Developer
- Software Engineer
- AI Engineer
- Machine Learning Engineer
- Data Analyst

###  Core Engineering Roles
- ECE Engineer
- Electrical Engineer
- Mechanical Engineer
- Civil Engineer

### Management Roles
- MBA
- BBA



#  AI Model Used
This project uses:
python
meta-llama/llama-3-8b-instruct
via:
python
OpenRouter API

##Technologies Used

| Technology | Purpose |
| Python | Backend Logic |
| Streamlit | Frontend UI |
| OpenAI SDK | AI API Integration |
| OpenRouter API | LLM Access |
| PyPDF2 | PDF Text Extraction |

##Libraries Used
Install dependencies using:
bash
pip install streamlit openai PyPDF2

## How to Run the Project
## Step 1: Clone Repository
bash
git clone YOUR_GITHUB_REPOSITORY_LINK

## Step 2: Open Project Folder
bash
cd AI_Resume_Analyzer

## Step 3: Install Requirements
bash
pip install -r requirements.txt

## Step 4: Run Streamlit App
bash
python -m streamlit run app.py

## ATS Score Breakdown

| Section | Weight |
|---|---|
| Skills Match | 35 |
| Experience | 20 |
| Projects | 15 |
| Education | 15 |
| Achievements | 10 |
| Formatting | 5 |

## ATS Score Feedback System

| Score Range | Resume Quality |
| 90 - 100 | 🔥 Excellent Resume |
| 75 - 89 | ✅ Good Resume |
| 50 - 74 | ⚠ Average Resume |
| Below 50 | ❌ Needs Improvement |

##Project Highlights

✅ Beginner-Friendly  
✅ Real-World AI Project  
✅ Hackathon Ready  
✅ Multi-Domain ATS Support  
✅ AI + Resume + NLP Integration  
✅ Portfolio Ready Project  

## Developed By
Deepika 

