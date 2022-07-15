from django.db import models


class Detail(models.Model):
    name = models.CharField(max_length=255, null=False)
    count = models.IntegerField()

    def __str__(self):
        return self.name


class Substance(models.Model):
    name = models.CharField(max_length=255, null=False)
    count = models.IntegerField()

    def __str__(self):
        return self.name


class Technic(models.Model):
    name = models.CharField(max_length=255, null=False)
    count = models.IntegerField()

    def __str__(self):
        return self.name