import tweepy
import time


api_key = ''
api_key_secreat = ''
access_token = ''
access_token_secreat =''

auth = tweepy.OAuthHandler(api_key,api_key_secreat)
auth.set_access_token(access_token,access_token_secreat)

api = tweepy.API(auth,wait_on_rate_limit=True,wait_on_rate_limit_notify=True)

user = api.me()

#search =["#python","#ML","#Data Science","#AI"]   # search tag
search = "#python"
numTweets = 500   #rate limit


for tweet in tweepy.Cursor(api.search,search,lang="en").items(numTweets):
    try:
        print('Tweet liked')
        tweet.favorite()

        print('tweet retweeted')
        tweet.retweet()

        time.sleep(60*10) #sleep for 10 minutes
        
    except tweepy.TweepError as e:
        print(e.reason)
    except StopAsyncIteration:
        break





