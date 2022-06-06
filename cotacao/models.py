from django.db import models


class Currency(models.Model):
    abbreviation = models.CharField(max_length=3)

    def __str__(self):
        return self.abbreviation


class Rate(models.Model):
    currency = models.ForeignKey(
        'Currency', on_delete=models.CASCADE, related_name='rates')
    amount = models.CharField(max_length=20)
    date = models.DateField()
    base = models.ForeignKey(
        'Currency', on_delete=models.CASCADE, related_name='based_rates')

    def __str__(self):
        return f'{self.currency} {self.amount} {self.date}'
