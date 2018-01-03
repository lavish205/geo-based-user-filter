import unittest

from src.location import Location
from src.exception import InvalidLatLonException


class TestLocation(unittest.TestCase):
    """
    unit test of locations
    """
    def setUp(self):
        self.origin_lat = 53.339428
        self.origin_lon = -6.257664
        self.city = 'dublin'

    def test_create_location(self):
        location = Location.createFrom(self.city, self.origin_lat, self.origin_lon)
        self.assertEqual(type(location), Location)
        self.assertEqual(location.latitude, self.origin_lat)
        self.assertEqual(location.longitude, self.origin_lon)
        self.assertEqual(location.city, self.city)

    def test_create_location_with_string(self):
        """
        coordinate should be typecast to float if they are passed in string type
        """
        str_lat = str(self.origin_lat)
        str_lon = str(self.origin_lon)
        location = Location.createFrom(self.city, str_lat, str_lon)
        self.assertEqual(type(location), Location)
        self.assertEqual(location.latitude, self.origin_lat)
        self.assertEqual(location.longitude, self.origin_lon)

    def test_create_location_with_invalid_input(self):
        """
        coordinates are always in the form of float, if invalid
        coordinates are passed like ascii it should throw proper exception
        """
        invalid_lat = 'test_lat'
        invalid_lon = 'test_lon'
        with self.assertRaises(InvalidLatLonException):
            Location.createFrom(self.city, invalid_lat, invalid_lon)


class TestDistance(unittest.TestCase):

    def setUp(self):
        self.origin_lat = 53.339428
        self.origin_lon = -6.257664
        self.origin_city = 'dublin'
        self.source_lat = 53.2451022
        self.source_lon = -6.238335
        self.source_city = 'dublin'
        self.distance = 10.566936288868613

    def test_same_location_distance_zero(self):
        """
        this tests the functionality of distance calculation between two
        coordinates.
        distance between two coordinates should always be zero
        """
        coordinate = Location.createFrom(self.origin_city, self.origin_lat, self.origin_lon)
        duplicate_coordinate = coordinate
        distance = coordinate.distance_from(duplicate_coordinate)
        self.assertEqual(distance, 0.0)

    def test_calculate_distance(self):
        """
        this test distance between two known point to
        check if distance calculation formula is working fine.
        """
        origin_coord = Location.createFrom(self.origin_city, self.origin_lat, self.origin_lon)
        source_coord = Location.createFrom(self.source_city, self.source_lat, self.source_lon)
        distance = origin_coord.distance_from(source_coord)
        self.assertEqual(distance, self.distance)
