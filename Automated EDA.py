#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().system('pip install jupyter notebook')


# In[2]:


get_ipython().system('pip install dtale')


# In[5]:


import pandas as pd
import dtale


# In[6]:


import seaborn as sns


# In[7]:


df=sns.load_dataset('titanic')


# In[8]:


df.head()


# In[10]:


dtale.show(df)


# In[ ]:




