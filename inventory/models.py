# models.py
from django.db import models

class Item(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, unique=True)  # 💡 unique=True eklendi

    def __str__(self):
        return f"{self.id} - {self.name}"