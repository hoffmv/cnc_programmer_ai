from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()

class Cam_optimizerModelInput(BaseModel):
    # Add fields here
    example_field: str

@router.post("/run")
def run_cam_optimizer(data: Cam_optimizerModelInput):
    return {
        "msg": "Auto-generated response from cam_optimizer",
        "received": data.dict()
    }