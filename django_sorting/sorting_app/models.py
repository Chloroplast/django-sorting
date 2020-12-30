from django.core.validators import validate_comma_separated_integer_list
from django.db import models
from datetime import datetime


class SortRun(models.Model):
    algorithm = models.CharField(max_length=100)
    data = models.CharField(validators=[validate_comma_separated_integer_list], max_length=10000, default="")
    elapsed_time = models.FloatField(default=-1)
    date = models.DateField(default=datetime.now)

