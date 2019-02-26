from django.db import models


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Crop(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    uses = models.TextField()
    growing_period = models.TextField()
    further_info = models.TextField()
    Physiology = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    temp_abs_min = models.CharField(max_length=3)
    temp_abs_max = models.CharField(max_length=3)
    temp_opt_min = models.CharField(max_length=3)
    temp_opt_max = models.CharField(max_length=3)
    rf_abs_min = models.CharField(max_length=20)
    rf_abs_max = models.CharField(max_length=20)
    rf_opt_min = models.CharField(max_length=20)
    rf_opt_max = models.CharField(max_length=20)
    crop_cycle = models.TextField()

    def __str__(self):
        return self.name

