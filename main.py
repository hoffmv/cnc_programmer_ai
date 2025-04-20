from fastapi import FastAPI

# Import routers

from modules.machine_profile.routes import router as machine_profile_router

from modules.material_tool_engine.routes import router as material_tool_engine_router

from modules.cam_optimizer.routes import router as cam_optimizer_router

from modules.feedback_logger.routes import router as feedback_logger_router

from modules.file_organizer.routes import router as file_organizer_router


app = FastAPI(title="Cnc Programmer Ai")

# Register routers

app.include_router(machine_profile_router, prefix="/machine_profile", tags=["Machine Profile"])

app.include_router(material_tool_engine_router, prefix="/material_tool_engine", tags=["Material Tool Engine"])

app.include_router(cam_optimizer_router, prefix="/cam_optimizer", tags=["Cam Optimizer"])

app.include_router(feedback_logger_router, prefix="/feedback_logger", tags=["Feedback Logger"])

app.include_router(file_organizer_router, prefix="/file_organizer", tags=["File Organizer"])


@app.get("/")
def root():
    return {"msg": "API is active and ready"}