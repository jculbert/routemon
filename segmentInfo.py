class SegmentInfo:

    def __init__(self, name, duration, duration_in_traffic):

        self.name = name
        self.duration = duration
        self.duration_in_traffic = duration_in_traffic

    def to_dict(self):
        return {"name": self.name, "duration": self.duration, "duration_in_traffic": self.duration_in_traffic}
