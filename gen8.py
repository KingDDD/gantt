import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
from datetime import datetime, timedelta

# enumerate tasks
tasks = [
    {"Task": "This is a Test", "Start": "2025-04-25", "Finish": "2025-05-01", "Phase": "TestPHASE", "Assigned To": "Damian Lopez"},
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

df = pd.DataFrame(tasks)
df["Start"] = pd.to_datetime(df["Start"])
df["Finish"] = pd.to_datetime(df["Finish"])

# color scheme
intense_colors = {
    "Design": "#e74c3c",
    "Subcontracting": "#f1c40f",
    "Implementation": "#2ecc71"
}

# generate gantt chart frame
fig = px.timeline(
    df,
    x_start="Start",
    x_end="Finish",
    y="Task",
    color="Phase",
    color_discrete_map=intense_colors,
    hover_data=["Assigned To"],
    text="Assigned To",
    title="Klockner Mockup Gantt Chart"
)
fig.update_yaxes(autorange="reversed")
fig.update_traces(textposition='inside', insidetextanchor='start', textfont_color='white')

# cosmetics and legend position
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

# shade for weekends
start_date = df["Start"].min()
end_date = df["Finish"].max()
current = start_date

while current <= end_date:
    if current.weekday() == 5:  # saturday
        weekend_start = current
        weekend_end = current + timedelta(days=2)  # sat + sun
        fig.add_shape(
            type="rect",
            x0=weekend_start,
            x1=weekend_end,
            y0=-0.5,
            y1=len(df["Task"]) - 0.5,
            fillcolor="rgba(255, 255, 255, 0.05)",  # white overlay
            layer="below",
            line_width=0,
        )
    current += timedelta(days=1)

fig.show()

