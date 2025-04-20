def calculate_cutting_parameters(material: str, tool_diameter: float, machine_rpm_limit: int):
    material_sfm_map = {
        "aluminum": 600,
        "mild steel": 300,
        "stainless steel": 200,
        "brass": 500,
        "titanium": 150,
        "plastic": 800
    }

    sfm = material_sfm_map.get(material.lower(), 300)
    rpm = min((sfm * 3.82) / tool_diameter, machine_rpm_limit)
    feed_per_tooth = 0.002 if tool_diameter < 0.25 else 0.004
    num_flutes = 2 if material.lower() in ["aluminum", "plastic"] else 4
    feed_rate = rpm * num_flutes * feed_per_tooth
    depth_of_cut = 0.25 * tool_diameter
    stepover = 0.4 * tool_diameter

    return {
        "spindle_speed_rpm": round(rpm),
        "feed_rate_ipm": round(feed_rate, 1),
        "depth_of_cut_inches": round(depth_of_cut, 3),
        "stepover_inches": round(stepover, 3),
        "notes": f"Material={material}, Tool={tool_diameter}in, Flutes={num_flutes}"
    }
