import heapq

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
        if userId not in self.followers:
            return []
        
        minHeap = []
        followees = self.followers[userId]
        for followee in followees:
            if followee in self.tweets:
                index = len(self.tweets[followee])-1
                time, tweet = self.tweets[followee][index]
                minHeap.append([-time, tweet, followee, index-1])
        heapq.heapify(minHeap)

        res = []
        while minHeap and len(res) < 10:
            _, tweet, followee, nextIndex = heapq.heappop(minHeap)
            res.append(tweet)
            if nextIndex >= 0:
                time, nextTweet = self.tweets[followee][nextIndex]
                heapq.heappush(minHeap, ([-time, nextTweet, followee, nextIndex-1]))

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