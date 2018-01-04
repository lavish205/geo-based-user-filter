import argparse

from src.constants import RADIUS, ORIGIN_LATITUDE, ORIGIN_LONGITUDE
from src.location import Location
from src.filters import FilterCriteria
from src.utils import get_customer_within_radius, get_customers, get_file_path, report


def main(radius, origin_lat, origin_lon, customer_file):
    # create location object of origin to compare distance with other location
    origin = Location('dublin', origin_lat, origin_lon)
    customers = get_customers(customer_file)
    filter_criteria = FilterCriteria.get_filter(0, radius)
    invited_customers = get_customer_within_radius(customers, origin, filter_criteria)
    fields = ['user_id', 'name']  # fields that need to be printed of customers
    report(invited_customers, fields)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-radius',
                        type=float,
                        default=RADIUS,
                        help='Radius which will be used as a filter criteria')
    parser.add_argument('-latitude',
                        type=float,
                        default=ORIGIN_LATITUDE,
                        help='Latitude of origin from where distance will be calculated')
    parser.add_argument('-longitude',
                        type=float,
                        default=ORIGIN_LONGITUDE,
                        help='Longitude of origin from where distance will be calculated')
    parser.add_argument('file',
                        type=str,
                        help='File path which contains data of customers')
    args = parser.parse_args()
    file_path = get_file_path(args.file)
    main(args.radius, args.latitude, args.longitude, file_path)
