import plotly.express as px
import pandas as pd

# Define sample tasks
tasks = [
    {"Task": "Site Survey", "Start": "2025-05-01", "Finish": "2025-05-05", "Phase": "Design"},
    {"Task": "Architectural Design", "Start": "2025-05-06", "Finish": "2025-05-20", "Phase": "Design"},
    {"Task": "Structural Engineering", "Start": "2025-05-10", "Finish": "2025-05-25", "Phase": "Design"},
    {"Task": "Select Subcontractors", "Start": "2025-05-21", "Finish": "2025-05-26", "Phase": "Subcontracting"},
    {"Task": "Sign Contracts", "Start": "2025-05-27", "Finish": "2025-05-30", "Phase": "Subcontracting"},
    {"Task": "Foundation Work", "Start": "2025-06-01", "Finish": "2025-06-10", "Phase": "Implementation"},
    {"Task": "Framing", "Start": "2025-06-11", "Finish": "2025-06-20", "Phase": "Implementation"},
    {"Task": "Electrical & Plumbing", "Start": "2025-06-21", "Finish": "2025-06-30", "Phase": "Implementation"},
    {"Task": "Final Inspection", "Start": "2025-07-01", "Finish": "2025-07-02", "Phase": "Implementation"},
]

# Create DataFrame
df = pd.DataFrame(tasks)
df["Start"] = pd.to_datetime(df["Start"])
df["Finish"] = pd.to_datetime(df["Finish"])

# Intense colors for phases
intense_colors = {
    "Design": "#e74c3c",         # bright red
    "Subcontracting": "#f1c40f", # vivid yellow
    "Implementation": "#2ecc71"  # bright green
}

# Build Gantt chart
fig = px.timeline(
    df,
    x_start="Start",
    x_end="Finish",
    y="Task",
    color="Phase",
    color_discrete_map=intense_colors,
    title="Construction Project Gantt Chart (Dark Mode)",
)

fig.update_yaxes(autorange="reversed")

# Apply dark background and light text
fig.update_layout(
    plot_bgcolor="#1e1e1e",
    paper_bgcolor="#1e1e1e",
    font=dict(color="white"),
    xaxis_title="Timeline",
    yaxis_title="Tasks",
    margin=dict(l=100, r=40, t=60, b=40),
    height=500
)

fig.show()

