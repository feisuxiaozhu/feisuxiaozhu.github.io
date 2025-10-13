import numpy as np
import matplotlib.pyplot as plt


scores = np.array([
    100.00, 85.71, 92.38, 100.00, 93.33, 86.67, 98.10, 100.00,
    100.00, 78.10, 86.67, 59.05, 95.24, 91.43, 97.14, 100.00,
    89.52, 88.57, 95.24, 60.95, 100.00, 95.24, 95.24, 91.43, 99.05
])


bins = [55, 60, 65, 70, 75, 80, 85, 90, 95, 100.001]
mean_val = np.mean(scores)
median_val = np.median(scores)

plt.hist(scores, bins=bins, edgecolor='black', rwidth=0.9)
plt.xlabel("Score")
plt.ylabel("Number of People")
plt.title("Midterm 1")

plt.axvline(mean_val, color='red', linestyle='dashed', linewidth=1.5, label=f"Average = {mean_val:.1f}")
plt.axvline(median_val, color='blue', linestyle='dotted', linewidth=1.5, label=f"Median = {median_val:.1f}")

# # Add grade cutoffs
# plt.axvline(90, color='green', linestyle='solid', linewidth=1, label="A cutoff (90)")
# plt.axvline(80, color='orange', linestyle='solid', linewidth=1, label="B cutoff (80)")
# plt.axvline(70, color='purple', linestyle='solid', linewidth=1, label="C cutoff (70)")
# plt.axvline(60, color='brown', linestyle='solid', linewidth=1, label="D cutoff (60)")

# Add shaded grade regions
plt.axvspan(90, 100, color='green', alpha=0.15, label="Grade A")
plt.axvspan(80, 90, color='orange', alpha=0.15, label="Grade B")
plt.axvspan(70, 80, color='purple', alpha=0.15, label="Grade C")
plt.axvspan(60, 70, color='brown', alpha=0.15, label="Grade D")
plt.axvspan(55, 60, color='red', alpha=0.15, label="Grade F")

plt.xticks(bins)
plt.legend()
plt.show()