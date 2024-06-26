import requests


class APIClient:
    API = 'https://external-api.illinois.edu/'
    
    def get(self):
        return requests.get(self.API)   

    def post(self, data):
        return requests.post(f'{self.API}record/', data)