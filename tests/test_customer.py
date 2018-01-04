import json
import unittest

from main import get_customers, get_file_path, get_customer_within_radius
from src.customer import CustomerFactory, Customer
from src.exception import InvalidFilePathException
from src.filters import FilterCriteria


class TestCustomer(unittest.TestCase):
    """
    """
    def setUp(self):
        self.city = 'dublin'
        self.filename = 'customer_data.txt'
        self.file_path = get_file_path(self.filename)
        self.invalid_file_path = '/random/path/file.txt'
        self.lat = 53.339428
        self.lon = -6.257664
        self.name = 'Intercom'
        self.radius = 100
        self.user_id = 1
        self.intercom_user = CustomerFactory.create(
            self.user_id, self.name, self.city, self.lat, self.lon
        )
        self.intercom_loc = self.intercom_user.location

    def test_create_customer(self):
        """
        Test customer object creation flow
        """
        customer = CustomerFactory.create(
            self.user_id, self.name, self.city, self.lat, self.lon)
        self.assertEqual(type(customer), Customer)

    def test_get_customers_from_input_file(self):
        """
        Test return type of all customers created by using customer data file
        """
        customers = get_customers(self.file_path)
        self.customers = customers
        for customer in customers:
            self.assertEqual(type(customer), Customer)

    def test_get_customers_with_in_radius(self):
        """
        Test return type get_customer_with_in_radius method
        """
        customers = get_customers(self.file_path)
        filter_criteria = FilterCriteria.get_filter(0, self.radius)
        customers = get_customer_within_radius(customers, self.intercom_loc, filter_criteria)
        for customer in customers:
            self.assertEqual(type(customer), Customer)

    def test_get_customer_from_invalid_input_file(self):
        """
        Test for invalid customer input file
        :return:
        """
        with self.assertRaises(InvalidFilePathException):
            get_customers(self.invalid_file_path)

    def test_validate_input_file(self):
        """
        It validates each line present in file and checks for required keys.
        """
        required_keys = ('user_id', 'latitude', 'longitude', 'name')
        keys = []
        with open(self.file_path) as f:
            for line in f:
                data = json.loads(line)
                keys = data.keys()
        for key in required_keys:
            self.assertIn(key, keys)

