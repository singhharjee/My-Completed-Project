import re
import matplotlib.pyplot as plt
import numpy as np
import tweepy
from textblob import TextBlob  # text/tweet parse
from tweepy import OAuthHandler


api_key="Jm6WDXZuiwlwUnT9mFbPdSpcg"
api_secret_key="Wp4Gbf74R6MZWjXvj0ifKrCobwWbchhn53Mv8L7VMLbIUi6Wnd"

access_token ="919434545924935681-wFjVVTbs0pmyB2VwSoj4VwGb7tBYCyr"
access_token_secret="RaPfxU0rSMjkS3MSI9N0ztXu4I2iLMecXg79OerNHw4Ly"




auth = OAuthHandler(api_key, api_secret_key)
# set access token and secret
auth.set_access_token(access_token, access_token_secret)
# create tweepy API object to fetch tweets
api = tweepy.API(auth)




#get data from the user
topics=input('Enter topic on which you want to analyze the twitter data(eg. name of a leader,famous personality,etc): ')
print('Please wait while we are fetching the result.........')




#cleaning up the data which is not required
def clean_data(tweets):
    return ' '.join(re.sub(r"(@[A-Za-z0-9]+)|([^0-9A-Za-z \t]) |(\w+:\/\/\S+)", " ", tweets).split())  



try:
    tweets=api.search(q=topics,count=1000)
    #print(tweets)   

    polar=[]
    for t in tweets:
        text = clean_data(t.text)
        #print(text)
        analysis=TextBlob(text)
                
        if analysis.sentiment.polarity>0:
            polar.append('positive')
        elif analysis.sentiment.polarity<0:
            polar.append('negative')
        elif analysis.sentiment.polarity==0:
            polar.append('neutral')


    print('**************************************************************',topics,'************************************************************************')
    #print(polar)
    positive=[]
    negative=[]
    neutral=[]
    for i in polar:
        if i=='neutral':
            neutral.append(i)
        elif i=='positive':
            positive.append(i)
        else:
            negative.append(i)
        
    total=len(positive)+len(negative)+len(neutral)
    posperc=(len(positive)*100)/total
    negperc=(len(negative)*100)/total
    neuperc=(len(neutral)*100)/total

    print('no. of positive tweets= ',len(positive))
    print('no. of negative tweets= ',len(negative))
    print('no. of neutral tweets= ',len(neutral))
    print('% positive tweets= ',posperc)
    print('%negative tweets= ',negperc)
    print('%neutral tweets= ',neuperc)
    print('*********************************************************************************************************************************************')
    #print(polar)


    ###############################################################################
    #plotting Graph

    #fig, ax = plt.subplots()
    index = np.arange(1)
    bar_width = 0.1
    opacity = 1

    plt.bar(index, len(positive), bar_width, alpha=opacity, color='g', edgecolor='w', label='positive')


    plt.bar(index + bar_width, len(negative), bar_width, alpha=opacity, color='r', edgecolor='w', label='negative')


    plt.bar(index + bar_width+ bar_width, len(neutral), bar_width, alpha=opacity, color='b', edgecolor='w', label='neutral')


    plt.xticks(index+bar_width, [topics],family='fantasy')
    plt.xlabel('Topics',fontweight='bold',fontsize='10')
    plt.ylabel('Sentiments',fontweight='bold',fontsize='10')
    plt.title('Twitter Sentiment Analysis',fontweight='bold', color = 'white', fontsize='17', horizontalalignment='center',backgroundcolor='black')

    plt.legend()
    
    plt.tight_layout()
    plt.show()
except ZeroDivisionError:
    print("Twitter doesn't have any tweets regarding the entered topic" )
except tweepy.error.TweepError:
    print("NO INTERNET!!! Check your internet connection")


