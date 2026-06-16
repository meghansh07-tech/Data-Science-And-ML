import matplotlib.pyplot as plt

import pandas as pd
import numpy as np
# Create dataframe
K=pd.Series([1,2,3,4,5,6],['A1','B1','C1','D1','E1','F1'])
data = {'Company':['GOOG','GOOG','MSFT','MSFT','FB','FB'],
       'Person':['Sam','Charlie','Amy','Vanessa','Carl','Sarah'],
       'Sales':[200,120,340,124,243,350]}
df = pd.DataFrame(data, ['A','B','C','D','E','F'],columns=['Company','Person','Sales'])
print(K)
print(df)
wind= 'CA NY WY OR CO BH'.split()
df['states'] = wind
df.set_index('states')
print(df)
m=df['Sales'].sum()
print("Sum of sales=" ,m)
i=df.loc['A','Sales']
j=df.loc['B','Sales']
print(i*j)
print(df.groupby('Company').count())
t=pd.concat([df,K])
print(t)
print(t.dropna())
a,b=int(input('Enter a number: ')),int(input('Enter another number: '))
c=a/b
print(c)
x=np.arange(1,11,1)
y=np.arange(1,11,1)
plt.plot(x,y,'r-')
plt.plot(x,c,'b-')
plt.show()
