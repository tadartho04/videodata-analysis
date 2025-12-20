import pandas as pd

# Load the dataset
df = pd.read_csv("Videodata.csv")

# Display basic information
print(df.info())

# Check missing values
print(df.isnull().sum())

# Replace '?' with proper missing values
df.replace("?", pd.NA, inplace=True)

# Remove duplicate rows
df.drop_duplicates(inplace=True)

# Save cleaned dataset
df.to_csv("cleaned_videodata.csv", index=False)

print("Data cleaning completed successfully.")

# -----------------------------
# Feature Engineering
# -----------------------------

# 🔹Fixing column names first 
df.columns = df.columns.str.strip()

# 🔹 Age group feature
df["age_group"] = pd.cut(
    df["age"],
    bins=[0, 25, 45, 65, 120],
    labels=["Young", "Adult", "Senior", "Old"]
)

# 🔹 Work hours category
df["work_hours_category"] = pd.cut(
    df["hours-per-week"],
    bins=[0, 34, 45, 100],
    labels=["Part-time", "Full-time", "Overtime"]
)

# 🔹 Capital activity
df["capital_activity"] = "None"
df.loc[df["capital-gain"] > 0, "capital_activity"] = "Gain"
df.loc[df["capital-loss"] > 0, "capital_activity"] = "Loss"

# 🔹 Saving final dataset
df.to_csv("final_cleaned_videodata.csv", index=False)

print("Feature engineering completed successfully")