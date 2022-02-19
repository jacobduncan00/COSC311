import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def rankOccupation(adult_frame):
    occupation_income = adult_frame[['occupation', 'income']]
    over = occupation_income[occupation_income['income']
                             == '>50K'].groupby('occupation').count()
    under = occupation_income[occupation_income['income']
                              == '<=50K'].groupby('occupation').count()
    print(over)
    print(under)


def main():
    adult_frame = pd.read_csv("adult.data", header=None,
                              skipinitialspace=True,  # this data has some extra whitespace
                              names=['age', 'workclass', 'fnlwgt', 'education',
                                     'education-num', 'marital-status',
                                     'occupation', 'relationship', 'race',
                                     'sex', 'capital_gain', 'capital_loss',
                                     'hr_per_week', 'country', 'income'
                                     ])
    rankOccupation(adult_frame)


if __name__ == "__main__":
    main()
