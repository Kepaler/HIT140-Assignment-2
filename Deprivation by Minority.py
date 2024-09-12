import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('dataset1.csv')
total_of_deprived = df['deprived'].value_counts()
total_of_minority = df['minority'].value_counts()

#Compare Minority by Deprivation
minority_deprived = df.groupby('minority')['deprived'].mean()
print(minority_deprived)

#Counting total of Minorities identifying as Deprived
depravity_by_minority = df[df['minority'] == 1]['deprived'].value_counts()

#Obtaining percentaile of each gender group which idetify as deprived (male=1 female=0)
percentage_depravity_by_minority = (depravity_by_minority / total_of_minority) * 100

print("Depravity by minority")
print(percentage_depravity_by_minority)

#Estimated percentage of experiencing depravity - majority = 11% && minority = 65% 

# Plot for Minoirty by Deprivation
sns.barplot(x='minority', y='deprived', data=df)
plt.title('Deprivation by Minority')
plt.show()