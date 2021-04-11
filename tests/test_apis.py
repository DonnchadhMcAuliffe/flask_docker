# Python standard
from api import app

# Third party
from unittest import TestCase


class TestApis(TestCase):

    def setUp(self):
        app.config['TESTING'] = True
        self.app = app.test_client()

    def test_base_url_returns_hello(self):
        response = self.app.get('/name/id')
        self.assertEqual(
            response.status_code,
            200
        )

