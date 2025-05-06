import plotly.express as px
import pandas as pd
from datetime import datetime, timedelta

# Define sample tasks for the construction company
tasks = [
    # Design Phase
    {"Task": "Site Survey", "Start": "2025-05-01", "Finish": "2025-05-05", "Phase": "Design"},
    {"Task": "Architectural Design", "Start": "2025-05-06", "Finish": "2025-05-20", "Phase": "Design"},
    {"Task": "Structural Engineering", "Start": "2025-05-10", "Finish": "2025-05-25", "Phase": "Design"},
    
    # Subcontracting Phase
    {"Task": "Select Subcontractors", "Start": "2025-05-21", "Finish": "2025-05-26", "Phase": "Subcontracting"},
    {"Task": "Sign Contracts", "Start": "2025-05-27", "Finish": "2025-05-30", "Phase": "Subcontracting"},
    
    # Implementation Phase
    {"Task": "Foundation Work", "Start": "2025-06-01", "Finish": "2025-06-10", "Phase": "Implementation"},
    {"Task": "Framing", "Start": "2025-06-11", "Finish": "2025-06-20", "Phase": "Implementation"},
    {"Task": "Electrical & Plumbing", "Start": "2025-06-21", "Finish": "2025-06-30", "Phase": "Implementation"},
    {"Task": "Final Inspection", "Start": "2025-07-01", "Finish": "2025-07-02", "Phase": "Implementation"},
]

# Create DataFrame
df = pd.DataFrame(tasks)

# Convert dates to datetime
df["Start"] = pd.to_datetime(df["Start"])
df["Finish"] = pd.to_datetime(df["Finish"])

# Create Gantt chart
fig = px.timeline(
    df,
    x_start="Start",
    x_end="Finish",
    y="Task",
    color="Phase",
    title="Construction Project Gantt Chart",
)

fig.update_yaxes(autorange="reversed")  # Tasks from top to bottom
fig.update_layout(
    xaxis_title="Timeline",
    yaxis_title="Tasks",
    margin=dict(l=100, r=40, t=60, b=40),
    height=500
)

fig.show()

