#!/usr/bin/env python
# coding: utf-8

# **OBJECTIVE**
# * Improve customer experience by analysing sales data
# * Increase revenue

# In[2]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()
from matplotlib.ticker import PercentFormatter


# In[4]:


df = pd.read_csv("Diwali Sales Data.csv", encoding = 'unicode_escape')
df.head(10)


# In[5]:


df.shape


# In[6]:


df.info()


# In[7]:


df_sales_data = df.copy()
df_sales_data


# In[8]:


df_sales_data.drop(["Status","unnamed1"], axis = 1, inplace = True)
# inplace is used to save the data what we are doing without assiginig it 


# In[9]:


df_sales_data.head()


# In[10]:


# check whether we have null values or not
pd.isnull(df_sales_data).sum()


# In[11]:


df_sales_data.shape


# In[12]:


df_sales_data.dropna(inplace = True)


# In[13]:


df_sales_data.shape


# In[14]:


# changing our dtype of amount col into int
df_sales_data['Amount'] = df_sales_data['Amount'].astype('int')


# In[15]:


df_sales_data['Amount'].dtype


# In[16]:


df_sales_data.columns


# In[17]:


df_sales_data.describe()
# it returns description of the data 


# In[18]:


df_sales_data[['Age','Orders','Amount']].describe()


# # Exploratory Data Analysis

# **GENDER**

# In[19]:


sns.set_palette('colorblind')


# In[28]:


ax = sns.countplot(x = 'Gender', data = df_sales_data, palette = ['midnightblue','orange'] )
sns.set(rc = {'figure.figsize': (8,5)})
sns.set_style('white')
for bars in ax.containers:
    ax.bar_label(bars)


# In[21]:


df_sales_data.groupby(['Gender'], as_index = False)['Amount'].sum().sort_values(by = 'Amount', ascending = False)


# In[22]:


sales_gen = df_sales_data.groupby(['Gender'], as_index = False)['Amount'].sum().sort_values(by = 'Amount', ascending = False)

sns.barplot(x = 'Gender', y = 'Amount', data = sales_gen)


# ***from the above graph most of the buyers are females and the purchasing power of female is greater than men***

# **AGE**

# In[29]:


ax = sns.countplot(x = 'Age Group', hue = 'Gender', data = df_sales_data, palette = ['teal','#EF476F'])

sns.set(rc = {'figure.figsize': (7,5)})
sns.set_style('white')
plt.xlabel("Age group", weight = 'bold')
plt.ylabel("Count", weight = 'bold')

for bars in ax.containers:
    ax.bar_label(bars)
    
    


# In[30]:


sales_age = df_sales_data.groupby(['Age Group'], as_index = False)['Amount'].sum().sort_values(by = 'Amount', ascending = False)

sns.set(rc = {'figure.figsize': (7,5)})
sns.set_style('white')
plt.xlabel("Age group", weight = 'bold')
plt.ylabel("Amount", weight = 'bold')


sns.barplot(x = 'Age Group', y = 'Amount', data = sales_age, palette = ['#255F85','#E4572E','#9BC53D','#750D37','#5B2A86','#254441','#F2FF49'])


# ***from the above graph we can see that most of the buyers are of 26-35 Age Group of females***

# **STATE**

# In[31]:


# total number of orders from top 10 states
sales_state = df_sales_data.groupby(['State'], as_index = False)['Orders'].sum().sort_values(by = 'Orders', ascending = False).head(10)


sns.set(rc = {'figure.figsize': (9,7)})
sns.set_style('white')
plt.xlabel("State", weight = 'bold', fontsize = 14)
plt.ylabel("Orders", weight = 'bold', fontsize = 14)
plt.xticks(rotation = 45, fontsize = 14)


sns.barplot(x = 'State', y = 'Orders', data = sales_state,
           palette = ['#0E131F','#15616D','#78290F','#35CE8D','#FF4365','#F26430','#6761A8','#9B8816','#CE6C47','#FFD046'])


# In[37]:


# total of amount from top 10 states
sales_state = df_sales_data.groupby(['State'], as_index = False)['Amount'].sum().sort_values(by = 'Amount', ascending = False).head(10)

sns.set(rc = {'figure.figsize': (16,7)})
sns.set_style('white')
plt.xlabel("State", weight = 'bold', fontsize = 14)
plt.ylabel("Amount", weight = 'bold', fontsize = 14)
plt.xticks(fontsize = 14, rotation = 15)

sns.barplot(x = 'State', y = 'Amount', data = sales_state,
           palette = ['#0E131F','#15616D','#78290F','#35CE8D','#FF4365','#F26430','#6761A8','#9B8816','#CE6C47','#FFD046'])


# ***from the above graphs we can see that most of the orders are from UP, maharastra and karnataka and total amount also highest from UP, maharastra and karnataka***

# **MARITAL STATUS**

# In[53]:


ax = sns.countplot(x = 'Marital_Status', data = df_sales_data, palette = ['#C33149','#E2C044'])

sns.set(rc = {'figure.figsize': (7,4)})
sns.set_style('white')
plt.xlabel("Marital_Status", weight = 'bold', fontsize = 14)
plt.ylabel("Count", weight = 'bold', fontsize = 14)

