from django.db import models

class StudentModel(models.Model):
    roll = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=20)
    father_name = models.CharField(max_length=30)
    address = models.TextField()

    def __str__(self):
        return f"Roll : {self.roll} Name: {self.name}"