import plotly.express as px
import pandas as pd

# Define tasks with assigned resources
tasks = [
    {"Task": "Site Survey", "Start": "2025-05-01", "Finish": "2025-05-05", "Phase": "Design", "Assigned To": "Survey Team"},
    {"Task": "Architectural Design", "Start": "2025-05-06", "Finish": "2025-05-20", "Phase": "Design", "Assigned To": "Architects"},
    {"Task": "Structural Engineering", "Start": "2025-05-10", "Finish": "2025-05-25", "Phase": "Design", "Assigned To": "Engineers"},
    {"Task": "Select Subcontractors", "Start": "2025-05-21", "Finish": "2025-05-26", "Phase": "Subcontracting", "Assigned To": "Project Manager"},
    {"Task": "Sign Contracts", "Start": "2025-05-27", "Finish": "2025-05-30", "Phase": "Subcontracting", "Assigned To": "Legal Team"},
    {"Task": "Foundation Work", "Start": "2025-06-01", "Finish": "2025-06-10", "Phase": "Implementation", "Assigned To": "Construction Crew A"},
    {"Task": "Framing", "Start": "2025-06-11", "Finish": "2025-06-20", "Phase": "Implementation", "Assigned To": "Construction Crew B"},
    {"Task": "Electrical & Plumbing", "Start": "2025-06-21", "Finish": "2025-06-30", "Phase": "Implementation", "Assigned To": "Subcontractors"},
    {"Task": "Final Inspection", "Start": "2025-07-01", "Finish": "2025-07-02", "Phase": "Implementation", "Assigned To": "Inspector"},
]

# Create DataFrame
df = pd.DataFrame(tasks)
df["Start"] = pd.to_datetime(df["Start"])
df["Finish"] = pd.to_datetime(df["Finish"])

# Intense color scheme
intense_colors = {
    "Design": "#e74c3c",
    "Subcontracting": "#f1c40f",
    "Implementation": "#2ecc71"
}

# Create the Gantt chart
fig = px.timeline(
    df,
    x_start="Start",
    x_end="Finish",
    y="Task",
    color="Phase",
    color_discrete_map=intense_colors,
    hover_data=["Assigned To"],
    title="Klockner Mockup Gantt View"
)

fig.update_yaxes(autorange="reversed")

# Dark theme & styled legend
fig.update_layout(
    plot_bgcolor="#1e1e1e",
    paper_bgcolor="#1e1e1e",
    font=dict(color="white"),
    xaxis_title="Timeline",
    yaxis_title="Tasks",
    legend=dict(
        bgcolor="#2c2c2c",
        bordercolor="white",
        borderwidth=1,
        font=dict(color="white")
    ),
    margin=dict(l=100, r=40, t=60, b=40),
    height=550
)

fig.show()

