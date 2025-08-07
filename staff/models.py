from django.db import models

DEPS = [("ADMIN", "Administration"), ("ACC", "Accounts"), ("CF", "C&F"), ("FN", "Finance"), ("HR", "Human Resourse"), ("OPS", "Operations")]
# Create your models here.
class Staff(models.Model):
    reg_number = models.CharField(max_length=100, null=False)
    name = models.CharField(max_length=100, null=False)
    department = models.CharField(max_length=50, null=False, choices=DEPS)

    def __init__(self):
        return f'{self.name} - {self.department}'
