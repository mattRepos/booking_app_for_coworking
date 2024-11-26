from django.db import models

class Room(models.Model):
    
    name = models.CharField(max_length=100)
    description = models.TextField()
    price_per_night = models.DecimalField(max_digits=10, decimal_places=2)
    capacity = models.IntegerField(default=1)  # Вместимость комнаты
    is_available = models.BooleanField(default=True)  # Доступна ли комната для бронирования
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


