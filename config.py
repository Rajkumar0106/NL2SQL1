import os
from dotenv import load_dotenv

load_dotenv()

REDSHIFT_CONFIG = {
    'host': os.getenv('REDSHIFT_HOST'),
    'port': os.getenv('REDSHIFT_PORT'),
    'database': os.getenv('REDSHIFT_DB'),
    'user': os.getenv('REDSHIFT_USER'),
    'password': os.getenv('REDSHIFT_PASSWORD')
}

# Define table relationships
TABLE_RELATIONSHIPS = {
    'orders': {
        'customers': {'orders.customer_id': 'customers.customer_id'},
        'products': {'orders.product_id': 'products.product_id'}
    },
    'customers': {
        'addresses': {'customers.address_id': 'addresses.address_id'}
    }
    # Add more table relationships as needed
}