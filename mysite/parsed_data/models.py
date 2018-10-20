## parsed_data/models.py
from django.db import models


class priceData(models.Model):
    code = models.CharField(max_length=7)
    price = models.CharField(max_length=20)