import os


class Auth:
    ENVIRONMENT = None
    CREDENTIALS = {
        'client_id': None,
        'client_secret': None
    }
    OAUTH_URL = None

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

    # def get_token(self):
    #     return ""
