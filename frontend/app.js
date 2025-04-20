document.getElementById("aiForm").addEventListener("submit", async function (e) {
  e.preventDefault();
  const payload = {
    material: document.getElementById("material").value,
    tool_diameter: parseFloat(document.getElementById("diameter").value),
    machine_name: document.getElementById("machine").value,
    operation_type: document.getElementById("operation").value,
    desired_surface_finish: document.getElementById("surface").value || null
  };
  const res = await fetch("http://127.0.0.1:8000/cam_optimizer/suggest", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(payload)
  });
  const data = await res.json();
  document.getElementById("output").innerHTML = `
    <strong>Suggested Parameters:</strong><br>
    SFM: ${data.optimal_sfm}<br>
    FPT: ${data.optimal_fpt}<br>
    Depth of Cut: ${data.depth_of_cut}<br>
    Stepover: ${data.stepover}<br>
    Confidence: ${data.confidence}
  `;
});