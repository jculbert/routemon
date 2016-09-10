from route import Route

class RouteRequest:
    def __init__(self,origin,destination,waypoints):
        self.origin = origin
        self.destination = destination
        self.waypoints = waypoints

def define_Route(origin,destination,waypoints)

    route1 = Route(origin,destination,waypoints)

    if route1.waypoints == None:
        response = query_route(route1.origin, route1.destination)

        routeInfo = RouteResponse(response)

    else:
        routeInfo = []
        response = query_route(route1.origin, route1.waypoints[0])
        routeInfo.append(RouteResponse(response))

        if len(route1.waypoints) == 1:
            response = query_route(route1.waypoints[0], route1.destination)
            routeInfo.append(RouteResponse(response))

        else:
            for index in range(len(route1.waypoints[:-1])):
                response = query_route(route1.waypoints[index], route1.waypoints[index + 1])
                routeInfo.append(RouteResponse(response))

            response = query_route(route1.waypoints[-1], route1.destination)
            routeInfo.append(RouteResponse(response))

def query_route(origin,destination):

    url ='https://maps.googleapis.com/maps/api/directions/json'

    params = dict(
        origin = origin,
        destination = destination ,
        key = apikey ,
        departure_time = 'now',
        avoid ='tolls'
    )

    r = requests.get(url=url,params=params).json()
    return r