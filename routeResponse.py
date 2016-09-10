from leg import RouteLeg

class RouteResponse:

    def __init__(self, response):

        self.legs = []

        r_legs_list = response['routes'][0]['legs']
        for r_leg_dict in r_legs_list:
            leg = RouteLeg(r_leg_dict)
            self.legs.append(leg)

        #self.duration_in_traffic = (response['routes'][0]['legs'][0]['duration_in_traffic']['text'])
        #self.duration_no_traffic = (response['routes'][0]['legs'][0]['duration']['text'])