def standard_agent(subject: str, grade_level: int, topic: str):
    return {
        "subject": subject,
        "grade_level": grade_level,
        "topic": topic,
        "objectives": [
            f"Understand the basic concepts of {topic}",
            f"Apply {topic} principles to solve problems",
            f"Analyze and evaluate {topic} in real world scenarios"
        ]
    }