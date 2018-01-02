import json

from src.coordinate import Location, Coordinate
from src.customer import Customer, CustomerFactory
from src.filters import FilterCriteria


def get_customers(input_file):
    """
    Creates the list of customer objects by parsing input file.
    :returns list of customer object
    """
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

def report(customers_data, fields):
    """
    """
    if not isinstance(fields, list):
        raise ValueError("fields must be an instance of list")

    for customer in customers_data:
        values = [str(getattr(customer, field)) for field in fields]

        line = " ".join([str(x) for x in values])
        print line

if __name__ == '__main__':
    RADIUS = 100
    ORIGIN_LAT = 53.339428
    ORIGIN_LON = -6.257664
    origin_coordinate = Coordinate.createFrom(ORIGIN_LAT, ORIGIN_LON)
    origin = Location('dublin', origin_coordinate)
    customers = get_customers('src/customer_data.txt')
    filter_criteria = FilterCriteria.get_filter(RADIUS)
    invited_customers = get_customer_within_radius(customers, origin, filter_criteria)
    fields = ['user_id', 'name']
    report(invited_customers, fields)
