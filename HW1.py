
# coding: utf-8

# In[8]:

import pandas as pd

Location = "C:\DataAnalitics\datasets-1\datasets/algebradata.csv"
df = pd.read_csv(Location)
df.head()


# In[6]:

def grade_to_num(x):
    if x == 'A' :
        return 4
    if x == 'B' :
        return 3
    if x == 'C' :
        return 2
    if x == 'D' :
        return 1
    if x == 'F' :
        return 0
    
df['gradenum'] = df['Grade'].apply(grade_to_num)
num_students = df['Grade'].count()
num_students


# In[7]:

num_passing = df[df['gradenum']>1]
num_passing['Grade'].count()


# In[8]:

691/999.0


# In[11]:

pd.pivot_table(df[df['Gender'] == 'F'], values= ['Fname'], index=['Grade'], aggfunc='count',margins='True')


# In[12]:

(168+112+101)/518.0


# In[14]:

df['Hours of Study'].mean()


# In[24]:

df[df['Grade'] > 1]['Hours of Study'].mean()

