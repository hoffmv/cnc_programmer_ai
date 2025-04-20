from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()

class Machine_profileModelInput(BaseModel):
    # Add fields here
    example_field: str

@router.post("/run")
def run_machine_profile(data: Machine_profileModelInput):
    return {
        "msg": "Auto-generated response from machine_profile",
        "received": data.dict()
    }