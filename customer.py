from coordinate import Location, Coordinate


class Customer(object):
    """
    """
    def __init__(self, user_id, name, location):
        """
        """
        self._user_id = user_id
        self._name = name
        self._location = location

    @property
    def name(self):
        return self._name

    @property
    def user_id(self):
        return self._user_id

    @property
    def location(self):
        return self._location


class CustomerFactory(object):
    @classmethod
    def create(cls, user_id, name, lat, lon):
        coordinate = Coordinate.createFrom(lat, lon)
        location = Location(name, coordinate)
        customer = Customer(user_id, name, location)
        return customer

