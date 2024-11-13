import os, requests, base64
from dotenv import load_dotenv

load_dotenv("keys.env")
API_key = os.getenv("API_KEY")

class DataParser:
    def __init__(self, filters={}, API_key = API_key):
        self.API_key = API_key
        self.encoded_key = base64.b64encode(bytes("aEcS9UfAagInparSiv23aoa_vPzxqWvm:", 'utf-8')).decode()
        self.headers = {"Authorization": f"Basic {self.encoded_key}", **filters}

    def get_advertisements(self):
        response = requests.get("https://inpars.ru/api/v2/estate",
                                    headers={**self.headers}, params={"typeAd":'2', "fields":"id,cityId,floor,sq,cost"}).json().get('data')

        return response

