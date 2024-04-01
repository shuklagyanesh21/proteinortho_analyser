import pandas as pd
import os

#Take user input for the tsv file
file_path = input("Enter the path to proteinortho result tsv file: ")
if not os.path.exists(file_path):
    print("File does not exist.")
    exit()

# Read the file into a DataFrame
df = pd.read_csv(file_path, delimiter="\t")

# Function to replace values based on conditions
def replace_value(cell_value):
    if "," in str(cell_value):
        comma_count = cell_value.count(",") # Count the number of commas
        replaced_value = "P" * (comma_count + 1) # Replace with "P" repeated (comma count + 1) times
    elif "__peg_" in str(cell_value):
        replaced_value = "P" # Replace with "P" if cell contains "__peg_"
    elif cell_value == "*":
        replaced_value = "A" # Replace "*" with "A"
    else:
        replaced_value = cell_value # No replacement needed
    return replaced_value

# Apply the function to cells in the dataframe
for column in df.columns:
    df[column] = df[column].apply(replace_value)
    
# Write the modified dataframe to a new TSV file
output_file_path = os.path.splitext(file_path)[0] + "_modified.tsv"
df.to_csv(output_file_path, sep="\t", index=False)

# Print a message confirming the write operation
filename = os.path.basename(file_path)
outname = os.path.basename(output_file_path)

print(filename + " has been modified and saved as " + outname)
