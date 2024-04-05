from django.db import models

# Define the Guard model
class Guard(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    work_date = models.DateField()
    description = models.TextField()
    experience = models.PositiveIntegerField()

class GuardReal(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    image = models.ImageField(upload_to='images/')
    work_date = models.DateField()
    description = models.TextField()
    experience = models.PositiveIntegerField()


class BookingReal(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    description = models.TextField()
    address = models.TextField()
    eircode = models.TextField()
    guard = models.ForeignKey(GuardReal, on_delete=models.CASCADE, related_name='bookings')