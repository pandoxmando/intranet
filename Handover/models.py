from django.db import models

CATEGORIES = [("LPT", "Laptop"), ("MOB", "Mobile Phone"), ("PRT", "Printer"), ("DSK", "Desktop"), ("AIO", "All In One"), ("TV", "Television")]
# Create your models here.
class Handover(models.Model):
    ho_date = models.DateField(auto_now_add=True)
    asset = models.ForeignKey("asset.Asset", on_delete=models.CASCADE, related_name="handover_asset")
    staff = models.ForeignKey("staff.Staff", on_delete=models.CASCADE, related_name="handover_staff")
    approved = models.BooleanField(default=False)
    approved_by_hr = models.ForeignKey("staff.Staff", on_delete=models.CASCADE, related_name="handover_approved_hr", null=True, blank=True)
    approved_by_hr_date = models.DateField(null=True, blank=True)
    approved_by_it = models.ForeignKey("staff.Staff", on_delete=models.CASCADE, related_name="handover_approved_it", null=True, blank=True)
    approved_by_it_date = models.DateField(null=True, blank=True)
    approved_by_comment = models.TextField(null=True, blank=True)

    def __str__(self):
        return f'{self.asset} - {self.staff}'
    

class HandoverReturn(models.Model):
    hr_date = models.DateField(auto_now_add=True)
    handover = models.ForeignKey(Handover, on_delete=models.CASCADE, related_name="handover_return")
    asset = models.ForeignKey("asset.Asset", on_delete=models.CASCADE, related_name="handover_return_asset")
    staff = models.ForeignKey("staff.Staff", on_delete=models.CASCADE, related_name="handover_return_staff")
    return_date = models.DateField(null=True, blank=True)
    return_condition = models.CharField(max_length=100, choices=CATEGORIES, default="LPT")

    def __str__(self):
        return f'{self.asset} - {self.staff} - {self.return_date}'