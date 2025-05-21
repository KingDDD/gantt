import matplotlib.pyplot as plt

# Investment allocation breakdown
categories = [
    "Salaries (6 months)",
    "Office Space & Utilities",
    "Software Licenses",
    "Computers & Equipment",
    "Insurance",
    "Legal/Accounting Fees",
    "Marketing/Branding",
    "Contingency Reserve"
]
amounts = [250000, 30000, 40000, 25000, 20000, 10000, 5000, 120000]

# Create pie chart
plt.figure(figsize=(8, 8))
plt.pie(amounts, labels=categories, autopct='%1.1f%%', startangle=140)
plt.title("Initial Investment Allocation ($500,000)")
plt.axis('equal')  # Equal aspect ratio ensures pie chart is circular
plt.tight_layout()
plt.show()

