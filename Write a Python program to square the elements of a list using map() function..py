#!/usr/bin/env python
# coding: utf-8

# In[1]:


def func(n):
    return n**2


# In[2]:


n = [4,5,2,9]
print('Sample List: ',n)
result = map(func,n)
print('\nSquare the elements in list: ')
print(list(result))


# In[ ]:




