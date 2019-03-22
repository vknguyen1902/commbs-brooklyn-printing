#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os
import pandas as pd
import numpy as np
os.getcwd()


# In[5]:


read_connection = pd.read_csv('Connections.csv')
read_connection.head(5)


# In[6]:


read_contact = pd.read_csv('Contacts.csv')
read_contact.head(5)


# In[11]:


connection = read_connection[['First Name','Last Name']]
connection.head(5)


# In[28]:


contact = read_contact[['FirstName','LastName','Emails']]
contact.info()


# In[ ]:





# In[29]:


contact = contact.dropna()
contact.info()


# In[24]:


contact.to_csv('social_contacts.csv', sep=',', index=False)


# In[ ]:




