from fastapi import APIRouter

router = APIRouter(
    prefix="/skills",
    tags=["Skills"]
)


@router.get("/")
def get_skills():
    return {
        "message": "Skills API is working"
    }


@router.post("/")
def add_skill(skill: str):
    return {
        "message": "Skill added successfully",
        "skill": skill
    }