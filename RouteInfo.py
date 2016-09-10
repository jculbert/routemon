from segmentInfo import SegmentInfo

class RouteInfo:

    def __init__(self):
        self.segmentInfo = []

    def addSegment(self, segmentInfo):
        self.segmentInfo.append(segmentInfo)