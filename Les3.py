
# coding: utf-8

# In[3]:

import pandas as pd
import matplotlib.pyplot as plt
import numpy.random as np
import sys

get_ipython().magic(u'matplotlib inline')
print ('Python version' + sys.version)
print ('Pandas version: ' + pd.__version__)


# In[7]:

np.seed(111)

def CreateDataSet(Number=1):
    Output = []
    for i in range(Number):
        rng = pd.date_range(start='1/1/2009', end = '12/31/2012', freq = 'W-MON')
        
        data = np.randint(low=25,high=1000,size=len(rng))
        status = [1,2,3]
        
        random_status = [status[np.randint(low=0,high=len(status))] for i in range(len(rng))]
        
        states = ['GA','FL','fl','NY','NJ','TX']
        
        random_states = [states[np.randint(low=0,high=len(states))]for i in range(len(rng))]
            
        Output.extend(zip(random_states, random_status,data,rng))
        
        return Output


# In[6]:

dataset = CreateDataSet(4)
df = pd.DataFrame(data=dataset, columns = ['State','Status','CustomerCount','StatusDate'])
df.info()


# In[8]:

df.to_excel('Lesson3.xlsx', index = False)
print('Done')


# In[10]:

import os
path = os.path.abspath(os.curdir)
print(path)
files = os.listdir(os.curdir)
for file in files :
    print(file)


# In[11]:

get_ipython().magic(u'pinfo pd.read_excel')


# In[13]:

Location = path + r'\Lesson3.xlsx'
print(Location)

df = pd.read_excel(Location, 0, index_col='StatusDate')
df.dtypes


# In[14]:

df.index
df.head()


# In[16]:

df['State'].unique()
df['State'] = df.State.apply(lambda x: x.upper())
df['State'].unique()
mask = df['Status'] ==1
df = df[mask]
mask = df.State =='NJ'
df['State'][mask] = 'NY'


# In[17]:

df['State'].unique()
df['CustomerCount'].plot(figsize=(15,5));
sortdf= df[df['State']== 'NY'].sort_values(['CustomerCount'], axis=0)
sortdf.head(10)


# In[18]:

Daily = df.reset_index().groupby(['State','StatusDate']).sum()
Daily.head()


# In[19]:

Daily.head()
Daily.index
Daily.index.levels[0]
Daily.index.levels[1]


# In[20]:

Daily.loc['FL'].plot()
Daily.loc['GA'].plot()
Daily.loc['NY'].plot()
Daily.loc['TX'].plot()


# In[21]:

Daily.loc['FL']['2012':].plot()
Daily.loc['GA']['2012':].plot()
Daily.loc['NY']['2012':].plot()
Daily.loc['TX']['2012':].plot()


# In[29]:

StateYearMonth = Daily.groupby([Daily.index.get_level_values(0),
                              Daily.index.get_level_values(1).year,
                              Daily.index.get_level_values(1).month])
Daily['Lower'] = StateYearMonth['CustomerCount'].transform(lambda x: x.quantile(q=.25)
                                                          - (1.5*x.quantile(q=.75)-x.quantile(q=.25)) )

Daily['Upper'] = StateYearMonth['CustomerCount'].transform(lambda x: x.quantile(q=.75)
                                                           + (1.5*x.quantile(q=.75)-x.quantile(q=.25)) )
Daily['Outlier'] = (Daily['CustomerCount']<
                   Daily['Lower']) | (Daily['CustomerCount'] > Daily['Upper'])

Daily = Daily[Daily['Outlier'] == False]
Daily.head()


# In[ ]:




# In[ ]:



