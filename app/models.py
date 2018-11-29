# app/models.py
from datetime import datetime

class Tweet:
    def __init__(self, text):
        self.id = None
        self.text = text
        self.created_at = datetime.now()
    def __repr__(self):
        return f'<{self.id} {self.text} {self.created_at}>'
