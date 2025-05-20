#!/usr/bin/env python3
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

def main():
    # 1) Load the data
    df = pd.read_csv("data/sample.csv")
    
    # 2) Compute basic stats
    print("Summary statistics:")
    print(df.describe(), end="\n\n")
    
    # 3) Add a new column
    df["norm_score"] = (df["score"] - df["score"].mean()) / df["score"].std()
    
    # 4) Show correlation matrix
    corr = df.corr()
    print("Correlation matrix:")
    print(corr, end="\n\n")
    
    # 5) Plot distribution of norm_score
    sns.histplot(df["norm_score"], kde=True)
    plt.title("Normalized Score Distribution")
    plt.xlabel("Normalized Score")
    plt.ylabel("Frequency")
    plt.tight_layout()
    plt.savefig("advanced/normalized_score.png")
    print("Saved plot to advanced/normalized_score.png")

if __name__ == "__main__":
    main()
