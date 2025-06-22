from django.db import models

class Item(models.Model):
    id = models.AutoField(primary_key=True)  # INT AUTO_INCREMENT PRIMARY KEY
    name = models.CharField(max_length=100)  # VARCHAR(100)

    def __str__(self):
        return f"{self.id} - {self.name}"
