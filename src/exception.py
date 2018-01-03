class InvalidCustomerDataFilePath(Exception):
    """
    """
    def __init__(self, message='', *args, **kwargs):
        if not message:
            message = "CustomerFile doesn't exists. Please check the path"
        super(InvalidCustomerDataFilePath, self).__init__(message, *args, **kwargs)

class InvalidLatLonException(Exception):
    def __init__(self, message, *args, **kwargs):
        if not message:
            message = "Invalid lat long provided. Lat Long must be of type float"
        super(InvalidLatLonException, self).__init__(message, *args, **kwargs)

