from segmentInfo import SegmentInfo
import json


class RouteInfo:

    def __init__(self):
        self.segmentInfo = []

    def addSegment(self, segmentInfo):
        self.segmentInfo.append(segmentInfo)

    def to_JSON(self):
        return json.dumps(self, default=lambda o: o.__dict__)
