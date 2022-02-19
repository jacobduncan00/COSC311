import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# Draws 4 histograms for >50K & <=50K distributions for education and age
def histograms(adult_frame):
    aei = adult_frame[['age', 'education-num', 'income']]
    over = aei[aei['income'] == '>50K']
    under = aei[aei['income'] == '<=50K']
    # ----------------------------------------------------------
    over_hist_plot_edu = plt.figure("Education Distribution >50K")
    plt.title('Distribution of >50K')
    plt.xlabel('Years of education')
    plt.ylabel('# Of people per bin')
    over_hist_edu = over['education-num'].hist(bins=15)
    # ----------------------------------------------------------
    under_hist_plot_edu = plt.figure("Education Distribution <=50K")
    plt.title('Distribution of Lower Class')
    plt.xlabel('Years of education')
    plt.ylabel('# Of people per bin')
    under_hist_edu = under['education-num'].hist(bins=15)
    # ----------------------------------------------------------
    over_hist_plot_age = plt.figure("Age Distribution >50K")
    plt.title('Distribution of >50K')
    plt.xlabel('Age')
    plt.ylabel('# Of people per bin')
    over_hist_age = over['age'].hist(bins=15)
    # ----------------------------------------------------------
    under_hist_plot_age = plt.figure("Age Distribution <=50K")
    plt.title('Distribution of <=50K')
    plt.xlabel('Age')
    plt.ylabel('# Of people per bin')
    under_hist_age = under['age'].hist(bins=15)
    # ----------------------------------------------------------
    plt.show()


def yearsOfEducation(adult_frame):
    aei = adult_frame[['age', 'education-num', 'income']]
    over = aei[aei['income'] == '>50K']
    under = aei[aei['income'] == '<=50K']

    # Median and mean for years of education for those over 50k
    over_median = np.median(over.loc[:, 'education-num'].tolist())
    over_mean = np.mean(over.loc[:, 'education-num'].tolist())

    # Median and mean for years of education for those under or equal to 50k
    under_median = np.median(under.loc[:, 'education-num'].tolist())
    under_mean = np.mean(under.loc[:, 'education-num'].tolist())

    print('*** Upper Income Years Of Education Held ***')
    print('    Mean: ', over_mean, 'years')
    print('    Median: ', over_median, 'years', end='\n\n')

    print('*** Lower Income Years Of Education Held ***')
    print('    Mean: ', under_mean, 'years')
    print('    Median: ', under_median, 'years')


def medianAge(adult_frame):
    asi = adult_frame[['age', 'sex', 'income']]
    over = asi[asi['income'] == '>50K']
    under = asi[asi['income'] == '<=50K']

    # Median for both male and female
    over_median = np.median(over.loc[:, 'age'].tolist())
    under_median = np.median(under.loc[:, 'age'].tolist())

    # Median for over & under for males
    male_over_median = np.median(
        over[over['sex'] == 'Male'].loc[:, 'age'].tolist())
    male_under_median = np.median(
        under[under['sex'] == 'Male'].loc[:, 'age'].tolist())

    # Median for over & under for females
    female_over_median = np.median(
        over[over['sex'] == 'Female'].loc[:, 'age'].tolist())
    female_under_median = np.median(
        under[under['sex'] == 'Female'].loc[:, 'age'].tolist())

    # Pretty print results
    print("\n|******** Median Ages ********|")
    print("|Income:     >50K      <=50K  |")
    print("|-----------------------------|")
    print("|Male  | ", male_over_median,
          male_under_median, sep="     ", end="   |\n")
    print("|Female| ", female_over_median,
          female_under_median, sep="     ", end="   |\n")
    print("|Both  | ", over_median,
          under_median, sep="     ", end="   |\n")
    print("|*****************************|\n")


def rankOccupation(adult_frame):
    # Subset the dataframe to only include the occupation and income column
    occupation_income = adult_frame[['occupation', 'income']]
    over = occupation_income[occupation_income['income']
                             == '>50K'].groupby('occupation').count()
    under = occupation_income[occupation_income['income']
                              == '<=50K'].groupby('occupation').count()

    combinedTotal = []
    for pair in zip(over['income'].tolist(), under['income'].tolist()):
        combinedTotal.append(sum(pair))

    # Get unique occupations
    unique_occupations = sorted(set(occupation_income['occupation']))

    ratio = list(zip([pair[0]/pair[1]
                      for pair in zip(over['income'].tolist(), combinedTotal)], unique_occupations))

    # Getting rid of the '?' data as it is unneeded
    ratio.pop(0)

    print("Occupations ranked most to least likely to make over $50k anually:")
    c = 1
    for i in sorted(ratio, reverse=True):
        print(f"{c}.", i[1], end='\n')
        c += 1


def main():
    adult_frame = pd.read_csv("adult.data", header=None,
                              skipinitialspace=True,  # this data has some extra whitespace
                              names=['age', 'workclass', 'fnlwgt', 'education',
                                     'education-num', 'marital-status',
                                     'occupation', 'relationship', 'race',
                                     'sex', 'capital_gain', 'capital_loss',
                                     'hr_per_week', 'country', 'income'
                                     ])
    # Tasks
    rankOccupation(adult_frame)  # (a)
    medianAge(adult_frame)  # (b)
    yearsOfEducation(adult_frame)  # (c)
    histograms(adult_frame)  # (d & e)


if __name__ == "__main__":
    main()
