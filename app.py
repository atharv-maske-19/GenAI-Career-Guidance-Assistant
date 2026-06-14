
import streamlit as st
import plotly.express as px
import pandas as pd
import plotly.graph_objects as go

from resume_parser import extract_text_from_pdf
from career_recommender import recommend_career, find_missing_skills


from career_chatbot import get_career_advice

from report_generator import generate_report
from jd_matcher import match_resume_with_jd
from roadmap_generator import generate_roadmap
from course_recommender import recommend_courses
from ai_interview import generate_interview_question
from answer_evaluator import evaluate_answer
from interview_generator import generate_interview_questions
from interview_dashboard import calculate_interview_score

from interview_history import save_interview, get_history
from login import login_user
from register import register_user
from score_manager import save_ats_score
from career_utils import (
    calculate_ats_score,
    extract_skills,
    calculate_score,
    rank_resume,
    calculate_skill_gap,
    predict_placement,
    analyze_resume
)

# -----------------------------
# SAFE DEFAULTS
# -----------------------------
detected_keywords = []
score = 0
placement_score = 0
username = ""

if "score" not in st.session_state:
    st.session_state["score"] = 0

if "placement_score" not in st.session_state:
    st.session_state["placement_score"] = 0


# -----------------------------
# PAGE CONFIG
# -----------------------------
st.set_page_config(
    page_title="GenAI Career Guidance Assistant",
    layout="wide"
)


# -----------------------------
# LOGIN SYSTEM
# -----------------------------
st.sidebar.title("🔐 Login System")

menu = st.sidebar.selectbox("Menu", ["Login", "Register"])

if menu == "Register":

    new_user = st.sidebar.text_input("Username")
    new_pass = st.sidebar.text_input("Password", type="password")

    if st.sidebar.button("Register"):
        register_user(new_user, new_pass)
        st.sidebar.success("Registration Successful")

elif menu == "Login":

    username = st.sidebar.text_input("Username")
    password = st.sidebar.text_input("Password", type="password")

    if st.sidebar.button("Login"):
        user = login_user(username, password)

        if user:
            st.sidebar.success("Login Successful")
            st.session_state["username"] = username
            st.rerun()
        else:
            st.sidebar.error("Invalid Credentials")
            
if "username" in st.session_state:

    st.sidebar.success(
        f"Welcome {st.session_state['username']}"
    )

    if st.sidebar.button("Logout"):

        del st.session_state["username"]

        st.rerun()
# -----------------------------
# LOGIN CHECK
# -----------------------------
if "username" not in st.session_state:

    st.warning("🔐 Please login first to access the Career Guidance Assistant.")

    st.stop()

st.title("🎓 GenAI Career Guidance Assistant")
st.write("Upload your resume and get AI-powered career recommendations.")


# -----------------------------
# FILE UPLOAD
# -----------------------------
uploaded_file = st.file_uploader("Upload Resume (PDF)", type=["pdf"])

resume_text = ""