for bars in ax.containers:
    ax.bar_label(bars)


# In[54]:


sales_state = df_sales_data.groupby(['Marital_Status', 'Gender'], as_index = False)['Amount'].sum().sort_values(by = 'Amount', ascending = False).head(10)

sns.set(rc = {'figure.figsize': (8,6)})
sns.set_style('white')
plt.xlabel("Marital_Status", weight = 'bold', fontsize = 14)
plt.ylabel("Amount", weight = 'bold', fontsize = 14)

sns.barplot(x = 'Marital_Status', y = 'Amount', data = sales_state, hue = 'Gender',
           palette = ['#4B2840','#87C38F'])


# ***from the above graphs we can see that most of the buyers are married(women) and they have more purchasing power***

# **OCCUPATION**

# In[79]:


sns.set(rc = {'figure.figsize': (20,7)})

ax = sns.countplot(x = 'Occupation', data = df_sales_data,
                  palette = ['#022B3A','#46351D','#7D4F50','#037971','#FE621D',
                            '#EEB902','#A61C3C','#3E5C76','#545E56','#843B62',
                            '#F49D6E','#F487B6','#F58F29','#49393B','#8BBF9F'])
sns.axes_style('white', {'axes.grid': False})
ax.grid(False)

plt.xlabel("Occupation", weight = 'bold', fontsize = 16)
plt.ylabel("count", weight = 'bold', fontsize = 16)
plt.xticks(rotation = 45, fontsize = 14)


for bars in ax.containers:
    ax.bar_label(bars)


# In[81]:


sales_occupation = df_sales_data.groupby(['Occupation'], as_index = False)['Amount'].sum().sort_values(by = 'Amount', ascending = False)

sns.set(rc = {'figure.figsize': (20,7)})
sns.barplot(x = 'Occupation', y = 'Amount', data = sales_occupation,
            palette = ['#022B3A','#46351D','#7D4F50','#037971','#FE621D',
                            '#EEB902','#A61C3C','#3E5C76','#545E56','#843B62',
                            '#F49D6E','#F487B6','#F58F29','#49393B','#8BBF9F'])
sns.set_style('white')

ax.grid(False)

plt.xlabel("Occupation", weight = 'bold', fontsize = 16)
plt.ylabel("Amount", weight = 'bold', fontsize = 16)
plt.xticks(rotation = 45, fontsize = 14)


# ***from above graph we can see that most of the buyers are from IT sector, Aviation and Healthcare***

# In[73]:


sns.set(rc = {'figure.figsize': (15,7)})

ax = sns.countplot(x = 'Product_Category', data = df_sales_data,
                  palette = ['#022B3A','#6D435A','#7D4F50','#037971','#FE621D',
                            '#EEB902','#92DCE5','#3E5C76','#545E56','#843B62',
                            '#806D40','#00BD9D','#EC9A29','#49393B','#CC2936','#1F7A8C','#EE6C4D','#CE5374'])
sns.set_style('white')
plt.xlabel("Product_Category", weight = 'bold', fontsize = 16)
plt.ylabel("count", weight = 'bold', fontsize = 16)
plt.xticks(rotation = 45)

for bars in ax.containers:
    ax.bar_label(bars)


# In[63]:


sales_occupation = df_sales_data.groupby(['Product_Category'], as_index = False)['Amount'].sum().sort_values(by = 'Amount', ascending = False)

sns.set(rc = {'figure.figsize': (15,7)})
sns.barplot(x = 'Product_Category', y = 'Amount', data = sales_occupation,
            palette = ['#022B3A','#6D435A','#7D4F50','#037971','#FE621D',
                            '#EEB902','#92DCE5','#3E5C76','#545E56','#843B62',
                            '#806D40','#00BD9D','#EC9A29','#49393B','#CC2936','#1F7A8C','#EE6C4D','#CE5374'])
sns.set_style('white')
plt.xlabel("Product_Category", weight = 'bold', fontsize = 16)
plt.ylabel("Amount", weight = 'bold', fontsize = 16)
plt.xticks(rotation = 45)


# ***from above graphs we can see that most of the sold products are from Food, clothing and electronic gadgets category***

# In[71]:


# top 10 most sold products
sales_productID = df_sales_data.groupby(['Product_ID'], as_index = False)['Orders'].sum().sort_values(by = 'Orders', ascending = False).head(10)

sns.set(rc = {'figure.figsize': (20,7)})
sns.barplot(x = 'Product_ID', y = 'Orders', data = sales_productID,
           palette = ['#143642','#F56416','#679436','#D90368','#540D6E','#553A41','#E9806E','#CAA8F5','#E6C229','#06D6A0'])

sns.set_style('white')
plt.xlabel("Product_ID", weight = 'bold', fontsize = 16)
plt.ylabel("Orders", weight = 'bold', fontsize = 16)
plt.xticks(rotation = 45)


# # **CONCLUSION**
# **Married women of age group 26-35 from UP, Maharastra and Karnataka working in IT, Aviation and Healthcare are most likely to buy products in Food, Clothing and Electronics categories**
# 
# 

# In[ ]:




