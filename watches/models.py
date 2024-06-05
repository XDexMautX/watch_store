from django.db import models

class Watch(models.Model):
    name = models.CharField(max_length=100)  # Добавлено поле name
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    image = models.ImageField(upload_to='watches_images/')

    def __str__(self):
        return self.name