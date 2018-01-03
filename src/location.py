from math import radians, cos, sin, asin, sqrt

from exception import InvalidLatLonException


class Location(object):
    """
    """
    def __init__(self, city, lat, lon):
        self._city = city
        self._latitude = lat
        self._longitude = lon

    @property
    def city(self):
        return self._city

    @property
    def latitude(self):
        return self._latitude

    @property
    def longitude(self):
        return self._longitude

    def distance_from(self, other):
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
        r = 6371  # Radius of earth in kilometers. Use 3956 for miles
        return abs(c * r)

    @classmethod
    def createFrom(cls, city, lat, lon):
        try:
            lat = float(lat)
            lon = float(lon)
        except ValueError, e:
            raise InvalidLatLonException(e.message)

        return cls(city, lat, lon)
