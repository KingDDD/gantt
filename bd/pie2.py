import matplotlib.pyplot as plt

# Define time allocation breakdown (in percentage)
categories = [
    "Billable Project Work",
    "Internal R&D / Tools Development",
    "Administrative / Meetings",
    "Training / Professional Development",
    "Unallocated / Bench Time"
]
percentages = [65, 15, 10, 5, 5]

# Create pie chart
plt.figure(figsize=(8, 8))
plt.pie(percentages, labels=categories, autopct='%1.1f%%', startangle=140, colors=plt.cm.Paired.colors)
plt.title("Engineering Staff Time Allocation")
plt.axis('equal')  # Equal aspect ratio ensures pie chart is circular
plt.tight_layout()
plt.show()

