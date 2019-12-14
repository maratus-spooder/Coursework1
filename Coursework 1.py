#!/usr/bin/env python
# coding: utf-8

# ### Question 1
# a) Read the file “Length-cells.csv” (it contains two datasets: length of normal cells and that of cancer cells)

# In[1]:


import csv
csvfile = open('Length-cells.csv', 'r') 
mycsv = csv.reader(csvfile)
next(mycsv)
x1=[]
y1=[]
for row in mycsv:
    x1.append(float(row[0]))
    y1.append(float(row[1]))


# In[2]:


import array as ar
x=ar.array("f",x1)
y=ar.array("f",y1)


# In[3]:


print(x)


# In[4]:


print(y)


# In[5]:


import matplotlib.pyplot as plt


# In[6]:


plt.hist(x, len(x), alpha = 0.5, label='normal cells')
plt.hist(y, len(y), alpha = 0.5, label='cancer cells')
plt.legend(loc='upper right')
plt.show()


# ### Question 2
# - Generate 100 random real numbers in the range [1, 200]
# - Round off the generated numbers to 2 digits and print out the full list
# - Generate an array of 50 random integers numbers in the range [1, 100]
# - Generate an array of 50 random real numbers in the range [0, 1]
# - Plot the arrays of random real and integer numbers as histograms (provide a
# legend)
# - Sort the dataset of random real numbers in ascending order
# - Sort the dataset of random integer numbers in descending order
# - Swap the first and last numbers in the sorted dataset of random real
# numbers. Print out the result

# In[16]:


import random

my100numbers = []

for i in range(0,100):
    x = random.uniform(1, 200)
    x2=float("{0:.2f}".format(x))
    my100numbers.append(x2)
    

print(my100numbers)


# In[17]:


my50numbers = []

for i in range(0,50):
    x = random.randrange(1, 100)
    my50numbers.append(x)
x=ar.array("i",my50numbers)


# In[18]:


my50realnumbers = []

for i in range(0,50):
    x = random.uniform(0, 1)
    my50realnumbers.append(x)
x=ar.array("f",my50realnumbers)


# In[19]:


import numpy as np

my50realnumbers=np.array(my50realnumbers)
my50numbers=np.array(my50numbers)


# In[11]:


plt.hist(my50numbers, len(my50numbers), alpha = 0.5, label='Integers')
plt.hist(my50realnumbers*100, len(my50realnumbers), alpha = 0.5, label='Real Numbers*100')
plt.legend(loc='upper right')
plt.show()


# In[12]:


my50realnumbers = np.sort(my50realnumbers)
my50numbers = np.sort(my50numbers)
my50numbers = my50numbers[::-1]


# In[13]:


temp = my50realnumbers[0]
my50realnumbers[0] = my50realnumbers[len(my50realnumbers)-1]
my50realnumbers[len(my50realnumbers)-1] = temp


# In[14]:


print (my50realnumbers)


# In[ ]:




