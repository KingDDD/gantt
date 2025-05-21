import matplotlib.pyplot as plt
import pandas as pd
import matplotlib.dates as mdates
from datetime import datetime

# Define key milestones with start and end dates
milestones = [
    {"Task": "Company Formation & Legal Setup", "Start": "2025-06-01", "End": "2025-06-15"},
    {"Task": "Initial Hiring (5 Engineers)", "Start": "2025-06-16", "End": "2025-07-15"},
    {"Task": "Office Setup & Infrastructure", "Start": "2025-06-20", "End": "2025-07-10"},
    {"Task": "Begin Internal Project Work", "Start": "2025-07-15", "End": "2025-08-31"},
    {"Task": "Start Accepting External Projects", "Start": "2025-09-01", "End": "2025-09-30"},
    {"Task": "Reach Break-Even", "Start": "2025-12-01", "End": "2025-12-01"},
    {"Task": "Expand Engineering Team", "Start": "2026-01-01", "End": "2026-03-31"},
    {"Task": "Open Second Office (Optional)", "Start": "2027-01-01", "End": "2027-06-30"},
]

# Convert milestones to DataFrame
df = pd.DataFrame(milestones)
df["Start"] = pd.to_datetime(df["Start"])
df["End"] = pd.to_datetime(df["End"])
df["Duration"] = df["End"] - df["Start"]

# Create Gantt chart
fig, ax = plt.subplots(figsize=(12, 6))
for i, row in df.iterrows():
    ax.barh(row["Task"], row["Duration"].days, left=row["Start"], color="skyblue", edgecolor="black")

ax.set_title("Archimedes Industries – Business Milestone Timeline")
ax.set_xlabel("Date")
ax.set_ylabel("Milestone")
ax.xaxis.set_major_locator(mdates.MonthLocator(interval=2))
ax.xaxis.set_major_formatter(mdates.DateFormatter("%b %Y"))
plt.grid(axis='x', linestyle='--', alpha=0.6)
plt.tight_layout()
plt.show()

