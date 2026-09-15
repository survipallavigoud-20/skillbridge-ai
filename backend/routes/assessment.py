from fastapi import APIRouter

router = APIRouter(
    prefix="/assessment",
    tags=["Assessment"]
)


@router.get("/")
def get_assessment():
    return {
        "message": "Assessment API is working"
    }


@router.post("/")
def submit_assessment(answer: str):
    answer_lower = answer.lower()

    if "python" in answer_lower:
        skill = "Python"
    elif "web" in answer_lower or "html" in answer_lower:
        skill = "Web Development"
    elif "data" in answer_lower:
        skill = "Data Science"
    elif "ai" in answer_lower or "machine learning" in answer_lower:
        skill = "AI / Machine Learning"
    else:
        skill = "General Programming"

    return {
        "message": "Assessment submitted successfully",
        "answer": answer,
        "identified_skill": skill
    }
    