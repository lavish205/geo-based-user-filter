# geo-based-user-filter

## project structure

```
├── customer_data.txt # customer data input file
├── LICENSE
├── main.py # Entry point of the project
├── README.md
├── src
│   ├── constants.py # contains default values
│   ├── customer.py # contains methods related to Customer
│   ├── exception.py # contains exceptions that are being used through out the project
│   ├── filters.py # contains filter criteria
│   ├── __init__.py
│   ├── location.py # contains method related to Location object
│   └── utils.py # other utilities that are being used in project
└── tests # contains all unit test
    ├── __init__.py
    ├── test_location.py
    └── test_customers.py
```

## Running the project

```
$ python main.py <customer_file_path>
```

Example
```
$ python main.py customer_data.txt
```

## Running tests

```
$ pytest test/
```
