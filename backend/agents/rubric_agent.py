def rubric_agent(questions: list):
    rubrics = []
    for q in questions:
        rubrics.append({
            "question_id": q["id"],
            "total_points": q["points"],
            "criteria": [
                {
                    "description": "Correct and complete answer",
                    "points": q["points"]
                },
                {
                    "description": "Partially correct answer",
                    "points": q["points"] // 2
                },
                {
                    "description": "Incorrect or no answer",
                    "points": 0
                }
            ]
        })
    
    return {"rubrics": rubrics}