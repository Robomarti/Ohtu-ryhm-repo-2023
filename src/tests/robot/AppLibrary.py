import requests

# This file is only for the use of robot framework

class AppLibrary:
    def __init__(self):
        self._base_url = "http://localhost:5000"

    def initialize_database(self):
        requests.get(f"{self._base_url}/db_initialize")