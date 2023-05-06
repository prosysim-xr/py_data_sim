import numpy as np
import pandas as pd

# get dataframe for  company
emp_df = pd.read_csv('./_1References/employees.csv')
dept_policy_df = pd.read_csv('./_1References/dept_policy.csv')
emp_df = pd.read_csv('./_1References/employees.csv')

s = pd.Series([1, 3, 5, np.nan, 6, 8])

currentExpectedTargets =  emp_df.groupby(['dept', 'seniority']).get_group(
    ('IT','junior'))['expected_targets'].item()
print(currentExpectedTargets )