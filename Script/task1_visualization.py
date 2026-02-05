# Step 0: Import libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_style("whitegrid")  # optional: nicer plots

# Step 1: Load CSV (update with your exact file name)
file_path = r"C:\Users\admin\Documents\Prodigy Infotech\Task1 datasets\demographics.csv"
df = pd.read_csv(file_path)

# Step 2: Quick look at dataset
print("✅ Dataset loaded successfully!")
display(df.head())
print("\nColumns:", df.columns)

# Get the count of counties per state
state_counts = df['State'].value_counts()

# Create a color palette with as many colors as there are states
palette_colors = sns.color_palette("viridis", n_colors=len(state_counts))

# Step 3: Bar chart for categorical variable (Number of Counties per State)
plt.figure(figsize=(12,6))
sns.countplot(data=df, x='State', hue='State',order=state_counts.index, palette=palette_colors)
plt.title('Number of Counties per State')
plt.xlabel('State')
plt.ylabel('Count of Counties')
plt.xticks(rotation=90)
plt.show()

# Step 4: Histogram for continuous variable (Total Population)
plt.figure(figsize=(12,6))
sns.histplot(df['Total Population'].dropna(), bins=30, kde=True, color='skyblue')
plt.title('Distribution of Total Population')
plt.xlabel('Total Population')
plt.ylabel('Frequency')
plt.show()
