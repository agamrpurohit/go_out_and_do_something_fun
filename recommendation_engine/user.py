import collections
import random


class User:
    # This class represents app user and includes the following:
    # ---Attributes---
    # Likes history
    # Dislikes history
    # Individual recommendation queue
    # ---Methods---
    # Assign (moves front choice to either like or dislike)
    # Generate recommendation stack

    def __init__(self):
        self.likes = []
        self.dislikes = []
        self.recommendations = collections.deque()

    def assign(self, destination):
        choice = self.recommendations.popleft()
        destination.append(choice)
        # Remember to remove the element from the cache 

    def generate_recommendation(self):
        engine = Engine(self.likes, self.dislikes)
        if not self.likes and not self.dislikes:
            # grab random element
            recommendation = engine.give_random()

        else:
            # Generate based on history
            recommendation = engine.generate()
        self.recommendations.append(recommendation)
