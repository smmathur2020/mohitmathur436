#!/usr/bin/env python
# coding: utf-8

# In[1]:


a = "Hello"
print(type(a))
#basically 'type()' help in figuring out the type of variable used in the program 


# In[2]:


#list
l = [10,20,30,"hello"]
print(l)

#delete the list element
del l[0]
print("after deleting element",l)
print(type(l))


# In[6]:


#tuple
t=(20,"hello")
print(t)
print(type(t))


# In[5]:


#dictionary(dict)
d = {
    'course_name':'python',
    'duration': '2 Months'
}
print(d['duration'])
print(type(d))


# In[ ]:


#set
s = {10,20,30,10}
print(type(s))

