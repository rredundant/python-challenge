import os
import csv
unique_months = 0
net_change = 0
month_change = 0
change_list = []
last_month = 0
row = ['',0]

with open('budget_data.csv', 'r') as f:
    reader = csv.reader(f,)
    next(reader)
    largest_increase = row
    largest_decrease = row
    for row in reader:
        net_change += int(row[1])
        this_month = row[1]
        unique_months += 1
        month_change = int(this_month) - int(last_month)
        change_list.append(month_change)
        if month_change > int(largest_increase[1]):
            largest_increase = [row[0], month_change]
        if month_change < int(largest_decrease[1]):
            largest_decrease = [row[0], month_change]
        last_month = this_month
change_list.pop(0)

def mean(x):
    return float(sum(x)/len(x))
ave_change = round(mean(change_list))

print("Financial Analysis")
print(f"Total Months: {unique_months}")
print(f"Total: ${net_change}")
print(f"Average Change: ${round(mean(change_list),2)}")
print(f"Greatest Increase in Profits: {largest_increase[0]} ${largest_increase[1]}")
print(f"Greatest Decrease in Profits: {largest_decrease[0]} ${largest_decrease[1]}")

file = open("Financial_Analysis.txt", "w")
file.write("Financial Analysis" + "\n")
file.write(f"Total Months: {unique_months}" + "\n")
file.write(f"Total: ${net_change}" + "\n")
file.write(f"Average Change: ${round(mean(change_list),2)}" + "\n")
file.write(f"Greatest Increase in Profits: {largest_increase[0]} ${largest_increase[1]}" + "\n")
file.write(f"Greatest Decrease in Profits: {largest_decrease[0]} ${largest_decrease[1]}")
file.close()