from mongo import get_mongo_collection
from datetime import datetime

def log_feedback(user: str, issue_type: str, description: str, file_ref: str = None):
    feedback_log = get_mongo_collection("cnc_feedback")
    entry = {
        "timestamp": datetime.now().isoformat(),
        "submitted_by": user,
        "issue_type": issue_type,
        "description": description,
        "file_reference": file_ref,
        "resolved": False
    }
    feedback_log.insert_one(entry)
    return {
        "status": "logged",
        "issue": issue_type,
        "file": file_ref or "N/A",
        "timestamp": entry["timestamp"]
    }
