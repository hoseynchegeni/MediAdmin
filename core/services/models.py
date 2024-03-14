from django.db import models
from datetime import date
from reception.models import Reception
from booking.models import Appointment

# Create your models here.

DAYS_OF_WEEK = (
    (0, "Monday"),
    (1, "Tuesday"),
    (2, "Wednesday"),
    (3, "Thursday"),
    (4, "Friday"),
    (5, "Saturday"),
    (6, "Sunday"),
)


class Service(models.Model):
    name = models.CharField(max_length=255)
    doctor = models.ForeignKey(
        "doctor.Doctor", on_delete=models.SET_NULL, blank=True, null=True
    )
    description = models.TextField(blank=True, null=True)
    category = models.ForeignKey(
        "ServiceCategory", on_delete=models.SET_NULL, blank=True, null=True
    )
    duration = models.PositiveIntegerField()  # Duration in minutes
    price = models.DecimalField(max_digits=10, decimal_places=2)
    preparation_instructions = models.TextField(blank=True, null=True)
    documentation_requirements = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    therapeutic_measures = models.TextField(blank=True)  # اقدمات درمانی
    recommendations = models.TextField(blank=True)  # توصیه ها
    # suggested_prescription = 0
    appointment_per_day = models.PositiveIntegerField(default=3)
    off_days = models.ManyToManyField("OffDay", blank=True)

    @property
    def today_reception_count(self):
        # Get today's date
        today = date.today()
        # Filter receptions for today and this service
        receptions_today = self.reception_set.filter(date=today)
        # Count the number of receptions
        return receptions_today.count()

    @property
    def total_reception_count(self):
        return Reception.objects.filter(service=self).count()

    @property
    def appointment_count_today(self):
        today = date.today()
        return Appointment.objects.filter(service=self, date=today).count()

    @property
    def waiting_receptions_today(self):
        today = date.today()
        return self.reception_set.filter(date=today, status="WAITE").count()

    def __str__(self):
        return self.name


class OffDay(models.Model):
    day_of_week = models.PositiveSmallIntegerField(choices=DAYS_OF_WEEK)

    def __str__(self):
        return DAYS_OF_WEEK[self.day_of_week][1]


class ServiceConsumable(models.Model):
    service = models.ForeignKey("services.Service", on_delete=models.CASCADE)
    consumable = models.ForeignKey("asset.Consumable", on_delete=models.CASCADE)
    dose = models.CharField(max_length=10, blank=True, null=True)
    note = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(
        "accounts.User", on_delete=models.SET_NULL, blank=True, null=True
    )

    def __str__(self):
        return f"{self.service}.{self.consumable}"


class ServiceCategory(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(
        "accounts.User", on_delete=models.SET_NULL, blank=True, null=True
    )

    def __str__(self):
        return self.name
