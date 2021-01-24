# --------------
#Importing header files
import pandas as pd
import scipy.stats as stats
import math
import numpy as np
import matplotlib.pyplot as plt
from statsmodels.stats.weightstats import ztest
from statsmodels.stats.weightstats import ztest
from scipy.stats import chi2_contingency

import warnings

warnings.filterwarnings('ignore')
#Sample_Size
sample_size=2000

#Z_Critical Score
z_critical = stats.norm.ppf(q = 0.95)  

# Critical Value
# critical_value = stats.chi2.ppf(q = 0.95, # Find the critical value for 95% confidence*
#                       df = 6)   # Df = number of variable categories(in purpose) - 1

#Reading file
data=pd.read_csv(path)

#Code starts here
data_sample=data.sample(n=sample_size,random_state=0)

sample_mean=data_sample['installment'].mean()

sample_std=data_sample['installment'].std()
margin_of_error=z_critical*(sample_std/math.sqrt(sample_size))

confidence_interval=(sample_mean-margin_of_error, sample_mean+ margin_of_error)

print(confidence_interval)

true_mean=data['installment'].mean()
print(true_mean)

sample_size=np.array([20,50,100])

fig,axes=plt.subplots(3,1,figsize=(10,20))

for i in range(len(sample_size)):

    m=[]

    for j in range(1000):

        mean=data['installment'].sample(sample_size[i]).mean()

        m.append(mean)

    mean_series=pd.Series(m)

    axes[i].hist(mean_series,normed=True)

plt.show()


#Task 3
data['int.rate']=data['int.rate'].map(lambda x: str(x)[:-1])

data['int.rate']=data['int.rate'].astype(float)/100

z_statistic_1,p_value_1=ztest(x1=data[data['purpose']=='small_business']['int.rate'],value=data['int.rate'].mean(),alternative='larger')

print(z_statistic_1)
print(p_value_1)

#Installment vs Loan Defaulting

z_statistic_2,p_value_2=ztest(x1=data[data['paid.back.loan']=='No']['installment'],x2=data[data['paid.back.loan']=='Yes']['installment'])

print(z_statistic_2)
print(p_value_2)









