# File: advanced/data_analysis.py
#!/usr/bin/env python3
"""
Loads a sample CSV, computes summary statistics, and plots data distribution.
Requires pandas, numpy, seaborn, matplotlib.
"""
import pandas as pd       # For data manipulation
import numpy as np        # For numeric operations
import seaborn as sns      # For statistical plotting
import matplotlib.pyplot as plt  # For figure control

def main():
    # 1) Load the data from CSV file
    data_path = "data/sample.csv"
    df = pd.read_csv(data_path)
    print(f"Loaded data from {data_path}, shape: {df.shape}\n")

    # 2) Compute and display basic summary statistics
    print("Summary statistics for numeric columns:")
    print(df.describe(), "\n")

    # 3) Create a normalized score column: z-score = (value - mean) / std
    mean_score = df["score"].mean()
    std_score = df["score"].std()
    df["norm_score"] = (df["score"] - mean_score) / std_score
    print(f"Added norm_score: mean={mean_score:.2f}, std={std_score:.2f}\n")

    # 4) Compute and display the correlation matrix
    corr_matrix = df.corr()
    print("Correlation matrix:")
    print(corr_matrix, "\n")

    # 5) Plot the distribution of the normalized scores
    sns.histplot(df["norm_score"], kde=True)
    plt.title("Normalized Score Distribution")
    plt.xlabel("Normalized Score")
    plt.ylabel("Frequency")
    plt.tight_layout()

    # Save the plot to file
    output_plot = "advanced/normalized_score.png"
    plt.savefig(output_plot)
    print(f"Saved distribution plot to {output_plot}\n")

    # Optionally show plot (uncomment below if running interactively)
    # plt.show()

if __name__ == "__main__":
    main()
