import json
import os
import unittest

from main import get_customers, get_customer_filepath
from src.coordinate import Coordinate, Location
from src.customer import CustomerFactory, Customer
from src.exception import InvalidCustomerDataFilePath


class TestCustomer(unittest.TestCase):
    """
    """
    def setUp(self):
        self.lat = 53.339428
        self.lon = -6.257664
        self.user_id = 1
        self.name = 'Intercom'
        self.file_path = get_customer_filepath()
        self.invalid_file_path = '/random/path/file.txt'

    def test_create_customer(self):
        customer = CustomerFactory.create(
            self.user_id, self.name, self.lat, self.lon)
        self.assertEqual(type(customer), Customer)

    def test_get_customers_from_input_file(self):
        """
        """
        customers = get_customers(self.file_path)
        for customer in customers:
            self.assertEqual(type(customer), Customer)

    def test_get_customer_from_invalid_input_file(self):
        with self.assertRaises(InvalidCustomerDataFilePath):
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

