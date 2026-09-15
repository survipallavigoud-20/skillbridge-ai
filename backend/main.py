from fastapi import FastAPI
from routes.users import router as users_router
from routes.skills import router as skills_router
from routes.assessment import router as assessment_router
from routes.skill_gap import router as skill_gap_router
from routes.recommendations import router as recommendations_router

app = FastAPI(title="SkillBridge AI Backend")

app.include_router(users_router)
app.include_router(skills_router)
app.include_router(assessment_router)
app.include_router(skill_gap_router)
app.include_router(recommendations_router)

@app.get("/")
def home():
    return {
        "message": "SkillBridge AI Backend is running!"
    }


@app.get("/health")
def health_check():
    return {
        "status": "healthy"
    }