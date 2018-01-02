import json


from coordinate import Location, Coordinate
from customer import Customer, CustomerFactory

class WithinRadiusFilterCriteria(object):
    """
    """

    def __init__(self, radius):
        self._radius = radius

    @property
    def radius(self):
        return self._radius

    def satisfies(self, distance):
        """
        """
        return abs(distance) <= self.radius

class BetweenRadiusFilterCriteria(object):
    """
    """

    def __init__(self, radius1, radius2):
        self._radius1 = radius1
        self._radius2 = radius2

    def satisfies(self, distance):
        """
        """
        distance = abs(distance)
        return self._radius1 <= distance <= self._radius2


def get_customers(input_file):
    customers = []
    with open(input_file, 'rb') as f:
        for line in f:
            data = json.loads(line.strip())
            customer = CustomerFactory.create(
                    data['user_id'],
                    data['name'],
                    data['latitude'],
                    data['longitude'],
                    )
            customers.append(customer)
    return customers



def get_customer_within_radius(customers, origin, filter_criteria):
    """
    """
    invited_customers = []

    for customer in customers:
        distance = customer.location.distance(origin)

        if filter_criteria.satisfies(distance):
            invited_customers.append(customer)
    invited_customers.sort(key=(lambda x: x.user_id))
    return invited_customers

def report(customers_data, fields=['user_id', 'name', 'location']):
    """
    """
    for customer in customers_data:
        values = [str(getattr(customer, field)) for field in fields]

        line = " ".join([str(x) for x in values])
        print line

if __name__ == '__main__':
    RADIUS = 100
    origin_coordinate = Coordinate.createFrom(53.339428, -6.257664)
    origin = Location('dublin', origin_coordinate)
    customers = get_customers('customer_data.txt')
    filter_criteria = WithinRadiusFilterCriteria(RADIUS)
    filter_criteria = BetweenRadiusFilterCriteria(50, 100)
    invited_customers = get_customer_within_radius(customers, origin, filter_criteria)

    report(invited_customers)
