from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
import uuid
import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from agents.standard_agent import standard_agent
from agents.question_agent import question_agent
from agents.difficulty_agent import difficulty_agent
from agents.rubric_agent import rubric_agent
from agents.analytics_agent import analytics_agent

from database.database import get_db, create_tables, Assessment
from pydantic import BaseModel

create_tables()

router = APIRouter()


class AssessmentRequest(BaseModel):
    subject: str
    grade_level: int
    topic: str


@router.post("/create-assessment")
def create_assessment(req: AssessmentRequest, db: Session = Depends(get_db)):

    try:
        standards = standard_agent(req.subject, req.grade_level, req.topic)

        questions_data = question_agent(
            standards["objectives"],
            req.subject,
            req.topic
        )

        difficulty_data = difficulty_agent(questions_data["questions"])
        rubrics_data = rubric_agent(difficulty_data["questions"])
        analytics_data = analytics_agent(
            difficulty_data["questions"],
            rubrics_data["rubrics"]
        )

        share_id = str(uuid.uuid4())

        assessment = Assessment(
            subject=req.subject,
            grade_level=req.grade_level,
            topic=req.topic,
            objectives=standards["objectives"],
            questions=difficulty_data["questions"],
            rubrics=rubrics_data["rubrics"],
            analytics=analytics_data,
            share_id=share_id
        )

        db.add(assessment)
        db.commit()
        db.refresh(assessment)

        return {
            "id": assessment.id,
            "share_id": share_id,
            "standards": standards,
            "questions": difficulty_data["questions"],
            "rubrics": rubrics_data["rubrics"],
            "analytics": analytics_data
        }

    except Exception as e:
        return {
            "error": str(e)
        }


@router.get("/assessments")
def get_assessments(db: Session = Depends(get_db)):
    return db.query(Assessment).all()


@router.get("/stats")
def get_stats(db: Session = Depends(get_db)):

    assessments = db.query(Assessment).all()

    total_questions = sum(
        len(a.questions) for a in assessments if a.questions
    )

    return {
        "total_assessments": len(assessments),
        "total_questions": total_questions,
        "success_rate": 100 if assessments else 0
    }