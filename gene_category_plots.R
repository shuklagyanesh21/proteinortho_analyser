library(ggplot2)
library(tidyr)
library(dplyr)
# Load the data
df <- read.csv("D:/PhD_1st_Year/Data/protein_ortho/myxo_87.proteinortho_category.csv", header = T)

# Transform data from wide to long format
df_long <- pivot_longer(df, cols = c("Core.genes", "Accessory.genes", "Unique.genes"), names_to = "Gene_Type", values_to = "Count")

# Generate stacked bar plot
ggplot(df_long, aes(x = X, y = Count, fill = `Gene_Type`)) +
  geom_bar(stat = "identity") +
  theme(axis.text.x = element_text(angle = 45, hjust = 1)) +
  labs(title = "Orthologous genes in myxo_87 dataset", x = "Organism", y = "Count")

# Save the plot
ggsave("D:/PhD_1st_Year/Data/protein_ortho/myxo87_proteinortho_barplot.png", width = 13, height = 6)


######Box-Plot##################################################################

ggplot(df_long, aes(x = Gene_Type, y = Count, fill = Gene_Type)) +
  geom_boxplot() +
  labs(title = "Orthologous genes in myxo_87 dataset", x = "Gene_Type", y = "Count")

# Save the plot
ggsave("D:/PhD_1st_Year/Data/protein_ortho/myxo87_proteinortho_boxplot.png", width = 8, height = 6)


######Percentage Box-Plot##################################################################

# Calculate the percentage of each gene type within each organism
df_long <- df_long %>%
  group_by(X) %>%
  mutate(Total = sum(Count)) %>%
  ungroup() %>%
  mutate(Percentage = (Count / Total) * 100)

# Generate stacked bar plot with percentages
ggplot(df_long, aes(x = X, y = Percentage, fill = `Gene_Type`)) +
  geom_bar(stat = "identity") +
  theme(axis.text.x = element_text(angle = 45, hjust = 1)) +
  labs(title = "Percentage of Gene Types for Organisms", x = "Organism", y = "Percentage")

# Save the plot
ggsave("D:/PhD_1st_Year/Data/protein_ortho/myxo87_proteinortho_100barplot.png", width = 13, height = 6)
