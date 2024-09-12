import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Read CSV fil
df = pd.read_csv('dataset1.csv')
total_of_gender = df['gender'].value_counts()
total_of_deprived = df['deprived'].value_counts()

#Compare Gender by Deprivation
gender_deprived = df.groupby('gender')['deprived'].mean()
print(gender_deprived)

#Counting total of Gender identifying as Deprived
depravity_by_gender = df[df['gender'] == 1]['deprived'].value_counts()

#Obtaining percentaile of each gender group which idetify as deprived (male=0 female=1)
percentage_depravity_by_gender = (depravity_by_gender / total_of_gender) * 100

print("Depravity by gender")
print(percentage_depravity_by_gender)

# % of genders idetifying as experincing deprivation - Other = 52% && Male = 43%

# Plot for Gender
sns.barplot(x='gender', y='deprived', data=df)
plt.title('Deprivation by Gender')
plt.show()
