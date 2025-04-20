def optimize_toolpath(material: str, tool_diameter: float, finish_required: bool):
    strategy = {}
    base_stepover = 0.4 * tool_diameter
    passes = 1 if not finish_required else 2
    if material.lower() in ["aluminum", "brass", "plastic"]:
        pattern = "climb"
        rough_stepover = 0.5 * tool_diameter
    else:
        pattern = "conventional"
        rough_stepover = 0.35 * tool_diameter
    finish_stepover = 0.1 * tool_diameter if finish_required else rough_stepover
    strategy["pattern"] = pattern
    strategy["roughing_stepover"] = round(rough_stepover, 3)
    strategy["finishing_stepover"] = round(finish_stepover, 3)
    strategy["passes"] = passes
    strategy["notes"] = f"{material.title()} | Tool Ø={tool_diameter} in | Finish required: {finish_required}"
    return strategy
