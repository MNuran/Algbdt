
# coding: utf-8

# In[1]:

import pandas as pd
Location = "C:\DataAnalitics\datasets-1\datasets/axisdata.csv"
df = pd.read_csv(Location)
df.head()


# In[2]:

df['Cars Sold'].mean()


# In[11]:

df['Cars Sold'].max()


# In[4]:

df['Cars Sold'].min()


# In[5]:

pd.pivot_table(df, values = ['Cars Sold'], index =['Gender'])


# In[6]:

df[df['Cars Sold']>3]['Hours Worked'].mean()


# In[7]:

df['Years Experience'].mean()


# In[8]:

df[df['Cars Sold']>3]['Years Experience'].mean()


# In[10]:

pd.pivot_table(df, values = ['Cars Sold'], index = ['SalesTraining'])


# In[ ]:



