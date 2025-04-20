import os
import shutil

def organize_uploaded_file(filename: str, upload_dir: str = "incoming_files", base_dir: str = "organized_files"):
    _, ext = os.path.splitext(filename.lower())
    if ext in [".nc", ".tap", ".gcode"]:
        folder = "gcode"
    elif ext in [".dxf", ".dwg", ".svg"]:
        folder = "drawings"
    elif ext in [".toolpath", ".cam", ".setup"]:
        folder = "toolpaths"
    else:
        folder = "misc"
    source_path = os.path.join(upload_dir, filename)
    target_dir = os.path.join(base_dir, folder)
    os.makedirs(target_dir, exist_ok=True)
    target_path = os.path.join(target_dir, filename)
    try:
        shutil.move(source_path, target_path)
        return {"status": "success", "category": folder, "moved_to": target_path}
    except Exception as e:
        return {"status": "error", "error": str(e)}
