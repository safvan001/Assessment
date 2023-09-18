from django.db import models

class Property(models.Model):
    property_name = models.CharField(max_length=200)
    property_cost = models.CharField(max_length=50)
    property_type = models.CharField(max_length=100)
    property_area = models.CharField(max_length=100)
    property_locality = models.CharField(max_length=200)
    property_city = models.CharField(max_length=100)
    individual_property_link = models.URLField()

    def __str__(self):
        return self.property_name
class ScrapingTask(models.Model):
    name = models.CharField(max_length=100)
    successful_records = models.PositiveIntegerField(default=0)
    is_enabled = models.BooleanField(default=True)
    trigger_timing = models.CharField(max_length=100)

# Create your models here.
