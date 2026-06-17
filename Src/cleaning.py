import pandas as pd

# Load data
df = pd.read_csv("Data/household_power_consumption.csv")

# Create datetime column
df["Datetime"] = pd.to_datetime(
    df["Date"] + " " + df["Time"],
    dayfirst=True
)

# Convert numeric columns
numeric_cols = [
    "Global_active_power",
    "Global_reactive_power",
    "Voltage",
    "Global_intensity",
    "Sub_metering_1",
    "Sub_metering_2",
    "Sub_metering_3"
]

for col in numeric_cols:
    df[col] = pd.to_numeric(df[col], errors="coerce")

# Check missing values again
print(df.isnull().sum())

# Remove rows with missing values
df = df.dropna()

print("\nShape after cleaning:")
print(df.shape)

# Save cleaned dataset
df.to_csv("Data/cleaned_data.csv", index=False)

print("\nCleaned dataset saved!")