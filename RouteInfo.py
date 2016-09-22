from segmentInfo import SegmentInfo
import json

class RouteInfo:

    def __init__(self, route_num):
        self.segment_info = []
        self.route_num = route_num
        self.summary = "Summary not set"

    def add_segment(self, segmentInfo):
        self.segment_info.append(segmentInfo)

    def add_summary(self, summary):
        self.summary = summary

    def get_segment_info_json(self):
        dict_list = []
        for info in self.segment_info:
            dict_list.append(info.to_dict())

        return json.dumps(dict_list)

