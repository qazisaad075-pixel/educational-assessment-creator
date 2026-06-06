def question_agent(objectives: list, subject: str, topic: str):

    questions = []
    q_id = 1

    for obj in objectives:

        # MCQ
        questions.append({
            "id": q_id,
            "type": "mcq",
            "question": f"Which of the following best represents {obj} in {topic}?",
            "options": [
                f"Correct understanding of {obj}",
                f"Incorrect concept of {obj}",
                f"Partially correct idea of {obj}",
                f"No relation to {obj}"
            ],
            "correct_answer": f"Correct understanding of {obj}"
        })
        q_id += 1

        # Short Answer
        questions.append({
            "id": q_id,
            "type": "short_answer",
            "question": f"Explain {obj} in the context of {subject}.",
            "correct_answer": f"Detailed explanation of {obj}"
        })
        q_id += 1

        # Essay
        questions.append({
            "id": q_id,
            "type": "essay",
            "question": f"Discuss the importance of {obj} in real life applications.",
            "correct_answer": f"Importance and application of {obj}"
        })
        q_id += 1

    return {"questions": questions}