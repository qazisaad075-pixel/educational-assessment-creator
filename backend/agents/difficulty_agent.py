def difficulty_agent(questions: list):
    difficulty_levels = ["remember", "understand", "apply"]
    points = [5, 10, 15]
    
    result = []
    for i, q in enumerate(questions):
        result.append({
            "id": q["id"],
            "type": q["type"],
            "question": q["question"],
            "correct_answer": q["correct_answer"],
            "difficulty": difficulty_levels[i % 3],
            "bloom_level": i + 1,
            "points": points[i % 3]
        })
    
    return {"questions": result}