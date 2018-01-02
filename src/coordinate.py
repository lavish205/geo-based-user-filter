
from math import radians, cos, sin, asin, sqrt

class InvalidLatLonException(Exception):
    def __init__(self, throwable):
        self.message = throwable.message

class Coordinate(object):
    """
    """
    def __init__(self, lat, lon):
        self.latitude = lat
        self.longitude = lon

    def distance(self, other):
        """
        Calculate the great circle distance between two points
        on the earth (specified in decimal degrees)
        """
        # convert decimal degrees to radians
        lon1, lat1, lon2, lat2 = map(
                radians, [self.longitude, self.latitude, other.longitude, other.latitude])

        # haversine formula
        dlon = lon2 - lon1
        dlat = lat2 - lat1
        a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
        c = 2 * asin(sqrt(a))
        r = 6371 # Radius of earth in kilometers. Use 3956 for miles
        return c * r

    @classmethod
    def createFrom(cls, lat, lon):
        try:
            lat = float(lat)
            lon = float(lon)
        except ValueError, e:
            raise InvalidLatLonException(e)

        return cls(lat, lon)

class Location(object):
    """
    """
    def __init__(self, city, coordinate):
        self._city = city
        self._coordinate = coordinate

    @property
    def city(self):
        return self._city

    @property
    def location(self):
        return self._coordinate

    def distance(self, other):
        return self.location.distance(other.location)

    def __str__(self):
        return "Lat: {lat} Lon: {lon}".format(lat=self.location.latitude,
                lon=self.location.longitude)
