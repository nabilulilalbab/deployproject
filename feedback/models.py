from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.
User = get_user_model()


class Feedback(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    email = models.CharField(max_length=100)
    komentar = models.TextField()
    rating = models.IntegerField(default=5)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.email}-{self.rating}'
