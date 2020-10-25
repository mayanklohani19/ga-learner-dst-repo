# --------------
# Importing header files
import numpy as np
import pandas as pd
from scipy.stats import mode 
 
import warnings
warnings.filterwarnings('ignore')

#Reading file
bank= pd.read_csv(path)

#Code starts here
categorical_var=bank.select_dtypes(include = 'object')

numerical_var=bank.select_dtypes(include = 'number')
# categorical_var.shape
# numerical_var.shape

# #STEP 2
banks=bank.drop(columns='Loan_ID')
print(banks.isnull().sum())
bank_mode=banks.mode().iloc[0]
banks=banks.fillna(bank_mode)

# STEP 3
avg_loan_amount = pd.pivot_table(banks,index=['Gender','Married','Self_Employed'],values='LoanAmount',aggfunc='mean')
# print(avg_loan_amount)

# STEP 4
loan_approved_se = len(banks[(banks['Self_Employed'] == 'Yes') & (banks['Loan_Status']== 'Y')])

loan_approved_nse = len(banks[(banks['Self_Employed'] == 'No') & (banks['Loan_Status'] == 'Y')])

percentage_se = (loan_approved_se * 100)/614
percentage_nse = (loan_approved_nse * 100)/614




#STEP 
loan_term = banks['Loan_Amount_Term'].apply(lambda x: (x/12))
big_loan_term = len(loan_term[loan_term >= 25])


#STEP 6

loan_groupby=banks.groupby(['Loan_Status'])

loan_groupby=loan_groupby['ApplicantIncome','Credit_History']

mean_values=loan_groupby.agg([np.mean])

print(mean_values)





