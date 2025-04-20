from fastapi import APIRouter
from pydantic import BaseModel
from . import logic

router = APIRouter()

class MaterialToolInput(BaseModel):
    material: str
    tool_diameter: float
    machine_id: str

@router.post("/calculate")
def calculate_material_settings(data: MaterialToolInput):
    result = logic.calculate_cutting_parameters(
        material=data.material,
        tool_diameter=data.tool_diameter,
        machine_rpm_limit=10000
    )

    # Ensure ALL expected frontend keys exist
    return {
        "spindle_speed_rpm": result.get("spindle_speed_rpm"),
        "feed_rate_ipm": result.get("feed_rate_ipm"),
        "depth_of_cut_inches": result.get("depth_of_cut_inches"),
        "stepover_inches": result.get("stepover_inches"),
        "notes": result.get("notes")
    }
