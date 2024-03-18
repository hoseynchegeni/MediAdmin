from django.db import models
from django.utils.translation import gettext_lazy as _


# Create your models here.
STATUS = (
    ("WAITE", "WAITE"),
    ("DONE", "DONE"),

)

def validate_current_month(value):
    pass


def validate_max_appointments_per_day(value):
    pass


class Appointment(models.Model):
    service = models.ForeignKey("services.Service", on_delete=models.CASCADE)
    client = models.ForeignKey(
        "client.Client", on_delete=models.CASCADE, blank=True, null=True
    )
    national_code = models.CharField(max_length=100, blank=True, null=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    date = models.DateField()
    status = models.CharField(max_length = 100, choices = STATUS, blank = True, null = True)
    has_package = models.BooleanField(default = False)
    package = models.ForeignKey('PackageAppointment', on_delete = models.CASCADE, blank = True, null = True)

    def __str__(self):
        return f"{self.service}, {self.client}, {self.date}"
    
    
    
class PackageAppointment (models.Model):
    package = models.ForeignKey("services.Package", on_delete=models.CASCADE)
    client = models.ForeignKey(
        "client.Client", on_delete=models.CASCADE, blank=True, null=True
    )
    national_code = models.CharField(max_length=100, blank=True, null=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    date = models.DateField()
    status = models.CharField(max_length = 100, choices = STATUS, blank = True, null = True)

    def __str__(self):
        return f"{self.package}, {self.client}, {self.date}"
