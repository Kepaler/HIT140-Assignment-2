import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Read CSV fil
df = pd.read_csv('dataset1.csv')
total_of_gender = df['gender'].value_counts()
total_of_minority = df['minority'].value_counts()

#Compare Minority by Gender and Display in Graph
minority_gender = df.groupby("minority")['gender'].mean()
print(minority_gender)

#Counting number of minorities within each gender
minorities_by_gender = df[df['minority'] == 1]['gender'].value_counts()

#Obtaining percentaile of each gender group which idetify as a minority male=1 other=0
percentage_minority_by_gender = (minorities_by_gender / total_of_gender) * 100
print(percentage_minority_by_gender)

#Estimated gender idetifying as minority ethnic group -- other = 25% && male = 23%

# Plot for Minority by Gender
sns.barplot(x='minority', y='gender', data=df)
plt.title('Minority by Gender')
plt.show()