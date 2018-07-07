'''
import all the necessary libraray
'''
import tweepy
import matplotlib.pyplot as plt


#import textblob which is build on top of nltk(natural language processing toolkit)
from textblob import TextBlob


'''
ENTER ALL THE NECESSARY KEYS AND KEYSECRET for connectivity
'''
c_key='dIfv0VWYf91yaKNjTLPr472eu'
c_secret='2kAGGahFO8cGnTKLlkjbbaAwhhhqmaaFq9WXONE7mBbyNDKitM'
a_key='1014829542622388224-2QWAliJQkJ79x32JXMT3rRS1Ddqq0K'
a_secret='Vqt5UR8hwYvCTmdd1fdj0QRAndGwY2eYJMWbbz6qRh5hD'


#for calculating percentage
def percentage_count(sentiments,number):
    return 100*float(sentiments)/float(number)



#creating object of OAuthHandler class and passing consumers key and secret
#and also setting the sccess token by the method set_access_token
auth=tweepy.OAuthHandler(c_key,c_secret)
auth.set_access_token(a_key,a_secret)

find=input('Enter the hashtag/keyword')
count=input('Enter how many tweet u want to analyse')


#calling tweepy API and passing auth
api=tweepy.API(auth)
public_tweet=api.search(q=find,count=count)



negative=0
positive=0
neutral=0


for tweet in public_tweet:
    analysis=TextBlob(tweet.text)
    if(analysis.sentiment.polarity==0):
        neutral+=1
    elif(analysis.sentiment.polarity>0.00):
        positive+=1
    elif(analysis.sentiment.polarity<0.00):
        negative+=1


positive=percentage_count(positive,count)
negative=percentage_count(negative,count)
neutral=percentage_count(neutral,count)

positive=format(positive,'.2f')
negative=format(negative,'.2f')
neutral=format(neutral,'.2f')


contender=[positive,negative,neutral]


plt.pie(contender,startangle=180,labels=['positive','negative','neutral'])
plt.legend([positive,negative,neutral])
plt.show()
