import sys
import csv
import re
if sys.version_info[0] < 3:
    import got
else:
    import got3 as got


def cleantweets(text):
    cleanTweet = re.sub(r"http\S+", "", text)
    cleanTweet = re.sub(r"RT", "", cleanTweet)
    cleanTweet = ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", cleanTweet).split())

    return cleanTweet


def gettweets(toUser, sinceDate, untilDate):

    tweetCriteria = got.manager.TweetCriteria().toUser(toUser).setSince(sinceDate).setUntil(
        untilDate).setMaxTweets(100000)
    tweet = got.manager.TweetManager.getTweets(tweetCriteria)

    count = 0
    with open('tweets.csv', 'w', encoding='utf-8') as f:
        writer = csv.writer(f, delimiter=',', lineterminator='\n')
        writer.writerow(['Time', 'User name', 'Raw Tweets', 'Clean Tweets'])
        for i in tweet:
            if i.username == 'CozyCo':
                pass
            else:
                time = i.date
                username = i.username
                rawtweet = i.text
                cleantweet = cleantweets(i.text)

                row = [time, username, rawtweet, cleantweet]

                writer.writerow(row)
                count += 1


    print('Retrieved {} tweets'.format(count))


toUser = 'CozyCo'
sinceDate = '2012-08-01'
untilDate = '2018-02-27'

gettweets(toUser, sinceDate, untilDate)