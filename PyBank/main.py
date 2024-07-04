import os
import csv

# Path to the CSV file
csv_path = os.path.join('Resources', 'budget_data.csv')

# Initializing variables for analysis
total_months = 0
net_total = 0
monthly_changes = []
dates = []

# Function to process the CSV file
def process_csv(file_path):
    global total_months, net_total
    with open(file_path, newline='') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',')
        
        # Skip the header
        next(csvreader)

        # Read the first row to initialize variables
        first_row = next(csvreader)
        total_months += 1
        net_total += int(first_row[1])
        previous_amount = int(first_row[1])

        # Iterating over each row in the CSV
        for row in csvreader:
            process_row(row, previous_amount)
            previous_amount = int(row[1])

# Function to process each row
def process_row(row, previous_amount):
    global total_months, net_total
    total_months += 1
    current_amount = int(row[1])
    net_total += current_amount

    # Calculating the monthly change and storing it
    change = current_amount - previous_amount
    monthly_changes.append(change)
    dates.append(row[0])

# Function to calculate financial statistics
def calculate_statistics():
    average_change = round(sum(monthly_changes) / len(monthly_changes), 2)
    greatest_increase = max(monthly_changes)
    greatest_decrease = min(monthly_changes)
    greatest_increase_date = dates[monthly_changes.index(greatest_increase)]
    greatest_decrease_date = dates[monthly_changes.index(greatest_decrease)]

    return average_change, greatest_increase, greatest_decrease, greatest_increase_date, greatest_decrease_date

# Function to print the financial analysis
def print_analysis(average_change, greatest_increase, greatest_decrease, greatest_increase_date, greatest_decrease_date):
    print("Financial Analysis\n")
    print("-------------------------------\n")
    print(f"Total Months: {total_months}\n")
    print(f"Total: ${net_total}\n")
    print(f"Average Change: ${average_change}\n")
    print(f"Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase})\n")
    print(f"Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease})\n")

# Function to write the results to a text file
def write_results(file_path, average_change, greatest_increase, greatest_decrease, greatest_increase_date, greatest_decrease_date):
    with open(file_path, "w") as text_file:
        text_file.write("Financial Analysis\n")
        text_file.write("-------------------------------\n")
        text_file.write(f"Total Months: {total_months}\n")
        text_file.write(f"Total: ${net_total}\n")
        text_file.write(f"Average Change: ${average_change}\n")
        text_file.write(f"Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase})\n")
        text_file.write(f"Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease})\n")

# Main execution
process_csv(csv_path)
average_change, greatest_increase, greatest_decrease, greatest_increase_date, greatest_decrease_date = calculate_statistics()
print_analysis(average_change, greatest_increase, greatest_decrease, greatest_increase_date, greatest_decrease_date)
results_path = os.path.join('Analysis', 'results.txt')
write_results(results_path, average_change, greatest_increase, greatest_decrease, greatest_increase_date, greatest_decrease_date)
