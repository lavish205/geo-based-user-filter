import json
import os

from src.customer import CustomerFactory
from src.exception import InvalidFilePathException


def get_file_path(filename):
    """
    Generates the absolute file path based on filename present in CWD
    :param filename: name of file present in CWD
    :return: absolute path of the file
    """
    return os.path.realpath(filename)


def get_customers(file_path):
    """
    Creates the list of customer objects by parsing customer data file.
    :param file_path: path of customer data text file
    :returns list of customer object
    """
    customers = []
    city = None  # storing city name as none because its not provided in customer data file
    try:
        with open(file_path, 'rb') as f:
            for line in f:
                data = json.loads(line.strip())
                customer = CustomerFactory.create(
                    data['user_id'],
                    data['name'],
                    city,
                    data['latitude'],
                    data['longitude'],
                    )
                customers.append(customer)
    except IOError:
        raise InvalidFilePathException
    return customers


def get_customer_within_radius(customers, origin, filter_criteria):
    """
    Filters out all the customers based on given filter criteria
    :param customers: list of all customer objects
    :param origin: location object (in our case its intercom dublin office location object)
    :param filter_criteria: criteria on which customers will be filtered out based on origin
    :return: sorted list of customer objects which satisfies filter criteria
    """
    invited_customers = []

    for customer in customers:
        distance = customer.location.distance_from(origin)

        if filter_criteria.satisfies(distance):
            invited_customers.append(customer)
    invited_customers.sort(key=(lambda x: x.user_id))
    return invited_customers


def report(customers_data, fields):
    """
    Print user_id and name of customer present in customers_data
    :param customers_data: list of customer objects
    :param fields: fields that need to be print of customer object
    :return: None
    """
    # fields must be an instance of list
    if not isinstance(fields, list):
        raise ValueError("fields must be an instance of list")

    for customer in customers_data:
        values = [str(getattr(customer, field)) for field in fields]

        line = " ".join([str(x) for x in values])
        print line
