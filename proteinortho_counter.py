import pandas as pd
import os
import argparse

# Set up argument parser
parser = argparse.ArgumentParser(description="Process proteinortho result tsv file.")
parser.add_argument("file_path", type=str, help="Path to the proteinortho result tsv file.")

# Parse arguments
args = parser.parse_args()
file_path = args.file_path
if not os.path.exists(file_path):
    print("File does not exist.")
    exit()
df = pd.read_csv(file_path, delimiter="\t")

# Function to replace values based on conditions
def replace_value(cell_value):
    if "," in str(cell_value):                    # For organisms with multiple genes
        comma_count = cell_value.count(",")
        replaced_value = "P" * (comma_count + 1) # Genes are 'one' more than the comma number
    elif "__peg_" in str(cell_value):             # Now only single gene organisms left so extract any word
        replaced_value = "P"                      # Change __peg_ to whatever is your header name standard
    elif cell_value == "*":
        replaced_value = "A"
    else:
        replaced_value = cell_value               # No replacement needed
    return replaced_value

# Apply the function to columns one-by-one
for column in df.columns:
    df[column] = df[column].apply(replace_value)

# Function to determine category of genes
def determine_category(row):
    p_count = sum(str(value).count("P") for value in row.values)  # Count total occurrences of 'P' in all cells
    if p_count == 1:
        return "unique"
    elif "A" not in row.values:
        return "core"
    else:
        return "accessory"

# Apply the function row-wise to create the 'category' column
df['category'] = df.apply(determine_category, axis=1)

# Count 'P' in each category for each species column
species_columns = df.columns[3:-1]  # Exclude first three columns and 'category' column
category_counts = {category: {col: 0 for col in species_columns} for category in ['core', 'accessory', 'unique']}

for _, row in df.iterrows():
    category = row['category']
    for col in species_columns:
        category_counts[category][col] += str(row[col]).count('P')

# Append counts to the dataframe
core_counts = [""] * 3 + [category_counts['core'][col] for col in species_columns]
accessory_counts = [""] * 3 + [category_counts['accessory'][col] for col in species_columns]
unique_counts = [""] * 3 + [category_counts['unique'][col] for col in species_columns]

df.loc[len(df)] = core_counts + ["Core genes"]
df.loc[len(df)] = accessory_counts + ["Accessory genes"]
df.loc[len(df)] = unique_counts + ["Unique genes"]

# Write the modified dataframe to a new TSV file
output_file_path = os.path.splitext(file_path)[0] + "_modified.tsv"
df.to_csv(output_file_path, sep="\t", index=False)

# Print a message confirming the write operation
filename = os.path.basename(file_path)
outname = os.path.basename(output_file_path)
print(filename + " has been modified and saved as " + outname)
