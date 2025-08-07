from django.db import models

CATEGORIES = [("LPT", "Laptop"), ("MOB", "Mobile Phone"), ("PRT", "Printer"), ("DSK", "Desktop"), ("AIO", "All In One"), ("TV", "Television")]
# Create your models here.
class Asset(models.Model):
    code = models.CharField(max_length=100, null=False)
    serial_number = models.CharField(max_length=100, null=False)
    specs = models.TextField(max_length=100, null=False)
    category = models.CharField(max_length=50, null=False, choices=CATEGORIES)

    def __str__(self):
        return f'{self.serial_number} - {self.category}'
