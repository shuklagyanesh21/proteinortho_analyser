import pandas as pd
import os

# Set the working directory
os.chdir(r"D:\PhD_1st_Year\Data\protein_
# Read the TSV file
df = pd.read_csv("myxo_87.proteinortho.tsv", sep="\t")

# Function to replace values with "P" based on comma count
def replace_with_P(cell_value):
    comma_count = cell_value.count(",") # Count the number of commas
    replaced_value = "P" * (comma_count + 1) # Replace with "P" repeated (comma count + 1) times
    return replaced_value

# Apply the function to cells containing commas
for column in df.columns:
    df[column] = df[column].apply(lambda x: replace_with_P(x) if "," in str(x) else x)

# Write the modified dataframe to a new TSV file
df.to_csv("final.tsv", sep="\t", index=False)

# Print a message confirming the write operation
print("DataFrame has been written to final.tsv")
