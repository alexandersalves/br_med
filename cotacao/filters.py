import django_filters

from cotacao.models import Currency, Rate


class RateFilter(django_filters.FilterSet):
    date = django_filters.DateFromToRangeFilter()

    class Meta:
        model = Rate
        fields = ['id', 'currency', 'amount', 'date']


class CurrencyFilter(django_filters.FilterSet):
    date = django_filters.DateFromToRangeFilter(field_name='rates__date')

    class Meta:
        model = Currency
        fields = ['id', 'abbreviation', 'date']
