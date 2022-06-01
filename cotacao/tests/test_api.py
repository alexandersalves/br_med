from django.test import TestCase
from django.urls import reverse
import vcr


class GetRateViewTest(TestCase):

    def setUp(self):
        self.url = reverse('cotacao-get-rate')

    @vcr.use_cassette()
    def test_get_rate(self):
        expected = [
            'date',
            'base',
            'rates',
        ]
        response = self.client.get(self.url)
        assert list(
            response.data.keys(),
        ) == expected
