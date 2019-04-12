import base64
import json
import os
import requests

from dotenv import load_dotenv
from pathlib import Path  # python3 only

env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)


class Auth:
    ENVIRONMENT = None
    CREDENTIALS = {
        'client_id': None,
        'client_secret': None
    }
    OAUTH_URL = None
    SCOPE = "cobranca.registro-boletos"

    def __init__(self, prod=True):
        if prod is True:
            self.ENVIRONMENT = 'PROD'
            self.CREDENTIALS['client_id'] = os.getenv('PROD_CLIENT_ID')
            self.CREDENTIALS['client_secret'] = os.getenv('PROD_CLIENT_SECRET')
            self.OAUTH_URL = os.getenv('PROD_OAUTH_URL')
        else:
            self.ENVIRONMENT = 'HOMOL'
            self.CREDENTIALS['client_id'] = os.getenv('HOMOL_CLIENT_ID')
            self.CREDENTIALS['client_secret'] = os.getenv('HOMOL_CLIENT_SECRET')
            self.OAUTH_URL = os.getenv('HOMOL_OAUTH_URL')

    def get_access_token(self):
        params = {
            "grant_type": "client_credentials",
            "scope": self.SCOPE
        }

        headers = {
            'Content-Type': "application/x-www-form-urlencoded",
            'Authorization': "Basic {token}".format(
                token=base64.b64encode("{client_id}:{client_secret}".format(
                    client_id=self.CREDENTIALS['client_id'],
                    client_secret=self.CREDENTIALS['client_secret']
                ).encode()).decode()
            )
        }
        response = requests.request("POST", self.OAUTH_URL, data={}, headers=headers, params=params)
        return json.loads(response.text).get('access_token')
