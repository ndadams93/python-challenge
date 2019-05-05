import os
import pandas as pd

csv_path = "Budget_Data.csv"

months = budget_df["Date"].nunique()
net_profit = budget_df["Profit/Losses"].sum()
average_change = budget_df["Difference"].mean()
max_change = budget_df["Difference"].max()
min_change = budget_df["Difference"].min()

budget_df = pd.read_csv(csv_path, encoding="utf-8")
budget_df["Previous Month"] = budget_df["Profit/Losses"].shift(1)
budget_df["Difference"] = budget_df["Profit/Losses"] - budget_df['Previous Month']
budget_df.head()

print("Financial Analysis")
print("----------------------------")
print("Total Months: " + str(months))
print("Total: $" + str(net_profit))
print("Average Change: $" + str(average_change))
print("Greatest Increase in Profits: " + str(max_change))
print("Greatest Decrease in Profits: " + str(min_change))

save_file = csv_path.strip(".csv") + " Analysis.txt"
filepath = os.path.join(".", save_file)
with open(filepath,'w') as text:
    text.write("Financial Analysis" + "\n")
    text.write("Total Months: {months}" + "\n")
    text.write("Total: ${net_profit}" + "\n")
    text.write("Average Revenue Change: ${average_change}" + "\n")
    text.write("Greatest Increase in Revenue: " + "\n")
    text.write("Greatest Decrease in Revenue: " + "\n")