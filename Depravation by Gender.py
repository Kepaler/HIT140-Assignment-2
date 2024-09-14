import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from scipy.stats import chi2_contingency


# Read CSV fil
df = pd.read_csv('dataset1.csv')
total_of_gender = df['gender'].value_counts()
total_of_deprived = df['deprived'].value_counts()

#Obtain total of participants
def participant_count():
    participant_total = 0
    for i in df['ID']:
        participant_total += 1
    print(participant_total)

#Obtain total of participants who identify as Male & total of  participants who idetify as non-male
def participant_gender_count():
    participant_gender_male = 0
    participant_gender_non_male = 120115
    for i in df['gender']:
        if i == 0:
            participant_gender_male += 1
    print("\nTotal Male Participants")
    print(participant_gender_male)
    
    #Updates non-malesample size
    participant_gender_non_male -= participant_gender_male
    print("\nTotal of participants that identify as non-male")
    print(participant_gender_non_male)

#Compare Gender by Deprivation function
def gender_to_depravity_graph():
    gender_deprived = df.groupby('gender')['deprived'].mean()
    print(gender_deprived)

    #Counting total of Gender identifying as Deprived
    depravity_by_gender = df[df['gender'] == 1]['deprived'].value_counts()

    #Obtaining percentaile of each gender group which idetify as deprived (male=0 female=1)
    percentage_depravity_by_gender = (depravity_by_gender / total_of_gender) * 100

    print("\nDepravity by gender")
    
    # % of genders idetifying as experincing deprivation - Other = 52% && Male = 43%
    print(percentage_depravity_by_gender)

    # Plot for Gender
    sns.barplot(x='gender', y='deprived', data=df)
    plt.title('Deprivation by Gender')
    plt.show()

#Chi-Square inferential statistic analysis function
def chi_square_inferential_statistic():

    # Creating a contingency table for Gender and Deprivation
    contingency_table = pd.crosstab(df['gender'], df['deprived'])

    # Performing Chi-Square Test
    chi2, p, dof, expected = chi2_contingency(contingency_table)

    # Output of results
    print(f"\nChi-square statistic:{chi2}")
    print(f"\np-value:{p}")
    print(f"\nDegrees of freedom:{dof}")
    print(f"\nExpected frequencies:\n{expected}")

participant_count()
participant_gender_count()
gender_to_depravity_graph()
chi_square_inferential_statistic()
