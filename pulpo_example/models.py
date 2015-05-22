from django.db import models


class PulpoUser(models.Model):
    name = models.TextField(max_length=20)
    last_name = models.TextField(max_length=20)
    birthdate = models.DateField()
    has_car = models.BooleanField(default=False)

    def __str__(self):
        return self.name + " " + self.last_name


class Country(models.Model):
    name = models.TextField(max_length=30)

    def __str__(self):
        return self.name


class Club(models.Model):
    name = models.TextField(max_length=30)
    country = models.ForeignKey(Country, related_name='clubs')
    established = models.DateField()

    def __str__(self):
        return self.name + ' (' + self.country.__str__() + ')'
