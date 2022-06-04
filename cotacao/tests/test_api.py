from django.test import TestCase
from django.urls import reverse
import vcr


class GetRateViewTest(TestCase):

    def setUp(self):
        self.url = reverse('cotacao-get-rate')

    @vcr.use_cassette(
        path_transformer=vcr.VCR.ensure_suffix('.cassettes'),
    )
    def test_get_rate(self):
        date = '03/06/2022'
        expected = [
            'date',
            'rates',
        ]
        response = self.client.get(
            self.url,
            data={
                'currency_from': 'USD',
                'currency_to': 'BRL',
                'start_date': date,
                'end_date': date,
            },
        )
        assert list(
            response.data[0].keys(),
        ) == expected
