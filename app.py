
import streamlit as st
from src.agents import InterviewCoach
from src.data_store import initialize_vector_store

st.set_page_config(
    page_title="AI Mock Interview Coach",
    page_icon="🎯",
    layout="wide"
)

st.title("🎯 Company-Smart Mock Interview Coach")
st.write("Your personal AI-powered interview preparation assistant.")

@st.cache_resource
def load_coach():
    vector_store = initialize_vector_store()
    return InterviewCoach(vector_store)

with st.sidebar:
    st.header("Interview Settings")

    company = st.text_input(
        "Target Company",
        "Lufthansa Technik"
    )

    role = st.text_input(
        "Job Role",
        "Junior Executive - Customs & Trade Operations"
    )

    difficulty = st.selectbox(
        "Difficulty Level",
        ["Beginner", "Intermediate", "Advanced"]
    )

    mode = st.radio(
        "Choose Your Activity",
        [
            "Mock Interview",
            "Evaluate Answer",
            "Personalised Coaching",
            "Session Report"
        ]
    )

if "history" not in st.session_state:
    st.session_state.history = []

if "messages" not in st.session_state:
    st.session_state.messages = []

if "last_evaluation" not in st.session_state:
    st.session_state.last_evaluation = ""

try:
    coach = load_coach()
except Exception as error:
    st.error(f"Application setup error: {error}")
    st.stop()

st.subheader(f"Company: {company}")
st.write(f"Role: {role}")

if mode == "Mock Interview":

    st.header("Live Mock Interview")

    if st.button("Start Interview"):
        question = coach.ask_question(
            company,
            role,
            difficulty,
            st.session_state.history
        )

        st.session_state.messages.append(
            {"role": "assistant", "content": question}
        )

    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    answer = st.chat_input("Enter your interview answer")

    if answer:
        st.session_state.messages.append(
            {"role": "user", "content": answer}
        )

        evaluation = coach.evaluate_answer(
            company,
            role,
            answer
        )

        st.session_state.history.append({
            "answer": answer,
            "evaluation": evaluation
        })

        st.session_state.last_evaluation = evaluation

        next_question = coach.ask_question(
            company,
            role,
            difficulty,
            st.session_state.history
        )

        st.session_state.messages.append({
            "role": "assistant",
            "content": "### Answer Evaluation\n"
                       + evaluation
                       + "\n\n### Next Question\n"
                       + next_question
        })

        st.rerun()

elif mode == "Evaluate Answer":

    st.header("Answer Evaluation")

    answer = st.text_area(
        "Enter your interview answer"
    )

    if st.button("Evaluate My Answer") and answer.strip():

        result = coach.evaluate_answer(
            company,
            role,
            answer
        )

        st.session_state.last_evaluation = result
        st.markdown(result)

elif mode == "Personalised Coaching":

    st.header("AI Interview Coach")

    concern = st.text_area(
        "What would you like to improve?"
    )

    if st.button("Get Coaching") and concern.strip():

        result = coach.get_coaching(
            company,
            role,
            concern
        )

        st.markdown(result)

elif mode == "Session Report":

    st.header("Interview Performance Report")

    if st.button("Generate Report"):

        if st.session_state.history:

            report = coach.generate_report(
                company,
                role,
                st.session_state.history
            )

            st.markdown(report)

        else:
            st.warning(
                "Complete a mock interview first."
            )
