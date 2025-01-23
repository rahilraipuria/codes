import csv
# Read the training data from the CSV file
with open("findS.csv") as f:
    csv_file = csv.reader(f)
    data = list(csv_file)
# Initialize specific and general hypotheses
specific = data[1][:-1] # Assume first positive example as the specific hypothesis
general = [['?' for _ in specific] for _ in specific] # General hypothesis initialized
# Process each training example
for i in data:
    if i[-1] == "Yes":
 # For positive examples, generalize the specific hypothesis
        for j in range(len(specific)):
            if i[j] != specific[j]:
                specific[j] = "?" # Make specific hypothesis more general
                general[j][j] = "?" # Set general hypothesis to '?' where mismatch occurs
    else:
 # For negative examples, specialize the general hypothesis
        for j in range(len(specific)):
            if i[j] != specific[j]:
                general[j][j] = specific[j] # Set general hypothesis to specific value where mismatch occurs
            else:
                general[j][j] = "?" # Keep '?' where there's no mismatch
print(f"\nStep {data.index(i)+1} of Candidate Elimination Algorithm")
print(f"Specific Hypothesis: {specific}")
print(f"General Hypothesis: {general}")
# Remove all redundant general hypotheses that contain only '?'
final_general = [g for g in general if '?' in g]
# Print the final results
print("\nFinal Specific Hypothesis:", specific)
print("\nFinal General Hypothesis:", final_general)