from django.db import models

class PostureData(models.Model):
    user_id = models.CharField(max_length=100)
    timestamp = models.DateTimeField(auto_now_add=True)
    state = models.CharField(max_length=20, choices=[
        ('normal', 'Normal'),
        ('deviated', 'Deviated'),
        ('critical', 'Critical'),
    ])
    anomaly_score = models.FloatField()
    feedback = models.TextField(blank=True)

    def __str__(self):
        return f"{self.user_id} - {self.state}"