from fastapi import APIRouter

router = APIRouter(
    prefix="/recommendations",
    tags=["Recommendations"]
)


@router.get("/")
def get_recommendations():
    return {
        "message": "Recommendations API is working"
    }


@router.post("/")
def get_learning_recommendations(skill_gap: str):
    recommendations = [
        "Learn the basics",
        "Practice with small projects",
        "Build one real-world project"
    ]

    return {
        "skill_gap": skill_gap,
        "recommendations": recommendations
    }
