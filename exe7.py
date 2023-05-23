class Twitter:
    def __init__(self, userName):
        self.name = userName
        self.list_following = []
        self.list_followers = []
    
    def Attach(self, user):
        print(f"{user.name} added a new follower: {self.name}")
        self.list_followers.append(user)
    
    def follow(self, user):
        self.list_following.append(user)
        print(f"{self.name} is following {user.name}")
        user.Attach(self)
        return self
    
    def tweet(self, message):
        for follower in self.list_followers:
            follower.update(message)
    
    def update(self, message):
        print(f"{self.name} got a new tweet: {message}")






a = Twitter('Alice')
k = Twitter('King')
q = Twitter('Queen')
h = Twitter('Mad Hatter')
c = Twitter('Cheshire Cat')
a.follow(c).follow(h).follow(q)
k.follow(q)
q.follow(q).follow(h)
h.follow(a).follow(q).follow(c)
print(f'==== {q.name} tweets ====')
q.tweet('Off with their heads!')
print(f'\n==== {a.name} tweets ====')
a.tweet('What a strange world we live in.')
print(f'\n==== {k.name} tweets ====')
k.tweet('Begin at the beginning, and go on till you come to the end: then stop.')
print(f'\n==== {c.name} tweets ====')
c.tweet("We're all mad here.")
print(f'\n==== {h.name} tweets ====')
h.tweet('Why is a raven like a writing-desk?')