# -*- coding: utf-8 -*-
"""
Created on Sun Jun  6 23:43:55 2021

@author: Muhammet Fikret ATAR
"""
import pandas as pd
import numpy as np
import math
import matplotlib.pyplot as plt
from IPython.display import display
data = pd.read_csv('manufacturing_defects.txt', sep='\t', header = None)
#assign some  head this text 
data.columns =['order', 'years','1','2',
              '3','4','5','6',
              '7','8','9','10',
              '11','12','13','14']
             
#print (data)
#poisson predicted calculate fuction
def Poisson_predicted(number,lamda,totalnumber):
    return (math.exp(-lamda) * (lamda ** number) * totalnumber / math.factorial(number))
#problem a solution
print("\nA-)\n")
##remove the some headers
##zeronumbers=(data['1']==0).sum()
data = data.drop(columns="order")
data_edited = data.drop("years", axis=1)
total_zeros=(data_edited.values == 0).sum()
total_one=(data_edited.values == 1).sum()
total_two=(data_edited.values == 2).sum()
total_three=(data_edited.values == 3).sum()
total_four=(data_edited.values == 4).sum()

#print result of numbers of defects

data = {'\# ofDefects':['0', '1', '2', '3','4'], '\# of cases in all company between the years':[total_zeros, total_one, total_two, total_three,total_four]}  

#create df for A 
dataframeforA = pd.DataFrame(data) 
#print problem a table
print( dataframeforA.to_string(index=False))

#problem b solution
print("\nB-)\nEstimate λ from the given data\n")
#total value is total defects
total_value=data_edited.count().sum()
#total value of defects
sum_of_values=(total_one*1)+(total_two*2)+(total_three*3)+(total_four*4)
#estimate λ from the given data
ave=sum_of_values/total_value
#print problem b λ
print("λ->",ave)

#problem c solution
print("\nC-)\nPoisson predicted cases with the estimated λ\n")

#call pp fuction and print result

#create dict for q-)c
data = {'\# ofDefects':[0, 1, 2, 3,4], 
        '\# of cases in all company between the years':
        [total_zeros, total_one, total_two, total_three,total_four],
        'Predicted \# of cases in all companies between the years':[Poisson_predicted(0,ave,total_value)
                                                                   ,Poisson_predicted(1,ave,total_value)
                                                                   ,Poisson_predicted(2,ave,total_value),
                                                                  Poisson_predicted(3,ave,total_value)
                                                                   ,Poisson_predicted(4,ave,total_value)]}
                                      
#create df for q-)c  
dataframeforC = pd.DataFrame(data) 
#print problem c solution
print( dataframeforC.to_string(index=False))

#print("\nD-) \n")
#height of \# of cases
arr = dataframeforC['\# of cases in all company between the years'].to_numpy()
#height of \# of Predicted \# of cases
arr2= dataframeforC['Predicted \# of cases in all companies between the years'].to_numpy()
w=0.3 
# The x position of bars
r1 = np.arange(len(arr))
r2 = [x + w for x in r1]

# red bar
plt.bar(r1, arr, width = w, color = 'red', edgecolor = 'black', capsize=15, label='actual cases')
 
# blue bar
plt.bar(r2, arr2, width = w, color = 'blue', edgecolor = 'black', capsize=15, label='predicted cases')
 
#graphic editing operation
plt.xticks([r + w for r in range(len(arr))], ['0', '1', '2','3','4'])
plt.ylabel('# of Cases')
plt.xlabel('# of Defects')
plt.legend()
 
# Show graphic
plt.show()

