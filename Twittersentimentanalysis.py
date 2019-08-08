import re
import matplotlib.pyplot as plt
import numpy as np
import tweepy
from textblob import TextBlob  # text/tweet parse
from tweepy import OAuthHandler




#cleaning up the data which is not required
def clean_data(tweets):
    return ' '.join(re.sub(r"(@[A-Za-z0-9]+)|([^0-9A-Za-z \t]) |(\w+:\/\/\S+)", " ", tweets).split())  




def graph(positive,negative,neutral,topics):
    #plotting Graph

    #fig, ax = plt.subplots()
    index = np.arange(1)
    bar_width = 0.1
    opacity = 1

    plt.bar(index, positive, bar_width, alpha=opacity, color='g', edgecolor='w', label='positive')


    plt.bar(index + bar_width, negative, bar_width, alpha=opacity, color='r', edgecolor='w', label='negative')


    plt.bar(index + bar_width+ bar_width, neutral, bar_width, alpha=opacity, color='b', edgecolor='w', label='neutral')


    plt.xticks(index+bar_width, [topics],family='fantasy')
    plt.xlabel('Topics',fontweight='bold',fontsize='10')
    plt.ylabel('Sentiments',fontweight='bold',fontsize='10')
    plt.title('Twitter Sentiment Analysis',fontweight='bold', color = 'white', fontsize='17', horizontalalignment='center',backgroundcolor='black')

    plt.legend()
    
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":

    api_key="eKfzeYoZWFUQ7g4ogx6KeZqRs"
    api_secret_key="suBMejO4npo3V5DjEGe3CiO3hYByPY37h4YVm7YqxqGpIMbOXn"
    
    access_token ="1140296275755036672-zOAtEJ4uUD3jU7Xw0Lhugi8smm656m"
    access_token_secret="xhRYHDe9JjaJO9X2el2PW2caBX9SL1YisciOdvkZNplJY"
    
    
    
    
    auth = OAuthHandler(api_key, api_secret_key)
    # set access token and secret
    auth.set_access_token(access_token, access_token_secret)
    # create tweepy API object to fetch tweets
    api = tweepy.API(auth)
    
    
    
    
    #get data from the user
    topics=input('Enter topic on which you want to analyze the twitter data(eg. name of a leader,famous personality,etc): ')
    print('Please wait while we are fetching the result.........')
    try:
        tweets=api.search(q=topics,count=1000)
        #print(tweets)   
        positive=0
        negative=0
        neutral=0
        for t in tweets:
            text = clean_data(t.text)
            #print(text)
            analysis=TextBlob(text)
                    
            if analysis.sentiment.polarity>0:
                positive+=1
            elif analysis.sentiment.polarity<0:
                negative+=1
            elif analysis.sentiment.polarity==0:
                neutral+=1
    
    
        print('**************************************************************',topics,'************************************************************************')
    
        total=positive+negative+neutral
        posperc=(positive*100)/total
        negperc=(negative*100)/total
        neuperc=(neutral*100)/total
    
        print('no. of positive tweets= ',positive)
        print('no. of negative tweets= ',negative)
        print('no. of neutral tweets= ',neutral)
        print('% positive tweets= ',posperc)
        print('%negative tweets= ',negperc)
        print('%neutral tweets= ',neuperc)
        print('*********************************************************************************************************************************************')
        #print(polar)
        graph(positive,negative,neutral,topics)
    except ZeroDivisionError:
        print("Twitter doesn't have any tweets regarding the entered topic" )
    except tweepy.error.TweepError:
        print("NO INTERNET!!! Check your internet connection")

