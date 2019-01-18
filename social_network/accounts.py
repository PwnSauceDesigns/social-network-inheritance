class User(object):
    def __init__(self, first_name, last_name, email):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.posts = []
        self.following = []

    def add_post(self, post):
        self.posts.append(post)

    def get_timeline(self):
        # return class objects from followed users posts
        answer = []
        for person in self.following:
            answer += person.posts
        return answer

    def follow(self, other):
        self.following.append(other)
