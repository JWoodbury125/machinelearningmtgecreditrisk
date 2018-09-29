
# coding: utf-8

# In[14]:


import pandas as pd
import csv
data = pd.read_csv('C:/Users/Jennifer/Desktop/CS691/hmda_lar.csv')
df = pd.DataFrame(data)
df


# In[18]:


df.columns


# In[24]:


df.describe()


# In[67]:


df[['denial_reason_name_1','state_abbr']][(df.applicant_income_000s>=300)].describe()

