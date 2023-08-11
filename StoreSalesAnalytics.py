#!/usr/bin/env python
# coding: utf-8

# In[2]:


# let's import the packages we will use in this project


import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# In[3]:


#Reading the data(CSV file)

df=pd.read_csv('I:\Python_Diwali_Sales_Analysis-main\Diwali Sales Data.csv',encoding='unicode_escape')


# In[4]:


df.shape


# In[4]:


df.head()


# In[ ]:


df.info


# In[5]:


#check for null values

pd.isnull(df).sum()


# In[6]:


#drop unrelated/blank columns

df.drop(['Status', 'unnamed1'], axis=1, inplace=True)


# In[7]:


# drop null values

df.dropna(inplace=True)


# In[8]:


pd.isnull(df).sum()


# In[9]:


# change data type

df['Amount'] = df['Amount'].astype('int64')


# In[10]:


df['Amount'].dtypes


# In[29]:


df.columns


# In[12]:


#rename column

df.rename(columns= {'Marital_Status':'Shaadi'})


# In[13]:


df.describe()


# In[14]:


df[['Age','Orders','Amount']].describe()


# # Exploratory Data Analysis
# ## Gender
# 
# 
# 

# In[15]:


# plotting a bar chart for Gender and it's count

ax = sns.countplot(x = 'Gender',data = df)

for bars in ax.containers:ax.bar_label(bars)


# In[1]:


# plotting a bar chart for gender vs total amount

sales_gen = df.groupby(['Gender'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False)

sns.barplot(x = 'Gender',y= 'Amount' ,data = sales_gen)

for bars in ax.containers:ax.bar_label(bars)


# From above graphs we can see that most of the buyers are females and even the purchasing power of females are greater than men

# ## Age

# In[17]:


#Age

ax=sns.countplot(x='Age Group', data=df, hue='Gender')

for bars in ax.containers:ax.bar_label(bars)


# In[18]:


# Total Amount vs Age Group

sales_age = df.groupby(['Age Group'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False)

sns.barplot(x='Age Group', y='Amount',data=sales_age)


# From above graphs we can see that most of the buyers are of age group between 26-35 yrs female 

# ## State

# In[19]:


# total number of orders from top 10 states

sales_state = df.groupby(['State'], as_index=False)['Orders'].sum().sort_values(by='Orders', ascending=False).head(10)

sns.set(rc={'figure.figsize':(17,5)})

sns.barplot(x='State', y='Orders', data=sales_state)


# In[20]:


# total amount/sales from top 10 states

sales_state = df.groupby(['State'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False).head(10)

sns.set(rc={'figure.figsize':(17,5)})

sns.barplot(x='State', y='Amount', data=sales_state)


# From above graphs we can see that most of the orders & total sales/amount are from Uttar Pradesh, Maharashtra and Karnataka respectively

# ## Marital Status

# In[21]:


#Marital Status
#01

ax=sns.countplot(x='Marital_Status',data=df)

sns.set(rc={'figure.figsize':(10,5)})

for bars in ax.containers:ax.bar_label(bars)


# In[22]:


# Marital Status vs Gender
sales_state = df.groupby(['Marital_Status', 'Gender'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False)

sns.set(rc={'figure.figsize':(6,5)})

sns.barplot(data = sales_state, x = 'Marital_Status',y= 'Amount', hue='Gender')


# From above graphs we can see that most of the buyers are married (women) and they have high purchasing power

# ## Occupation

# In[30]:


#On the basis of Occupation

ax=sns.countplot(x='Occupation',data=df)

for bars in ax.containers:ax.bar_label(bars)


# In[24]:


# total amount spend by people with different occupation

sales_state = df.groupby(['Occupation'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False)

sns.set(rc={'figure.figsize':(20,5)})

sns.barplot(data = sales_state, x = 'Occupation',y= 'Amount')


# From above graphs we can see that most of the buyers are working in IT, Healthcare and Aviation sector

# ## Product Category

# In[25]:


#Product Category

sns.set(rc={'figure.figsize':(28,5)})

ax = sns.countplot(data = df, x = 'Product_Category')

for bars in ax.containers:
    ax.bar_label(bars)


# In[26]:


# Amount vs Product Category

sales_state = df.groupby(['Product_Category'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False).head(10)

sns.set(rc={'figure.figsize':(20,5)})

sns.barplot(data = sales_state, x = 'Product_Category',y= 'Amount')


# In[27]:


# Amount vs Product ID

sales_state = df.groupby(['Product_ID'], as_index=False)['Orders'].sum().sort_values(by='Orders', ascending=False).head(10)

sns.set(rc={'figure.figsize':(20,5)})

sns.barplot(data = sales_state, x = 'Product_ID',y= 'Orders')


# ## Conclusion

# Married women age group 26-35 yrs from UP, Maharastra and Karnataka working in IT, Healthcare and Aviation are more likely to buy products from Food, Clothing and Electronics category

# In[ ]:




