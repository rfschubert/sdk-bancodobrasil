import os

from unittest import TestCase

from sdk_bancodobrasil import Auth


class AuthTestCase(TestCase):

    def setUp(self):
        self.auth = Auth

    def test_check_if_dot_env_variables_are_eligible_for_use(self):
        auth = self.auth(prod=False)
        self.assertEqual(auth.CREDENTIALS['client_id'], os.getenv('HOMOL_CLIENT_ID'))
        self.assertEqual(auth.CREDENTIALS['client_secret'], os.getenv('HOMOL_CLIENT_SECRET'))
        self.assertEqual(auth.OAUTH_URL, os.getenv('HOMOL_OAUTH_URL'))

        auth = self.auth()
        self.assertEqual(auth.CREDENTIALS['client_id'], os.getenv('PROD_CLIENT_ID'))
        self.assertEqual(auth.CREDENTIALS['client_secret'], os.getenv('PROD_CLIENT_SECRET'))
        self.assertEqual(auth.OAUTH_URL, os.getenv('PROD_OAUTH_URL'))

    def test_validate_ENVIRONMENT(self):
        self.assertEqual(self.auth().ENVIRONMENT, 'PROD')
        self.assertEqual(self.auth(prod=False).ENVIRONMENT, 'HOMOL')
