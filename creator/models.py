from django.db import models
from users.models import User

class Creator(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        db_table = "creator_creator"
        verbose_name = "creator"
        verbose_name_plural = "creators"
        ordering = ["-id"]

    def __str__(self):
        return self.user.email

