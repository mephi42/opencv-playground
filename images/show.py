
# coding: utf-8

# In[1]:

import cv2


# In[2]:

import matplotlib.pyplot as plt


# In[3]:

im = cv2.imread('/var/lib/images/4.2.04.tiff')


# In[4]:

plt.imshow(cv2.cvtColor(im, cv2.COLOR_BGR2RGB))


# In[ ]:



