import pandas as pd
import os

# Set the working directory
os.chdir(r"D:\PhD_1st_Year\Data\protein_ortho")

# Read the file into a DataFrame
df = pd.read_csv("myxo_87.proteinortho.tsv", delimiter="\t")

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
df.to_csv("final2.tsv", sep="\t", index=False)

# Print a message confirming the write operation
print("DataFrame has been written to final.tsv")
