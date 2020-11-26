# --------------
#Header files
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Reading of the file
df=pd.read_csv(path)
data=df
# Code starts here

#Replacing '-' in the column with 'Agender
data['Gender'].replace(to_replace='-',value='Agender',inplace=True)

#Storing the value counts of 'Gender
gender_count=df['Gender'].value_counts()

#Plotting bar raph of 'gender_count'
plt.bar(gender_count.index,gender_count)
plt.show()


# Task 2
alignment=data['Alignment'].value_counts()


plt.figure(figsize=(6,6))

plt.pie(alignment,labels=alignment.index,explode=(0.05,0.05,0.05))

plt.title('Character Alignment')

plt.show()

#Task 3

sc_df=data[['Strength','Combat']].copy()
sc_covariance=sc_df.cov().iloc[0,1]

sc_strength=sc_df['Strength'].std()
sc_combat=sc_df['Combat'].std()

sc_pearson=sc_covariance/(sc_strength*sc_combat)
print('Pearson Coefficient between Strength & Combat: ',sc_pearson)

# between intelligence and combat

ic_df=data[['Intelligence','Combat']].copy()
ic_covariance=ic_df.cov().iloc[0,1]

ic_intelligence=ic_df['Intelligence'].std()
ic_combat=ic_df['Combat'].std()

ic_pearson=ic_covariance/(ic_intelligence*ic_combat)
print('Pearson Coefficient between Intelligence & Combat: ',ic_pearson)

#Task 4
total_high=data['Total'].quantile(q=0.99)

super_best=data[data['Total']>total_high]

super_best_names=list(super_best['Name'])

print(super_best_names)




