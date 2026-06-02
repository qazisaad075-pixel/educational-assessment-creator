def analytics_agent(questions: list, rubrics: list):
    total_points = sum(q["points"] for q in questions)
    
    difficulty_dist = {"remember": 0, "understand": 0, "apply": 0}
    for q in questions:
        if q["difficulty"] in difficulty_dist:
            difficulty_dist[q["difficulty"]] += 1
    
    return {
        "total_questions": len(questions),
        "total_points": total_points,
        "difficulty_distribution": difficulty_dist,
        "learning_gaps": [
            "Students may struggle with application level questions",
            "More practice needed on core concepts"
        ],
        "recommendations": [
            "Add more practice questions on basic concepts",
            "Include real world examples in teaching"
        ]
    }