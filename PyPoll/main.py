# Importing necessary modules
import os
import csv

# Path to the election data CSV file
csv_path = os.path.join('Resources', 'election_data.csv')

# Function to process the CSV file and calculate votes
def process_csv(file_path):
    total_votes = 0
    candidate_votes = {}

    with open(file_path) as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',')
        next(csvreader)  # Skipping the header row

        # Looping through each row of the CSV file
        for row in csvreader:
            total_votes += 1
            candidate_name = row[2]

            # Recording each candidate's vote count
            if candidate_name not in candidate_votes:
                candidate_votes[candidate_name] = 1
            else:
                candidate_votes[candidate_name] += 1

    return total_votes, candidate_votes

# Function to calculate vote percentages and identify the winner
def calculate_results(total_votes, candidate_votes):
    percentage_votes = []
    winner = max(candidate_votes, key=candidate_votes.get)

    for candidate, votes in candidate_votes.items():
        percentage = round((votes / total_votes) * 100, 3)
        percentage_votes.append(f"{candidate}: {percentage}% ({votes})")

    return percentage_votes, winner

# Function to print election results
def print_results(total_votes, percentage_votes, winner):
    print("Election Results")
    print("--------------------------")
    print(f"Total Votes: {total_votes}")
    print("--------------------------")
    print('\n'.join(percentage_votes))
    print("--------------------------")
    print(f"Winner: {winner}")
    print("--------------------------")

# Function to write results to a text file
def write_results(file_path, total_votes, percentage_votes, winner):
    with open(file_path, "w") as text_file:
        text_file.write("Election Results\n")
        text_file.write("--------------------------\n")
        text_file.write(f"Total Votes: {total_votes}\n")
        text_file.write("--------------------------\n")
        text_file.write('\n'.join(percentage_votes) + "\n")
        text_file.write("--------------------------\n")
        text_file.write(f"Winner: {winner}\n")
        text_file.write("--------------------------\n")

# Main execution
total_votes, candidate_votes = process_csv(csv_path)
percentage_votes, winner = calculate_results(total_votes, candidate_votes)
print_results(total_votes, percentage_votes, winner)
results_file = os.path.join('Analysis', 'results.txt')
write_results(results_file, total_votes, percentage_votes, winner)
