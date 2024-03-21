import requests
import configuration
from data import order_data


def create_order():
    response = requests.post(configuration.URL_SERVICE + configuration.ORDERS_URL,
                             json=order_data)
    return response.status_code, response.json()


def get_order_by_track():
    response = requests.get(configuration.URL_SERVICE + configuration.TRACK_URL)
    return response.status_code, response.json()