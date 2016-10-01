class Route:

    def __init__(self, route_num, user_name, route_name, points, query_time, summary=None):
        self.route_num = route_num
        self.user_name = user_name
        self.route_name = route_name
        self.points = points
        self.query_time = query_time
        if summary:
            self.summary = summary
        else:
            self.summary = "No summary"

    def to_dict(self):

        points = []
        for p in self.points:
            points.append(p.to_dict())

        return {"route_num": self.route_num, "user_name": self.user_name, "route_name": self.route_name,
                "summary": self.summary, "points": points, "query_time": str(self.query_time)}


