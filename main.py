
from src.location import Location
from src.filters import FilterCriteria
from src.utils import get_customer_within_radius, get_customers, get_file_path, report


if __name__ == '__main__':
    # constants
    RADIUS = 100
    ORIGIN_LAT = 53.339428
    ORIGIN_LON = -6.257664
    FILENAME = 'customer_data.txt'

    # create location object of origin i.e. dublin to compare distance with other location
    origin = Location('dublin', ORIGIN_LAT, ORIGIN_LON)
    file_path = get_file_path(FILENAME)  # get file path of customer data file
    customers = get_customers(file_path)
    filter_criteria = FilterCriteria.get_filter(0, RADIUS)
    invited_customers = get_customer_within_radius(customers, origin, filter_criteria)
    fields = ['user_id', 'name']  # fields that need to be printed of customers
    report(invited_customers, fields)
