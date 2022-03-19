#!/usr/bin/env python
# coding: utf-8

# # library install

# In[1]:


pip install bs4


# In[2]:


pip install requests


# # importing libraries

# In[3]:


import requests


# In[4]:


from bs4 import BeautifulSoup


# # scraping website

# In[5]:


url="https://www.flipkart.com/search?q=apache%20180%20accesories&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off"


# # response

# In[6]:


response=requests.get(url)


# In[7]:


response


# # parsing

# In[8]:


soup=BeautifulSoup(response.text)


# In[9]:


soup


# In[10]:


access=soup.select(".s1Q9rs")


# In[11]:


access


# In[12]:


access_list=[]


# In[13]:


for item in access:
    access_list.append(item.text)
    access_list


# In[14]:


access_list


# In[15]:


prices=soup.select('._30jeq3')


# In[16]:


prices


# In[17]:


price_rating=[]


# In[18]:


for item in prices:
    price_rating.append(item.text)
    price_rating


# In[35]:


price_rating


# In[20]:


actual=soup.select('._3I9_wc')


# In[36]:


actual


# # data frame

# In[40]:


import pandas as pd


# In[43]:


Mytab=pd.DataFrame(access,columns=["access"])


# In[44]:


Mytab

