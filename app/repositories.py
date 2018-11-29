
class TweetRepository:
    def __init__(self):
        self.data=[]

    def add(self, tweet):
        self.data.append(tweet)
        self. data[-1].id=len(self. data)-1
        return self. data[-1].id

    def get(self,id):
        try:
            return self.data[id]
        except:
            return None

    def delete(self,id):
        try:
            del self.data[id]
        except:
            return None

    def clear(self):
        self.data=[]
