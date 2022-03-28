#!/usr/bin/env python
# coding: utf-8

# In[1]:


#importing libraries
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sb


# # Assignment 2

# In[3]:


#Importing data
IBM_Attrition = pd.read_csv ("D:/ADS/Assignment 2 and 3/ADS-Assignment-2-3-main/WA_Fn-UseC_-HR-Employee-Attrition.csv")
IBM_Attrition


# In[5]:


#displaying first 5 rows
IBM_Attrition.head ()


# In[6]:


#Displaying last 5 rows
IBM_Attrition.tail ()


# In[10]:


#Factors that lead to employee attrition data types
IBM_Attrition.dtypes


# In[11]:


#Checking for missing values
IBM_Attrition.isnull().sum()


# In[39]:


Dist_by_JobRole_Attrition = IBM_Attrition.groupby(
    ["JobRole","Attrition"])["DistanceFromHome"].sum()
Dist_by_JobRole_Attrition


# In[41]:


Monthly_Income_By_Edu_and_Attrition = IBM_Attrition.groupby([
    "Education","Attrition"
])["MonthlyIncome"].mean()
Monthly_Income_By_Edu_and_Attrition


# # Assignment 3

# In[48]:


plt.figure(figsize=(10,7.5))
sb.barplot(x="DistanceFromHome", y="JobRole", hue="Attrition", data=IBM_Attrition)
plt.title("Distance From Home by Job Role and Attrition")
plt.xlabel("Distance From Home")
plt.ylabel("Job Role")


# In[49]:


plt.figure(figsize=(10,7.5))
sb.barplot(x="MonthlyIncome", y="JobRole", hue="Attrition", data=IBM_Attrition)
plt.title("Monthly Income by Job Role and Attrition")
plt.xlabel("Monthly Income")
plt.ylabel("Job Role")


# In[ ]:




