#!/usr/bin/env python
# coding: utf-8

# In[25]:


import numpy as np
import random
import matplotlib.pyplot as plt

def ema(closed_prices, window):
    weights = np.exp(np.linspace(-1, 0, window))
    a = weights.sum()
    weights = weights/a
    em = np.convolve(closed_prices, weights)[:len(closed_prices)]
    em[:window] = em[window]
    x = list(range(1, len(closed_prices) + 1))
    plt.plot(x, em)

closed_prices = []
for i in range(200):
    closed_prices.append(random.uniform(40,50))    
#print(closed_prices)
ema(closed_prices, 10)

