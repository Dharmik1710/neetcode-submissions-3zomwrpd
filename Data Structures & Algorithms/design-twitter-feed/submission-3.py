class Twitter:

    def __init__(self):
        self.tweets = {}
        self.followers = {}
        self.clock = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        if userId in self.tweets:
            self.tweets[userId].append((self.clock, tweetId))
        else:
            self.tweets[userId] = [(self.clock, tweetId)]
            self.followers[userId] = {userId}
        self.clock+=1

    def getNewsFeed(self, userId: int) -> List[int]:
        print(self.tweets)
        print(self.followers)

        if userId not in self.followers:
            return []
        
        followees = self.followers[userId]
        tweetIdx = [0] * len(followees)
        res = []
        n = 10
        while n > 0:
            k, earliest, tweet = 0, 0, None
            for i, followee in enumerate(followees):

                tweets = self.tweets[followee]
                if tweetIdx[i] < len(tweets):
                    time, t = tweets[len(tweets) - tweetIdx[i] - 1]
                    if time >= earliest:
                        earliest = time
                        k = i
                        tweet = t
            
            if not tweet:
                break
            
            res.append(tweet)
            tweetIdx[k]+=1
            n-=1
        
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.followers:
            self.followers[followerId] = {followeeId}
        else:
            self.followers[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.followers and followerId != followeeId and followeeId in self.followers[followerId]:
            self.followers[followerId].remove(followeeId)
        

'''
users={}, key = userIds, val = [(time, tweet ids)]
tweet={}, key = tweetids, val = (time, tweet)

followers={}, key = followerid, val = set of followers including itself
'''