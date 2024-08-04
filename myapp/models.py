from django.db import models
from django.contrib.auth.models import User

class Complaint(models.Model):
    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL, related_name='complaints')
    product_name = models.CharField(max_length=255)
    purchase_date = models.DateField()
    complaint_details = models.TextField()
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.product_name
