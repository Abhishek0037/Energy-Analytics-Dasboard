import pandas as pd
import matplotlib.pyplot as plt



#reading cleaned data
df = pd.read_csv(
    "Data/cleaned_data.csv",
    parse_dates=["Datetime"]
)

print(df.head())


#basic statistics
avg_power = df["Global_active_power"].mean()

max_power= df["Global_active_power"].max()

min_power=df["Global_active_power"].min()

print("The average power consumed is :",avg_power,"kilowatts")
print("The maximum power consumed is :",max_power,"kilowatts")
print("The minimum power consumed is :",min_power,"kilowatts")


#peak hours
df["Hour"] = df["Datetime"].dt.hour

hourly_usage = (
    df.groupby("Hour")["Global_active_power"]
      .mean()
      .sort_values(ascending=False)
)

print("\nTop Peak Hours:")
print(hourly_usage.head())


# Hourly average consumption
hourly_usage = (
    df.groupby("Hour")["Global_active_power"]
      .mean()
)

plt.figure(figsize=(10,5))
hourly_usage.plot()

plt.title("Average Power Consumption by Hour")
plt.xlabel("Hour of Day")
plt.ylabel("Power Consumption (kW)")
plt.grid(True)
plt.savefig("hourly_consumption.png")
plt.show()


#montly analysis
df["Month"] = df["Datetime"].dt.month

monthly_usage = (
    df.groupby("Month")["Global_active_power"]
      .mean()
      .sort_values(ascending=False)
)

print("\nMonthly Usage:")
print(monthly_usage)

#monthly consumption chart
monthly_usage = (
    df.groupby("Month")["Global_active_power"]
      .mean()
)

plt.figure(figsize=(10,5))
monthly_usage.plot(kind="bar")

plt.title("Average Power Consumption by Month")
plt.xlabel("Month")
plt.ylabel("Power Consumption (kW)")
plt.savefig("monthly_consumption.png")
plt.show()