
# coding: utf-8

# In[35]:


'''
import all the necessary libraray
'''
import tweepy
import matplotlib.pyplot as plt



# In[86]:


#import textblob which is build on top of nltk(natural language processing toolkit)
from textblob import TextBlob


# In[87]:


'''
ENTER ALL THE NECESSARY KEYS AND KEYSECRET for connectivity
'''
c_key='dIfv0VWYf91yaKNjTLPr472eu'
c_secret='2kAGGahFO8cGnTKLlkjbbaAwhhhqmaaFq9WXONE7mBbyNDKitM'
a_key='1014829542622388224-2QWAliJQkJ79x32JXMT3rRS1Ddqq0K'
a_secret='Vqt5UR8hwYvCTmdd1fdj0QRAndGwY2eYJMWbbz6qRh5hD'


# In[88]:


#for calculating percentage
def percentage_count(sentiments,number):
    return 100*float(sentiments)/float(number)


# In[89]:


#creating object of OAuthHandler class and passing consumers key and secret
#and also setting the sccess token by the method set_access_token
auth=tweepy.OAuthHandler(c_key,c_secret)
auth.set_access_token(a_key,a_secret)


# In[91]:


find=input('Enter the hashtag/keyword')
count=input('Enter how many tweet u want to analyse')


# In[ ]:


#calling tweepy API and passing auth
api=tweepy.API(auth)
public_tweet=api.search(q=find,count=count)


# In[101]:


negative=0
positive=0
neutral=0


# In[102]:


for tweet in public_tweet:
    analysis=TextBlob(tweet.text)
    if(analysis.sentiment.polarity==0):
        neutral+=1
    elif(analysis.sentiment.polarity>0.00):
        positive+=1
    elif(analysis.sentiment.polarity<0.00):
        negative+=1


# In[103]:


positive=percentage_count(positive,count)
negative=percentage_count(negative,count)
neutral=percentage_count(neutral,count)

positive=format(positive,'.2f')
negative=format(negative,'.2f')
neutral=format(neutral,'.2f')


# In[105]:





# In[106]:


contender=[positive,negative,neutral]


# In[107]:


plt.pie(contender,startangle=180,labels=['positive','negative','neutral'])
plt.legend([positive,negative,neutral])
plt.show()
