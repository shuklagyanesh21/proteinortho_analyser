# proteinortho_analyser

This repository contains tools to analyze the output TSV file from the Proteinortho tool. It counts the core, accessory, and unique genes in genomes and plots them for better visualization.

## Steps to Use

1. **Run the Python Script**:
    - Use `proteinortho_counter.py` to process the Proteinortho output TSV file.
    - The script will count the core, accessory, and unique genes for each species and append these counts to the bottom of the TSV file.
    - The updated TSV file will be saved with `_modified` appended to the original filename.

2. **Post-processing**:
    - The need to use Excel for calculations has been eliminated by the latest script changes, which now automatically count the core, accessory, and unique genes.

3. **Prepare Data for Plotting**:
    - Transpose and paste the species name column along with the counts of core, accessory, and unique genes into a new dataset.
    - This dataset can be used as input for `gene_category_plots.R` to generate visualizations.

## Usage Instructions

1. **Run the Python Script**:
    - Open a terminal and navigate to the directory containing `proteinortho_counter.py`.
    - Execute the script with the following command:
      ```sh
      python proteinortho_counter.py <path_to_your_tsv_file>
      ```

2. **Prepare Data for Plotting**:
    - After running the Python script, open the modified TSV file.
    - Copy the species names and the corresponding counts of core, accessory, and unique genes.
    - Transpose and paste this data to create a new dataset.
    - Use this new dataset as input for `gene_category_plots.R`.
