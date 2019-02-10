
# coding: utf-8

# In[1]:


import nltk
from konlpy.corpus import kolaw
from konlpy.tag import *
import pandas as pd
import platform
from collections import Counter
from matplotlib import font_manager, rc
from konlpy.tag import Twitter; t = Twitter()
import numpy as np


# In[2]:


dfa = pd.read_csv("../petition_data_all.csv")


# In[3]:


df1 = dfa[dfa["count"]>=100]


# In[4]:


df1


# In[5]:


ko_con_text = list(df1["title"])
ko_con_text = ' '.join(ko_con_text)
print(len(ko_con_text))


# In[ ]:


tokens_ko = t.nouns(ko_con_text)
print("Fsd")

# In[ ]:


tokens_ko


# In[ ]:


nlist = list(df1["num"])
nlist


# In[ ]:


tokens_ko = list(set(tokens_ko))
tokens_ko


# In[ ]:


all_set = tokens_ko
len(all_set)


# In[ ]:


df_name = list(df1["title"])


# In[ ]:


conut_lists = []
for i in range(len(df_name)):
    conut_list = []
    for one_set in all_set:
        conut_list.append(df_name[i].count(one_set))
    conut_lists.append(conut_list)


# In[ ]:


len(all_set), len(set(all_set)), len(conut_lists[0])


# In[ ]:


lists = [{'key_word' : "key_word", str(i): 0} 
         for i in nlist]
test = pd.DataFrame(lists)

for i in range(len(list(df1["num"]))):
    test = test.drop(i,0)
    
test


# In[ ]:


for i in range(len(all_set)):
    tlist = []
    for j in range(len(conut_lists)):
        tlist.append(conut_lists[j][i])
    tlist.append(all_set[i])
    test.loc[i] = tlist
    
test


# In[ ]:


nlist.append("key_word")


# In[ ]:


nlist[3257]


# In[ ]:


len(nlist)


# In[ ]:


test.columns = nlist
test


# In[ ]:


test.to_csv("up100_t.csv",index=False)

