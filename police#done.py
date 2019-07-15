import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS 



file=pd.read_csv(r'E:\data python files\Public_Tweets_Police.csv')
#print(file.shape)
#print(file.info())
#print(file.columns)
#df=file.city_police.value_counts()
#print(df)

comment_words=" "
stopwords = set(STOPWORDS)
#print(stopwords)
for val in file.Tweet: 
     
    # typecaste each val to string 
    val = str(val) 
    #clean_data(val)
    # split the value 
    tokens = val.split(' ')  #break the string by space seperator 
    
    # Converts each token into lowercase 
    for i in range(len(tokens)): 
        tokens[i] = tokens[i].lower()  #convert every word to lower case 
          
    for words in tokens: 
         comment_words = comment_words + words + ' '

#print(comment_words)

wordcloud = WordCloud(width = 700, height = 600, 
                background_color ='white', 
                stopwords = stopwords,
                colormap='rainbow',
                max_font_size=50, min_font_size=10).generate(comment_words)

# plot the WordCloud image                        
plt.figure(figsize = (7, 6), facecolor = None) 
plt.imshow(wordcloud, interpolation='bilinear') 
plt.axis("off")  #dont' show x and y axis 
plt.tight_layout(pad = 0) #no space   
plt.show()
sns.countplot(x='city_police',data=file)
plt.show()