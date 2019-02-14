#!/usr/bin/env python
# coding: utf-8

# In[4]:


import os
import pandas as pd
import numpy as np


# In[8]:


read = pd.read_csv('02142019_203037-contact-details.csv')
read.columns


# In[10]:


contact = read[['Email','First Name','Last Name','Company Name']]
contact.head()


# In[14]:


contact_company = contact.dropna()
contact_company


# In[18]:


contact_company.to_csv('contact_company_021419.csv', sep=',', index=False)


# In[ ]:




