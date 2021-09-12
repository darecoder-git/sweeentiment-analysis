from textblob import TextBlob
import sys,tweepy
import matplotlib.pyplot as plt





def percentage(part,whole):
    return 100 + float(part)/float(whole)




consumerKey= "TO2Wc8Fjz3NdO4IbJY4xB8Mut"
consumerSecret= "MdXdxhTVZYREMcj4nx0PoaPWDeKKhQRUCYvTcJRF50yDz4atUj"
accessToken = "1346999544848867328-XyUmj7Y93w4YEvKOto1Qrzed8BXl0k"
accessTokenSecret= "49zp8HSJv8FjZDexCGW0TncW0RTaNtk2h0eUI5nULAzya"





auth = tweepy.OAuthHandler(consumer_key=consumerKey,consumer_secret=consumerSecret)
auth.set_access_token(accessToken,accessTokenSecret)
api=tweepy.API(auth)

searchTerm= input("Enter keyword:")
noOfSearchTerms= int(input("enter how many tweets to analyse:"))
tweets= tweepy.Cursor(api.search,  q=searchTerm ,lang="English").items(noOfSearchTerms)




positive =0
negative=0
neutral=0
polarity=0




for tweet in tweets:

    analysis= TextBlob(tweet.text)
    polarity += analysis.sentiment.polarity
    if(analysis.sentiment.polarity == 0.00):
        neutral+=1
    elif(analysis.sentiment.polarity > 0.00):
        positive+=1
    elif(analysis.sentiment.polarity < 0.00):
        negative+=1

        
positive = percentage (positive,noOfSearchTerms)
negative= percentage (negative,noOfSearchTerms)
neutral= percentage (neutral,noOfSearchTerms)




positive = format(positive, '.2f')
negative = format(negative, '.2f')
neutral = format(neutral, '.2f')




print("How people are reacting on" + str(searchTerm) + "by analysing" + str(noOfSearchTerms) + "Tweets.")


if(polarity == 0):
    print("Neutral")
elif(polarity < 0):
   print("negative")
elif(polarity > 0):
    print("positive")



labels= ['Positive [' +str(positive)+ '%]' , 'Neutral[' + str(neutral) + '%]' , 'Negative[' + str(negative) + '%]'] 

sizes = [positive, neutral, negative]
colors = ['yellowgreen','gold','red']




patches,texts = plt.pie(sizes, colors= colors ,startangle= 90)

plt.legend( patches , labels, loc="best")
plt.title('how people are reacting on' + str (searchTerm)+   'by analyzing'   + str (noOfSearchTerms) +     'Tweets.')
plt.axis('equal')
plt.tight_layout()
plt.show()