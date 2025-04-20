from fastapi import APIRouter
from pydantic import BaseModel
from . import logic

router = APIRouter()

class MaterialToolInput(BaseModel):
    material: str
    tool_diameter: float
    machine_id: str  # currently unused, but available

@router.post("/calculate")
def calculate_material_settings(data: MaterialToolInput):
    result = logic.calculate_cutting_parameters(
        material=data.material,
        tool_diameter=data.tool_diameter,
        machine_rpm_limit=10000  # or dynamically retrieved later
    )
    return result
