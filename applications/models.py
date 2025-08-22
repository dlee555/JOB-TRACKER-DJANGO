from django.db import models
from django.contrib.auth.models import User

class Application(models.Model):
    STATUS_CHOICES = [
        ("applied","Applied"),
        ("interview","Interview"),
        ("offer","Offer"),
        ("rejected","Rejected")
    ]

    user = models.ForeignKey(User,
     on_delete=models.CASCADE, 
     related_name="applications")

    company = models.CharField(max_length = 255)
    job_title = models.CharField(max_length = 255)
    application_link = models.URLField(blank = True)
    status = models.CharField(
        max_length = 20, choices = STATUS_CHOICES, default = "applied")
    date_applied = models.DateField()
    notes = models.TextField(blank=True)

    class Meta:
        ordering = ["-date_applied","-id"]

    def __str__(self):
        return f"{self.company} - {self.job_title}"