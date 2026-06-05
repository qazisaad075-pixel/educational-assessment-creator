def question_agent(objectives: list, subject: str, topic: str):
    questions = []

    for i in range(1, 11):  # 👉 10 QUESTIONS FIX
        if i == 1:
            q_type = "mcq"
        elif i == 2:
            q_type = "short_answer"
        elif i == 3:
            q_type = "essay"
        else:
            q_type = "short_answer"

        question_text = f"Q{i}: Explain {topic} in context of {subject}. Provide detailed understanding."

        question = {
            "id": i,
            "type": q_type,
            "question": question_text,
            "correct_answer": f"Understanding of {topic} in {subject}"
        }

        # MCQ options sirf MCQ ke liye
        if q_type == "mcq":
            question["options"] = [
                f"{topic} definition",
                f"{subject} concept",
                "General knowledge",
                "None of the above"
            ]

        questions.append(question)

    return {
        "questions": questions
    }