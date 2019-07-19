import re
import matplotlib.pyplot as plt
import numpy as np
import tweepy
from textblob import TextBlob  # text/tweet parse
from tweepy import OAuthHandler
from tkinter import Tk,Label,Entry,Button,BOTTOM,Text,PhotoImage,Frame,END

root = Tk()
root.title("Sentiment Analysis") 
root.geometry('1000x800')

# taking image from the directory and storing the source in a variable
icon =PhotoImage(file = r"E:\oauth_application.png")
icon1=PhotoImage(file=r"E:\IMG_20190719_201952.png")
# displaying the picture using a 'Label' by passing the 'picture' variriable to 'image' parameter
background =Label(root, image = icon)
background.pack()
background1=Label(root,image=icon1)
background1.pack(side="bottom")




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

label1 = Label(root, text="Search")
E1 = Entry(root, bd =5)

def entry():
    return E1.get()


#cleaning up the data which is not required
def clean_data(tweets):
    return ' '.join(re.sub(r"(@[A-Za-z0-9]+)|([^0-9A-Za-z \t]) |(\w+:\/\/\S+)", " ", tweets).split())  


def tweet():
    entry()
    topics=entry()
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

        
        T = Text(root,height=10, width=50)
        T.pack()
        T.insert(END,"**************************************************")
        T.insert(END,"\n")
        T.insert(END,"no. of positive tweets: ")
        T.insert(END,len(positive))
        T.insert(END,"\n")
        T.insert(END,"no. of negative tweets: ")
        T.insert(END,len(negative))
        T.insert(END,"\n")
        T.insert(END,"no. of neutral tweets: ")
        T.insert(END,len(neutral))
        T.insert(END,"\n")
        T.insert(END,"percentage of positive tweets: ")
        T.insert(END,posperc)
        T.insert(END,"\n")
        T.insert(END,"percentage of negative tweets: ")
        T.insert(END,negperc)
        T.insert(END,"\n")
        T.insert(END,"percentage of neutral tweets: ")
        T.insert(END,neuperc)
        T.insert(END,"\n")
        T.insert(END,"**************************************************")


        
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
        print("Twitter doesn't have any tweets regarding the entered topic")
        t1=Text(root,height=2, width=30)
        t1.pack
        t1.insert(END,"Twitter doesn't have any tweets regarding the entered topic")
    except tweepy.error.TweepError:
        print("NO INTERNET!!! Check your internet connection")
        t2=Text(root,height=2, width=30)
        t2.pack()
        t2.insert(END,"NO INTERNET!!! Check your internet connection")
        

submit = Button(root, text ="Submit", command = tweet)
label1.pack()
E1.pack()

submit.pack()


root.mainloop()

