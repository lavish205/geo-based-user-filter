from location import Location


class Customer(object):
    """
    Object of customer details
    """
    def __init__(self, user_id, name, location):
        """
        creates customer object based on the details provided
        :param user_id: user_id of the customer
        :param name: name of the customer
        :param location: location object of the customer
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
    """
    Creates the customer and location objects
    :return customer object
    """
    @classmethod
    def create(cls, user_id, name, city, lat, lon):
        location = Location.createFrom(city, lat, lon)
        customer = Customer(user_id, name, location)
        return customer

