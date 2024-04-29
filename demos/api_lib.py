import requests


class APIClient:
    API = 'https://external-api.illinois.edu/'
    
    def get(self):
        return requests.get(self.API)   

    def get_students(self):
        return requests.get(f'{self.API}students/')