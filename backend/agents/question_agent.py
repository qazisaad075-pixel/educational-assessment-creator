def question_agent(objectives: list, subject: str, topic: str):
    return {
        "questions": [
            {
                "id": 1,
                "type": "mcq",
                "question": f"What is the main concept of {topic}?",
                "options": ["Option A", "Option B", "Option C", "Option D"],
                "correct_answer": "Option A"
            },
            {
                "id": 2,
                "type": "short_answer",
                "question": f"Explain the importance of {topic} in {subject}.",
                "correct_answer": f"{topic} is important because it forms the foundation of {subject}."
            },
            {
                "id": 3,
                "type": "essay",
                "question": f"Discuss the real world applications of {topic}.",
                "correct_answer": f"{topic} has many real world applications in {subject}."
            }
        ]
    }