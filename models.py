from django.db import models

class Device(models.Model):
    name = models.CharField(max_length=100)
    device_type = models.CharField(max_length=50, choices=[('PC','Workstation PC'), ('SWITCH','Network Switch'), ('ROUTER','Router'), ('SERVER','Server Blade')])
    ip_address = models.GenericIPAddressField()
    is_online = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.ip_address}"
