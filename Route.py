class Route:

    def __init__(self, origin, destination, waypoints=None):
        self.origin = origin[0]
        self.originText = origin[1]
        self.destination = destination[0]
        self.destinationText = destination[1]
        self.waypoints = waypoints