if uploaded_file is not None and uploaded_file.size > 0:

    resume_text = extract_text_from_pdf(uploaded_file)

    st.subheader("📄 Extracted Resume Text")
    st.text_area("Resume Content", resume_text, height=250)


    # -----------------------------
    # ATS SCORE
    # -----------------------------
    ats_score, detected_keywords = calculate_ats_score(resume_text)

    st.subheader("📄 ATS Resume Score")

    gauge = go.Figure(
        go.Indicator(
            mode="gauge+number",
            value=ats_score,
            title={"text": "ATS Score"},
            gauge={"axis": {"range": [0, 100]}}
        )
    )

    st.plotly_chart(gauge, use_container_width=True)
    st.success(f"ATS Score: {ats_score}/100")

    if st.button("💾 Save ATS Score"):
        if "username" in st.session_state:
            save_ats_score(st.session_state["username"], ats_score)
            st.success("ATS Score Saved")
        else:
            st.warning("Please login first")
            
 
    # -----------------------------
    # ATS KEYWORDS
    # -----------------------------
    st.subheader("🔑 ATS Keywords Found")
    st.info(f"Detected {len(detected_keywords)} keywords")

    for keyword in detected_keywords:
        st.write(f"✅ {keyword}")


    # -----------------------------
    # CAREER RECOMMENDATION
    # -----------------------------
    career, scores = recommend_career(resume_text)
    st.success(f"🎯 Recommended Career: {career}")


    # -----------------------------
    # SKILLS
    # -----------------------------
    skills = extract_skills(resume_text)

    st.subheader("🛠️ Detected Skills")

    if skills:
        for skill in skills:
            st.write(f"✅ {skill}")
    else:
        st.warning("No skills detected.")


    # -----------------------------
    # RESUME ANALYSIS
    # -----------------------------
    strengths, weaknesses = analyze_resume(skills, ats_score)

    st.subheader("💪 Resume Strengths")
    for s in strengths:
        st.success(f"✅ {s}")

    st.subheader("⚠️ Areas To Improve")
    for w in weaknesses:
        st.warning(f"📌 {w}")


    # -----------------------------
    # READINESS SCORE
    # -----------------------------
    st.session_state["score"] = calculate_score(skills, career)

    st.subheader("📊 Career Readiness Score")
    st.progress(st.session_state["score"] / 100)
    st.write(f"Score: {st.session_state['score']}/100")


    # -----------------------------
    # RESUME RANK
    # -----------------------------
    rank_score = rank_resume(ats_score, st.session_state["score"])

    st.subheader("🏆 Resume Ranking Score")
    st.success(f"Overall Score: {rank_score}/100")


    # -----------------------------
    # CAREER CHART
    # -----------------------------
    df = pd.DataFrame({
        "Career": list(scores.keys()),
        "Score": list(scores.values())
    })

    fig = px.bar(df, x="Career", y="Score")
    st.plotly_chart(fig, use_container_width=True)


    # -----------------------------
    # MISSING SKILLS
    # -----------------------------
    if career:
        missing_skills = find_missing_skills(resume_text, career)
    else:
        missing_skills = []

    st.subheader("📚 Skills To Learn")

    for skill in missing_skills:
        st.write(f"📌 {skill}")


    # -----------------------------
    # SKILL GAP
    # -----------------------------
    skill_gap_score = calculate_skill_gap(skills, missing_skills)

    st.subheader("📊 Skill Gap Analysis")
    st.progress(skill_gap_score / 100)
    st.success(f"Skill Coverage: {skill_gap_score}%")
    
    # -----------------------------
    # PLACEMENT PREDICTION
    # -----------------------------
    st.subheader("🎯 Placement Prediction")

    interview_score = st.session_state.get("interview_score", 70)

    st.session_state["placement_score"] = predict_placement(
        ats_score,
        st.session_state["score"],
        interview_score,
        skill_gap_score
    )

    st.progress(st.session_state["placement_score"] / 100)
    st.success(f"Placement Probability: {st.session_state['placement_score']}%")


    # -----------------------------
    # ROADMAP
    # -----------------------------
    roadmap = generate_roadmap(career, missing_skills)

    st.subheader("🗺️ Learning Roadmap")

    for step in roadmap:
        st.write(f"🚀 {step}")


    # -----------------------------
    # COURSES
    # -----------------------------
    courses = recommend_courses(career)

    st.subheader("🎓 Courses")

    for c in courses:
        st.write(f"📚 {c}")


    # -----------------------------
    # JD MATCHING
    # -----------------------------
    st.subheader("📋 JD Match")

    jd = st.text_area("Paste Job Description")

    if jd:
        match_score, matched, missing = match_resume_with_jd(resume_text, jd)

        st.progress(match_score / 100)
        st.success(f"Match Score: {match_score}%")

        for m in matched:
            st.write(f"✅ {m}")

        for m in missing:
            st.write(f"📌 {m}")


    # -----------------------------
    # REPORT
    # -----------------------------
    st.subheader("📥 Download Report")

    try:
        pdf = generate_report(
            ats_score,
            career,
            skills,
            strengths,
            weaknesses
        )

        with open(pdf, "rb") as f:
            st.download_button(
                "Download Report",
                f,
                file_name="career_report.pdf",
                mime="application/pdf"
            )

    except Exception as e:
        st.error(f"Report Error: {e}")


# -----------------------------
# AI CAREER COUNSELOR
# -----------------------------
st.divider()
st.header("🤖 AI Career Counselor")

user_question = st.text_input("Ask career question")

if st.button("Get AI Advice"):
    if user_question:
        with st.spinner("Thinking..."):
            answer = get_career_advice(user_question, resume_text)

        st.subheader("AI Response")
        st.write(answer)
    else:
        st.warning("Enter a question")


# -----------------------------
# AI MOCK INTERVIEW
# -----------------------------
st.divider()
st.header("🎤 AI Mock Interview")

if "question" not in st.session_state:
    st.session_state.question = ""

if st.button("Generate Question"):
    if resume_text:
        st.session_state.question = generate_interview_question(career)
        st.success("Question Generated")
    else:
        st.warning("Upload resume first")

if st.session_state.question:
    st.subheader("Interview Question")
    st.write(st.session_state.question)

answer = st.text_area("Your Answer")

if st.button("Evaluate Answer"):

    if not st.session_state.question:
        st.warning("Generate question first")

    elif not answer:
        st.warning("Enter your answer")

    else:
        feedback = evaluate_answer(st.session_state.question, answer)

        st.subheader("AI Feedback")
        st.write(feedback)

        interview_score = calculate_interview_score(feedback)
        st.session_state["interview_score"] = interview_score

        st.subheader("📊 Interview Score")
        st.progress(interview_score / 100)
        st.success(f"Score: {interview_score}%")

        save_interview(
            st.session_state["username"],
            st.session_state.question,
            answer,
            feedback
        )

        st.success("Saved to Interview History")


# -----------------------------
# INTERVIEW HISTORY
# -----------------------------
st.divider()
st.header("📜 Interview History")

username = st.session_state.get("username", "")
history = get_history(username) if username else []

if history:
    for item in reversed(history):
        st.write(f"❓ Question: {item['Question']}")
        st.write(f"💬 Answer: {item['Answer']}")
        st.write(f"📝 Feedback: {item['Feedback']}")
        st.divider()
else:
    st.info("No interview history available") 