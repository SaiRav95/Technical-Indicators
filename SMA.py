#!/usr/bin/env python
# coding: utf-8

# In[85]:


import numpy as np
import random
import matplotlib.pyplot as plt 
def sma(closed_prices, Window):
    weights = np.repeat(1, Window)/Window
    simple = np.convolve(closed_prices, weights, 'valid')
    x = list(range(1, len(closed_prices) + 1 - Window + 1))
    plt.plot(x, simple)

closed_prices = []
for i in range(200):
    closed_prices.append(random.uniform(40,50))    
#print(closed_prices)
sma(closed_prices, 10)


# In[ ]:




