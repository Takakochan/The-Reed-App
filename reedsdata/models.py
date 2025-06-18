from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


# Create your models here.
class Reedsdata(models.Model):
    CHOICES = [(i, i) for i in range(11)]
    evaluation = models.IntegerField(choices=CHOICES, blank=True, null=True)
    reed_ID = models.CharField(null=True, max_length=220)

    def __str__(self):
        return self.reed_ID

    cane_brand = models.CharField(null=True,
                                  blank=True,
                                  max_length=220,
                                  default=None)
    gouging_machine = models.CharField(null=True, blank=True, max_length=220)
    #date = models.DateTimeField(auto_now_add=True)
    cane_diamater = models.IntegerField(null=True, blank=True, default=None)
    thicness = models.FloatField(null=True, blank=True, default=None)
    hardness = models.FloatField(null=True, blank=True, default=None)
    flexibility = models.FloatField(null=True, blank=True, default=None)
    density = models.FloatField(null=True, blank=True, default=None)
    reedauthor = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(default=timezone.now)
    shaper = models.CharField(null=True,
                              blank=True,
                              max_length=220,
                              default=None)
    harvest_year = models.CharField(null=True,
                                    blank=True,
                                    max_length=220,
                                    default=None)
    temperature = models.FloatField(null=True, blank=True, default=None)
    humidity = models.FloatField(null=True, blank=True, default=None)

    class Meta:
        unique_together = ['reed_ID', 'reedauthor']

    def get_fields(self):
        return [(field.name, getattr(self, field.name))
                for field in Reedsdata._meta.fields]
