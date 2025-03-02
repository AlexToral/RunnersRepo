import pandas as pd

# Load the CSV file into a DataFrame
csv_path = "./csv/filtered_runners.csv"
df = pd.read_csv(csv_path)
columns_to_print = ['Name', 'Pos', 'FinishTime','Time_Difference']
# Convert the FinishTime column to timedelta
df['FinishTime'] = pd.to_timedelta(df['FinishTime'], errors='coerce')

# Set your finish time as a timedelta
my_finish_time = pd.to_timedelta("01:45:30.00")

# Calculate the time difference relative to your finish time
df['TimeDifference'] = df['FinishTime'] - my_finish_time

# Drop rows with invalid or NaT FinishTime
df_filtered = df.dropna(subset=['FinishTime'])

# Filter for runners who finished before you (negative TimeDifference)
df_before_you = df_filtered[df_filtered['TimeDifference'] < pd.Timedelta(0)]

# Calculate the absolute time difference (to find the closest finishers)
df_before_you['AbsTimeDifference'] = df_before_you['TimeDifference'].abs()

# Sort by absolute time difference (closest to your finish time)
sorted_df = df_before_you.sort_values(by='AbsTimeDifference')

# Function to format timedelta without days
def format_timedelta(td):
    return str(td).split(" ")[-1]  # Get only the time part (ignoring the days)

# Apply the formatting to the relevant columns
sorted_df['FinishTime'] = sorted_df['FinishTime'].apply(format_timedelta)
sorted_df['Time_Difference'] = sorted_df['AbsTimeDifference'].apply(format_timedelta)

# Print the results
print("Top 5 runners who finished before you, closest to your finish time:")
print(sorted_df[columns_to_print].head(5).to_string(index=False))
