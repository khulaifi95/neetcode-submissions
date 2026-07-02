class Twitter:

    def __init__(self):
        self.count = 0
        self.followers = collections.defaultdict(set)
        self.posts = []

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.posts.append((self.count, userId, tweetId))
        self.count -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        k = 10
        res = []
        for i in range(len(self.posts) - 1, -1, -1):
            if k == 0:
                break
            rec, foId, tweetId = self.posts[i]
            if foId in self.followers[userId] or foId == userId:
                res.append(tweetId)
                k -= 1
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followers[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.followers[followerId].discard(followeeId)