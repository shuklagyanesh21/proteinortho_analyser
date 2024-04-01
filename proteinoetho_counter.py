import pandas as pd
import os

file_path = input("Enter the path to proteinortho result tsv file: ")
if not os.path.exists(file_path):
    print("File does not exist.")
    exit()

# Read the file into a DataFrame
df = pd.read_csv(file_path, delimiter="\t")

# Function to replace values based on conditions
def replace_value(cell_value):
    if "," in str(cell_value): 			 # For organisms with multiple genes
        comma_count = cell_value.count(",") 
        replaced_value = "P" * (comma_count + 1) # Genes are 'one' more than the comma number
    elif "__peg_" in str(cell_value):
        replaced_value = "P" 			 # Now only single gene organisms left so extract any word
    elif cell_value == "*":
        replaced_value = "A"
    else:
        replaced_value = cell_value 		 # No replacement needed
    return replaced_value
    
# Apply the function to columns one-by-one
for column in df.columns:
    df[column] = df[column].apply(replace_value)
    
# Function to determine category of genes
def determine_category(row):
    if "A" not in row.values:
        return "core"
    elif row.tolist().count("P") == 1:  # convert rows to list then count P
        return "unique"
    else:
        return "accessory"

# Apply the function row-wise to create the 'category' column
df['category'] = df.apply(determine_category, axis=1)

# Write the modified dataframe to a new TSV file
output_file_path = os.path.splitext(file_path)[0] + "_modified.tsv"
df.to_csv(output_file_path, sep="\t", index=False)

# Print a message confirming the write operation
filename = os.path.basename(file_path)
outname = os.path.basename(output_file_path)
print(filename + " has been modified and saved as " + outname)
