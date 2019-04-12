from unittest import TestCase

from sdk_bancodobrasil import Auth


class AuthTestCase(TestCase):

    def setUp(self):
        self.auth = Auth

    def test_check_if_dot_env_variables_are_eligible_for_use(self):
        auth = self.auth(prod=False)
        self.assertEqual()
