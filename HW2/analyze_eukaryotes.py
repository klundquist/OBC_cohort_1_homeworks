import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("eukaryotes.tsv", sep="\t")

stats = df['Size (Mb)'].describe()
print("Statistics for 'Size (Mb)':")
print(stats)

humans = df[df['Species'] == "Homo sapiens"]
print("\nHomo sapiens:")
print(humans)

# Converts 'Number of genes' to numeric, coercing errors to NaN
df['Number of genes'] = pd.to_numeric(df['Number of genes'], errors='coerce')
# Computes the correlation between Size (Mb) and Number of genes
correlation = df[['Size (Mb)', 'Number of genes']].corr()
print(f"\ncorrelation['Size (Mb)']['Number of genes']: {correlation['Size (Mb)']['Number of genes']}")

small_genomes = df[df['Size (Mb)'] < 5000]
print("\nSmall genomes:")
print(small_genomes)

# Replace '-' with NaN and convert to numeric
df['Number of genes'] = pd.to_numeric(df['Number of genes'], errors='coerce')

# Drop rows with missing values in relevant columns
df_clean = df.dropna(subset=['Number of genes', 'Size (Mb)'])

# Plot
plt.figure(figsize=(10, 6))
sns.scatterplot(data=df_clean, x='Size (Mb)', y='Number of genes')
plt.title('Number of Genes vs. Genome Size')
plt.xlabel('Genome Size (Mb)')
plt.ylabel('Number of Genes')
plt.tight_layout()
plt.savefig('genome_plot.png')
