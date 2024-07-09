import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the CSV file
content_df = pd.read_csv('datasets/Content.csv')
reactions_df = pd.read_csv('datasets/Reactions.csv')
reactiontype_df = pd.read_csv('datasets/ReactionTypes.csv')

#print(content_df.isnull().sum())
#print(reactions_df.isnull().sum())
#print(reactiontype_df.isnull().sum())

# Calculate percentage of null values in each column
null_percentage = content_df.isnull().mean() * 100

# Plotting the null percentages
plt.figure(figsize=(10, 6))
sns.barplot(x=null_percentage.index, y=null_percentage)
plt.xticks(rotation=90)
plt.xlabel('Column name')
plt.ylabel('Percentage of Null Values')
plt.title('Percentage of Null Values by Column')
plt.tight_layout()
plt.show()

