#!/usr/bin/env python
# coding: utf-8

# # Importing essential libraries

# In[1]:


import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import folium
import seaborn as sns


# # Making a userdefined dataset

# In[2]:


dict1 = {
'Name': ['Ritik', 'Swastik', 'Manushri', 'Mumma', 'Papa'],
'Marks': [100, 90, 98, 95, 96],
'City': ['London', 'California', 'Paris', 'Athens', 'Moscow']    
}


# # Passing the dataset to a pandas dataframe and reseting index

# In[3]:


df = pd.DataFrame(dict1)
df.reset_index(drop=True, inplace=True)


# In[4]:


df


# # Creating a simple Bar Chart using plotly

# In[5]:


df.plot(kind='bar')

plt.ylabel("Score")
plt.xlabel("Serial number")


# # Creating a simple piechart

# In[6]:


df['Marks'].plot(kind='pie')

plt.show()


# # Creating a line diagram

# In[7]:


df.plot()
plt.ylabel("Score")
plt.xlabel("Serial number")


# # imported a Tokyo Olympics 2021 dataset from a CSV file to pandas

# In[8]:


df_tokyo = pd.read_csv('Tokyo 2021 dataset.csv')


# In[9]:


df_tokyo


# # Extracting top5 rows

# In[10]:


df_tokyo.head(5)


# # Extracted top 5 rows for further analysis

# In[17]:


final=df_tokyo.head(5)


# In[18]:


final


# # Created a pie chart

# In[19]:


final['Rank'].plot(kind='pie')
plt.show()


# # Created a line diagram

# In[33]:


final.plot(x = 'NOCCode', y = 'Gold Medal', kind='line')

plt.show()


# # Strip plot comparing Rank of the top 5 countries 

# In[22]:


sns.stripplot(x="Rank", y="Team/NOC", data=final)


# # Count plot

# In[28]:


sns.countplot(x="NOCCode", data = final, palette = "Greens_d")


# # A scatter plot onto a FacetGrid

# In[31]:


sns.lmplot(x="Rank by Total", y="Gold Medal", hue="Total", data=final)


# # Regression plot

# In[37]:


sns.regplot(x="Rank by Total", y="Total", data=final)

