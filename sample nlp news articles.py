#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().system('pip install textblob==0.9.0')
get_ipython().system('pip install newspaper3K')


# In[2]:


import tkinter as tk
import nltk 
from textblob import TextBlob
from newspaper import Article


# In[3]:


nltk.download('punkt') # model that we can use for NLP


# In[4]:


#url="https://www.hindustantimes.com/world-news/khalistani-terror-cells-thrive-in-canada-indian-intel-shows-alarming-connections-101695604123751.html"


# In[5]:


url="https://timesofindia.indiatimes.com/city/amaravati"


# In[6]:


url


# In[7]:


article=Article(url)
article


# In[8]:


article.download()#download the url Data


# In[9]:


article.parse() #parse the data the parse dissect the article that it need # extract the appropriate data from the article ..


# In[10]:


article.nlp() # using nlp it does everything for you 


# In[11]:


print('Title:',article.title)
print("Auther:",article.authors)
print('Publication Date: ',article.publish_date)
print("Summary:",article.summary)


# In[12]:


# using sentiment analysis we can analyse the whole text
analysis = TextBlob(article.text)
if analysis.polarity > 0:
    print("Positive")
elif analysis.polarity < 0:
    print("Negative")
else:
    print("Neutral")


# In[13]:


# Summarize
def summarize():
    url = utext.get('1.0',"end").strip() #1.0 from start to end url reading 
    article = Article(url)
    article.download()
    article.parse()
    article.nlp()
    
    title.config(state='normal')
    author.config(state='normal')
    publication.config(state="normal")
    summary.config(state='normal')
    sentiment.config(state="normal")
    
    title.delete('1.0', 'end')
    title.insert('1.0',article.title)
    
    author.delete('1.0' ,'end')
    author.insert('1.0',article.authors)
    
    publication.delete('1.0', 'end')
    publication.insert('1.0',article.publish_date)
    
    summary.delete('1.0', 'end')
    summary.insert('1.0', article.summary)
    
    
    analysis = TextBlob(article.text)
    sentiment.delete('1.0', 'end')
    sentiment.insert('1.0',f'Polarity:{analysis.polarity}, Sentiment:{"Positive"if analysis.polarity > 0 else "Negative" if analysis.polarity < 0 else "Neutral"}')
            

    title.config(state = 'disabled')
    author.config(state = 'disabled')
    publication.config(state = 'diabled')
    summary.config(state = 'disabled')
    sentiment.config(state  = 'disabled')
    


# In[14]:


root = tk.Tk()
root.title("Article Summarizer")
root.geometry('1200x600')


# In[15]:


tlabel = tk.Label(root, text='Title')
tlabel.pack()


# In[16]:


title = tk.Text(root, height=1, width=140)
title.config(state='disabled', bg="#dddddd")
title.pack()


# In[17]:


alabel = tk.Label(root, text ='Author')
alabel.pack()
author = tk.Text(root, height=1, width=140)
author.config(state='disabled', bg="#dddddd")
author.pack()


# In[18]:


plabel = tk.Label(root, text ="Publishing Date")
plabel.pack()
publication = tk.Text(root, height=1, width=140)
publication.config(state='disabled', bg="#dddddd")
publication.pack()


# In[19]:


slabel = tk.Label(root, text ="Summary")
slabel.pack()
summary = tk.Text(root, height=20, width=140)
summary.config(state='disabled', bg="#dddddd")
summary.pack()


# In[20]:


selabel = tk.Label(root, text ="Sentiment Analysis")
selabel.pack()
sentiment = tk.Text(root, height=1, width=140)
sentiment.config(state='disabled', bg="#dddddd")
sentiment.pack()


# In[ ]:





# In[21]:


ulabel = tk.Label(root, text ="URL")
ulabel.pack()
utext = tk.Text(root, height=1, width=140)
utext.pack()


# In[22]:


btn = tk.Button(root,text="Summarize", command = summarize)
btn.pack()


# In[ ]:


root.mainloop() 


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




