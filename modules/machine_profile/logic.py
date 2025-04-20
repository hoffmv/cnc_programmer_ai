from mongo import get_mongo_collection

def get_machine_profile(machine_id: str):
    machines = get_mongo_collection("cnc_machines")
    return machines.find_one({"machine_id": machine_id}) or {"status": "not found"}

def set_machine_profile(machine_id: str, spindle_rpm: int, travel_x: float, travel_y: float, travel_z: float, notes: str = ""):
    machines = get_mongo_collection("cnc_machines")
    profile = {
        "machine_id": machine_id,
        "spindle_rpm": spindle_rpm,
        "travel_x_in": travel_x,
        "travel_y_in": travel_y,
        "travel_z_in": travel_z,
        "notes": notes
    }
    machines.update_one({"machine_id": machine_id}, {"$set": profile}, upsert=True)
    return {
        "status": "saved",
        "machine_id": machine_id,
        "rpm_max": spindle_rpm,
        "travel": f"{travel_x}x{travel_y}x{travel_z} in"
    }
