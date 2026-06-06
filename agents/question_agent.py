def question_agent(objectives: list, subject: str, topic: str):

    questions = [
        {
            "id": 1,
            "type": "mcq",
            "question": f"What is the best definition of {topic} in {subject}?",
            "options": [
                f"A concept related to {topic}",
                "An unrelated idea",
                "A mathematical formula",
                "None of these"
            ],
            "correct_answer": f"A concept related to {topic}"
        },
        {
            "id": 2,
            "type": "short_answer",
            "question": f"Define {topic} in your own words.",
            "correct_answer": f"Definition of {topic}"
        },
        {
            "id": 3,
            "type": "essay",
            "question": f"Explain the importance of {topic} in {subject}.",
            "correct_answer": f"Importance of {topic}"
        },
        {
            "id": 4,
            "type": "short_answer",
            "question": f"Give one real-life example of {topic}.",
            "correct_answer": f"Example of {topic}"
        },
        {
            "id": 5,
            "type": "short_answer",
            "question": f"What are the key characteristics of {topic}?",
            "correct_answer": f"Characteristics of {topic}"
        },
        {
            "id": 6,
            "type": "short_answer",
            "question": f"How is {topic} used in daily life?",
            "correct_answer": f"Uses of {topic}"
        },
        {
            "id": 7,
            "type": "mcq",
            "question": f"Which statement is most closely related to {topic}?",
            "options": [
                f"Statement about {topic}",
                "Irrelevant statement",
                "Random statement",
                "None of these"
            ],
            "correct_answer": f"Statement about {topic}"
        },
        {
            "id": 8,
            "type": "short_answer",
            "question": f"What problems can occur if {topic} is misunderstood?",
            "correct_answer": f"Problems related to {topic}"
        },
        {
            "id": 9,
            "type": "essay",
            "question": f"Compare {topic} with another related concept in {subject}.",
            "correct_answer": f"Comparison involving {topic}"
        },
        {
            "id": 10,
            "type": "short_answer",
            "question": f"Summarize everything you learned about {topic}.",
            "correct_answer": f"Summary of {topic}"
        }
    ]

    return {
        "questions": questions
    }