from fastapi import APIRouter

router = APIRouter(
    prefix="/skill-gap",
    tags=["Skill Gap"]
)


@router.get("/")
def get_skill_gap():
    return {
        "message": "Skill Gap API is working"
    }


@router.post("/")
def calculate_skill_gap(current_skill: str, target_skill: str):
    if current_skill.lower() == target_skill.lower():
        gap = "No skill gap"
    else:
        gap = f"Need to learn more about {target_skill}"

    return {
        "current_skill": current_skill,
        "target_skill": target_skill,
        "skill_gap": gap
    }