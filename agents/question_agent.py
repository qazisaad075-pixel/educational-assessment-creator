def question_agent(objectives: list, subject: str, topic: str):

    questions = [
        {
            "id": 1,
            "type": "mcq",
            "question": f"What is the correct definition of {topic}?",
            "correct_answer": f"Definition of {topic}",
            "options": [
                f"Definition of {topic}",
                "Incorrect answer A",
                "Incorrect answer B",
                "Incorrect answer C"
            ]
        },
        {
            "id": 2,
            "type": "short_answer",
            "question": f"Explain the meaning of {topic} in {subject}.",
            "correct_answer": f"Explanation of {topic}"
        },
        {
            "id": 3,
            "type": "essay",
            "question": f"Discuss the importance of {topic} in {subject}.",
            "correct_answer": f"Importance of {topic}"
        },
        {
            "id": 4,
            "type": "short_answer",
            "question": f"Give two examples related to {topic}.",
            "correct_answer": "Relevant examples"
        },
        {
            "id": 5,
            "type": "short_answer",
            "question": f"What are the main characteristics of {topic}?",
            "correct_answer": "Key characteristics"
        },
        {
            "id": 6,
            "type": "essay",
            "question": f"Analyze the role of {topic} in real-world situations.",
            "correct_answer": "Role analysis"
        },
        {
            "id": 7,
            "type": "short_answer",
            "question": f"How can students apply {topic} in practice?",
            "correct_answer": "Application answer"
        },
        {
            "id": 8,
            "type": "mcq",
            "question": f"Which statement best describes {topic}?",
            "correct_answer": f"Best description of {topic}",
            "options": [
                f"Best description of {topic}",
                "Wrong option A",
                "Wrong option B",
                "Wrong option C"
            ]
        },
        {
            "id": 9,
            "type": "short_answer",
            "question": f"Compare {topic} with a related concept.",
            "correct_answer": "Comparison answer"
        },
        {
            "id": 10,
            "type": "essay",
            "question": f"Evaluate the significance of {topic} in {subject}.",
            "correct_answer": "Evaluation answer"
        }
    ]

    return {"questions": questions}