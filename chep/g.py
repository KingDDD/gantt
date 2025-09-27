# Corrected Gantt chart generator for Gramener - saves PNG to /mnt/data
import matplotlib.pyplot as plt
import pandas as pd
import matplotlib.dates as mdates
from datetime import datetime, timedelta

# Project start date (week 1 starts)
start_date = datetime.strptime("2025-09-22", "%Y-%m-%d")

# Define milestones with durations (in weeks)
milestones = [
    {"Task": "Expedite Po Approval", "Duration_weeks": 1},
    {"Task": "Design & Hardware Finalization", "Duration_weeks": 1},
    {"Task": "Physical Implementation (Fulton Site)", "Duration_weeks": 3},
    {"Task": "Live Data acquisition & Training", "Duration_weeks": 4},
    {"Task": "Iterative Testing/Training into Handoff", "Duration_weeks": 3}, # starts week of Dec 22
]

# Build DataFrame
df = pd.DataFrame(milestones)

# Generate sequential start dates (fill forward, no gaps)
start_dates = []
current_start = start_date
for dur in df["Duration_weeks"]:
    start_dates.append(current_start)
    current_start = current_start + timedelta(weeks=dur)

df["Start"] = pd.to_datetime(start_dates)
df["End"] = df["Start"] + pd.to_timedelta(df["Duration_weeks"], unit="W")

# Sort by End date ascending so earliest-completing task is first
df = df.sort_values(by="End").reset_index(drop=True)

# Prepare numeric dates for plotting
df["Start_num"] = mdates.date2num(df["Start"])
df["Width_days"] = df["Duration_weeks"] * 7  # width in days for matplotlib date units

# Plot Gantt chart
fig, ax = plt.subplots(figsize=(12, 6))
y_positions = range(len(df))

for i, row in df.iterrows():
    ax.barh(i, row["Width_days"], left=row["Start_num"], height=0.6)

# Invert y-axis so earliest-completing (first end date) is on top
ax.invert_yaxis()

# Set y-ticks and labels
ax.set_yticks(list(y_positions))
ax.set_yticklabels(df["Task"])

# Format x-axis as dates
ax.xaxis_date()
ax.xaxis.set_major_locator(mdates.WeekdayLocator(interval=1))
ax.xaxis.set_major_formatter(mdates.DateFormatter("%b %d"))
plt.xticks(rotation=45)

ax.set_title("Dori AI — In Line Flaw Detection: Project Timeline")
ax.set_xlabel("Date")
ax.set_ylabel("Milestone")
plt.grid(axis="x", linestyle="--", alpha=0.5)
plt.tight_layout()

# Save image
output_path = "./DoriAi_Project_Timeline.png"
plt.savefig(output_path, dpi=300)
plt.close()

# Show a small table of the schedule for verification
display_df = df[["Task", "Start", "End", "Duration_weeks"]].copy()
display_df["Start"] = display_df["Start"].dt.strftime("%Y-%m-%d")
display_df["End"] = display_df["End"].dt.strftime("%Y-%m-%d")

# Display results to user and provide file location
import caas_jupyter_tools as cjt
cjt.display_dataframe_to_user("Dori Ai Gantt Schedule", display_df)

print(f"Saved Gantt chart image to: {output_path}")

