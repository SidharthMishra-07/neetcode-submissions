class Twitter:
    def __init__(self):
        self.time = 0
        self.tweetMap = defaultdict(list) # list {userID: [time, tweetID], [time-1, tweetID]}
        self.followMap = defaultdict(set) # set {userID: {5,2,3,..}}

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweetMap[userId].append([self.time, tweetId])
        self.time -=1

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        minheap = []
        self.followMap[userId].add(userId) #ensuring the user follows itself

        #Taking only the most recent tweet from all followers including user and
        #adding it to minheap.
        for followee in self.followMap[userId]:
            if followee in self.tweetMap:
                index = len(self.tweetMap[followee]) -1
                time, tweetId = self.tweetMap[followee][index]
                heapq.heappush(minheap, [time, tweetId, followee, index - 1])
            
            #merge k sorted
        while minheap and len(res) < 10:
            time, tweetId, followee, index = heapq.heappop(minheap)
            res.append(tweetId)

            if index>=0:
                time, tweetId = self.tweetMap[followee][index]
                heapq.heappush(minheap, [time, tweetId, followee, index-1])

        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followMap[followerId]:
            self.followMap[followerId].remove(followeeId)
