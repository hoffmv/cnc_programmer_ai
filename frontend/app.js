document.getElementById("aiForm").addEventListener("submit", async function (e) {
  e.preventDefault();

  const payload = {
    material: document.getElementById("material").value,
    tool_diameter: parseFloat(document.getElementById("diameter").value),
    machine_id: document.getElementById("machine").value
  };

  try {
    const res = await fetch("/material_tool_engine/calculate", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(payload)
    });

    const data = await res.json();
    document.getElementById("output").innerHTML = `
      <strong>Suggested Parameters:</strong><br>
      RPM: ${data.spindle_speed_rpm}<br>
      Feed Rate (IPM): ${data.feed_rate_ipm}<br>
      Depth of Cut (in): ${data.depth_of_cut_inches}<br>
      Stepover (in): ${data.stepover_inches}<br>
      Notes: ${data.notes}
    `;
  } catch (err) {
    document.getElementById("output").innerText = "Error: " + err.message;
  }
});
// Force redeploy tag
