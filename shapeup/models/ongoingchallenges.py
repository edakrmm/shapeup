from django.db import models
from shapeup.models import CustomUserModel


class ChallengesModel(models.Model):
    challenges =  models.CharField(max_length=150)
    challenger = models.ForeignKey(CustomUserModel, on_delete = models.CASCADE, related_name = 'challenge')
    class Meta:
        db_table = 'challenges'
        verbose_name = 'challenge'
        verbose_name_plural = 'challenges'

    def __str__(self):
        return self.challenges