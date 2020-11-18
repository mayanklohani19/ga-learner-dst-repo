# --------------
#Importing header files
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


#Reading the file
data=pd.read_csv(path)

#Code starts here

# Step 1 
#Reading the file


#Creating a new variable to store the value counts
loan_status=data['Loan_Status'].value_counts()
# print(data.iloc[25,1])
# print(data.iloc[53,9])
# print(loan_status[0])
# print(loan_status[1])

#Plotting bar plot
loan_status.plot(kind='bar')
plt.show()

# Step 2
#Plotting an unstacked bar plot
property_and_loan=data.groupby(['Property_Area', 'Loan_Status']).size().unstack()
property_and_loan.plot(kind='bar', stacked=False)

#Changing the x-axis label
plt.xlabel('Property_Area')

#Changing the y-axis label
plt.ylabel('Loan_Status')

#Rotating the ticks of X-axis
plt.xticks(rotation=45)
plt.show()

# Step 3
#Plotting a stacked bar plot
property_and_loan.plot(kind='bar', stacked=True)

#Changing the x-axis label
plt.xlabel('Property_Area')

#Changing the y-axis label
plt.ylabel('Loan_Status')

#Rotating the ticks of X-axis
plt.xticks(rotation=45)
plt.show()

# Step 4 
#Subsetting the dataframe based on 'Education' column
education_and_loan=data.groupby(['Education','Loan_Status']).size().unstack()

#Plotting density plot for 'Graduate'
education_and_loan.plot(kind='bar', stacked=True)

#Plotting density plot for 'Graduate'
plt.xlabel('Eduaction')
plt.ylabel('Loan_Status')
plt.xticks(rotation=45)
plt.show()

#For automatic legend display


# Step 5
#Setting up the subplots
graduate=pd.DataFrame(data[data['Education']=='Graduate'])

not_graduate=pd.DataFrame(data[data['Education']=='Not Graduate'])

graduate['LoanAmount'].plot(kind='density', label='Graduate')

not_graduate['LoanAmount'].plot(kind='density', label='Not Graduate')

# Income vs Loan

fig, (ax_1, ax_2, ax_3) = plt.subplots(nrows = 3 , ncols = 1)

#Plotting scatter plot

ax_1.scatter(data['ApplicantIncome'],data["LoanAmount"])
ax_1.set_title('Applicant Income')


ax_2.scatter(data['CoapplicantIncome'],data["LoanAmount"])
ax_2.set_title('Coapplicant Income')


data['TotalIncome']=data['CoapplicantIncome'] + data["ApplicantIncome"]
ax_3.scatter(data['TotalIncome'],data["LoanAmount"])
ax_3.set_title('Total Income')

plt.show()









