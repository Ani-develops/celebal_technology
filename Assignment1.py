#!/usr/bin/env python
# coding: utf-8

# In[1]:


def lower_triangle(n):

    for i in range(n+1):
        for j in range(i):
            print('*', end=' ')
        print()


n = 5
lower_triangle(n)


# In[2]:


def upper_triangle(n):

    for i in range(n):
        for j in range(n):
            if j >= i:
                print('*', end=' ')
            else:
                print(' ', end=' ')
        print()


n = 5
upper_triangle(n)


# In[3]:


def pyramid(n):
    count = 1

    for i in range(n):
        # Print leading spaces
        for j in range(n-i):
            print(' ', end='')

        # Print stars
        for k in range(count):
            print('*', end='')

        # for j in range(i):
        #     print(' ', end=' ')

        print()
        count += 2


n = 5
pyramid(n)


# In[ ]:




