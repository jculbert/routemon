class Point:

    def __init__(self, name, location):
        self.location = location
        self.name = name

    def to_dict(self):
        return {"location": self.location, "name": self.name}
