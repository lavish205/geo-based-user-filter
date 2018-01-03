import unittest

from src.coordinate import Coordinate, InvalidLatLonException

class TestCoordinates(unittest.TestCase):
    """
    """

    def setUp(self):
        self.origin_lat = 53.339428
        self.origin_lon = -6.257664

    def test_create_coordinates(self):
        coordinate = Coordinate.createFrom(self.origin_lat, self.origin_lon)
        self.assertEqual(type(coordinate), Coordinate)
        self.assertEqual(coordinate.latitude, self.origin_lat)
        self.assertEqual(coordinate.longitude, self.origin_lon)

    def test_create_coordinates_with_string(self):
        """
        coordinate should be typecast to float if they are passed in string type
        """
        str_lat = str(self.origin_lat)
        str_lon = str(self.origin_lon)
        coordinate = Coordinate.createFrom(str_lat, str_lon)
        self.assertEqual(type(coordinate), Coordinate)
        self.assertEqual(coordinate.latitude, self.origin_lat)
        self.assertEqual(coordinate.longitude, self.origin_lon)

    def test_create_coordinates_with_invalid_input(self):
        """
        coordinates are always in the form of float, if invalid
        coordinates are passsed like ascii it should throw proper exception
        """
        invalid_lat = 'test_lat'
        invalid_lon = 'test_lon'
        with self.assertRaises(InvalidLatLonException):
            coordinate = Coordinate.createFrom(invalid_lat, invalid_lon)

class TestDistance(unittest.TestCase):

    def setUp(self):
        self.origin_lat = 53.339428
        self.origin_lon = -6.257664
        self.source_lat = 53.2451022
        self.source_lon = -6.238335
        self.distance = 10.566936288868613

    def test_same_coordinate_distance_zero(self):
        """
        this tests the functionality of distance calculation between two
        coordinates.
        distance between two coordinates should always be zero
        """
        coordinate = Coordinate.createFrom(self.origin_lat, self.origin_lon)
        duplicate_coordinate = coordinate
        distance = coordinate.distance_from(duplicate_coordinate)
        self.assertEqual(distance, 0.0)

    def test_calculate_distance(self):
        """
        this test distance between two known point to
        check if distance calculation formula is working fine.
        """
        origin_coord = Coordinate.createFrom(self.origin_lat, self.origin_lon)
        source_coord = Coordinate.createFrom(self.source_lat, self.source_lon)
        distance = origin_coord.distance_from(source_coord)
        self.assertEqual(distance, self.distance)
