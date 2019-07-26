import re
import matplotlib.pyplot as plt
import numpy as np
import tweepy
from textblob import TextBlob  # text/tweet parse
from tweepy import OAuthHandler
from tkinter import*





api_key="eKfzeYoZWFUQ7g4ogx6KeZqRs"
api_secret_key="suBMejO4npo3V5DjEGe3CiO3hYByPY37h4YVm7YqxqGpIMbOXn"

access_token ="1140296275755036672-zOAtEJ4uUD3jU7Xw0Lhugi8smm656m"
access_token_secret="xhRYHDe9JjaJO9X2el2PW2caBX9SL1YisciOdvkZNplJY"




auth = OAuthHandler(api_key, api_secret_key)
# set access token and secret
auth.set_access_token(access_token, access_token_secret)
# create tweepy API object to fetch tweets
api = tweepy.API(auth)


root = Tk()
root.title("Twitter Sentiment Analysis") 
root.geometry('1000x800')
root.configure(bg="#E1E8ED")
root.iconbitmap(r"E:\Twitter_Logo_Blue.ico")

# taking image from the directory and storing the source in a variable
icon =PhotoImage(file = r"E:\oauth_application.png")
icon1=PhotoImage(file=r"E:\sentimentanalysis.png")
# displaying the picture using a 'Label' by passing the 'picture' variriable to 'image' parameter
background =Label(root, image = icon,bg="#E1E8ED")
background.pack()
background1=Label(root,image=icon1)
background1.pack(side="bottom")

#get data from the user
label1 = Label(root, text="Search",font="Helvetica 20 bold",bg="#E1E8ED")
E1 = Entry(root, bd =5,font="gotham",bg="#F5F8FA")




#cleaning up the data which is not required
def clean_data(tweets):
    return ' '.join(re.sub(r"(@[A-Za-z0-9]+)|([^0-9A-Za-z \t]) |(\w+:\/\/\S+)", " ", tweets).split())  


def tweet():
    topics=E1.get()
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
        posperc=round((len(positive)*100)/total,2)
        negperc=round((len(negative)*100)/total,2)
        neuperc=round((len(neutral)*100)/total,2)

        
        T = Text(root,height=9, width=50,bd=5,font="gotham",bg="#F5F8FA")
        T.pack()
        T.insert(END,"********************************************************************"+"\n")
        T.insert(END,"No. of positive tweets: "+str(len(positive))+"\n")
        T.insert(END,"No. of negative tweets: "+str(len(negative))+"\n")
        T.insert(END,"No. of neutral tweets: "+str(len(neutral))+"\n"+"\n")
        T.insert(END,"Percentage of positive tweets: "+str(posperc)+"%"+"\n")
        T.insert(END,"Percentage of negative tweets: "+str(negperc)+"%"+"\n")
        T.insert(END,"percentage of neutral tweets: "+str(neuperc)+"%"+"\n")
        T.insert(END,"********************************************************************")


        
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
        t1=Text(root,height=1, width=60,font="gotham",bd=5,bg="#F5F8FA")
        t1.pack()
        t1.insert(END,"OOPS!!!Twitter doesn't have any tweets regarding the entered topic")
    except tweepy.error.TweepError:
        t2=Text(root,height=1, width=45,font="gotham",bd=5,bg="#F5F8FA")
        t2.pack()
        t2.insert(END,"NO INTERNET!!! Check your internet connection")
        

submit = Button(root, text ="Submit", command = tweet,font="gotham",bg="#E1E8ED",bd=5,relief="raised")
label1.pack()
E1.pack()

submit.pack()


root.mainloop()

