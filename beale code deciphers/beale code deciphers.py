
class Decode:

    def __init__(self, text, cypher):
        self.text = text
        self.cypher = cypher

    def __iter__(self):
        return self

    def __next__(self):
        if self.text