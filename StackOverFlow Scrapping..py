#!/usr/bin/env python
# coding: utf-8

# In[1]:


import requests
from bs4 import BeautifulSoup


# In[4]:


url="https://stackoverflow.com/questions/415511/how-do-i-get-the-current-time-in-python"
data=requests.get(url)
soup = BeautifulSoup(data.content, 'html.parser')


# In[8]:


# print(soup.text)
question=soup.find('a',class_="question-hyperlink")
print('Question:',question.text)
answer=soup.find_all('div',class_="answercell post-layout--right")
count=1
for ans in answer:
    print(count,"____________________________________")
    oneans=ans.find('div',class_="s-prose js-post-body").text.strip()
    print(oneans)
    count+=1


# In[ ]:




