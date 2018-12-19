
# coding: utf-8

# In[1]:

get_ipython().magic('ls')


# In[2]:

with open('paragraph_1.txt') as f:
    data = f.read()


# In[3]:

data


# In[5]:

sent = data.split(".")


# In[7]:

len(sent) # 6 sentences right?


# In[10]:

# letters per word and words per sent

words = []

for s in sent:
    sent_words = s.split()
    for word in sent_words:
        words.append(word)


# In[14]:

import numpy as np

np.mean([len(x) for x in words])


# In[19]:

[len(x.split()) for x in sent if len(x) > 0] # len of sentences 


# In[28]:

sum([ len(x) for x in words] ) / len(words)


# In[30]:

get_ipython().magic('pinfo2 np.mean')


# In[25]:

len([1,2,3])


# In[ ]:




# In[ ]:



