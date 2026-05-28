import streamlit as st
from file_parser import extract_text
from quiz_generator import generate_mcqs
import os

st.set_page_config(page_title="AI Quiz Generator")

st.title("AI Quiz Generator")

uploaded_file = st.file_uploader(
    "Upload a PDF, DOCX, or TXT file",
    type=["pdf", "docx", "txt"]
)

if uploaded_file:

    # Create uploads folder if not exists
    os.makedirs("uploads", exist_ok=True)

    file_path = os.path.join("uploads", uploaded_file.name)

    # Save uploaded file
    with open(file_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    st.success("File uploaded successfully!")

    # Extract text
    text = extract_text(file_path)

    st.success("Text extracted successfully!")

    # Generate quiz only once
    if "quiz_data" not in st.session_state:

        with st.spinner("Generating quiz..."):
            st.session_state.quiz_data = generate_mcqs(text)

    quiz_data = st.session_state.quiz_data

    st.subheader("Quiz")

    # Store user answers
    if "user_answers" not in st.session_state:
        st.session_state.user_answers = {}

    score = 0

    # Display questions
    for i, q in enumerate(quiz_data):

        st.write(f"### Q{i+1}. {q['question']}")

        selected = st.radio(
            "Choose your answer",
            ["Select an option"] + q["options"],
            key=f"question_{i}"
        )

        if selected != "Select an option":
            st.session_state.user_answers[i] = selected

    # Submit button
    if st.button("Submit Quiz"):

        for i, q in enumerate(quiz_data):

            selected_answer = st.session_state.user_answers.get(i)

            if selected_answer == q["answer"]:
                score += 1

        st.subheader("Result")

        st.write(f" Correct Answers: {score}")

        st.write(f" Wrong Answers: {len(quiz_data) - score}")

        percentage = (score / len(quiz_data)) * 100

        st.write(f" Final Score: {percentage:.2f}%")
