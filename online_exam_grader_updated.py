
import streamlit as st

# Define the correct answers: single letters for Q1–66, combined letters (no comma) for Q67–74
answer_key = [
    'C','D','B','A','D','C','C','B','B','A',
    'C','D','A','A','C','B','B','C','D','C',
    'B','C','A','B','B','A','D','A','C','A',
    'A','D','B','D','D','C','B','C','D','B',
    'C','C','A','C','C','C','C','A','C','B',
    'C','C','A','C','A','D','A','B','B','B',
    'A','B','B','B','C','B',
    'BD','BC','BC','AD','AC','BD','AD','AD'
]

st.title("📝 Student Exam Auto-Grader")
st.write("Enter your 74 answers below. Use commas to separate answers.")
st.write("For multiple-answer questions (67–74), type answers together with no comma (e.g., `BD`, `AC`)")

student_input = st.text_area("Enter your answers (Q1 to Q74):")

if student_input:
    student_answers = [ans.strip().upper().replace(" ", "") for ans in student_input.split(",")]
    score = 0

    if len(student_answers) != 74:
        st.error(f"❌ You entered {len(student_answers)} answers. Please enter exactly 74.")
    else:
        for i in range(74):
            correct = answer_key[i]
            student = student_answers[i]

            # Sort both answers for fair comparison (e.g., "BD" == "DB")
            if sorted(student) == sorted(correct):
                score += 1

        st.success(f"✅ Your Score: {score} / 74")
        st.write(f"Percentage: {score / 74 * 100:.2f}%")
