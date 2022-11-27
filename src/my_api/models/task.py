from django.db import models
from my_api.models import BaseModel
from datetime import date


class Task(BaseModel):
    
    class Meta:
        db_table = 'task'
        verbose_name = verbose_name_plural = 'タスク'

    PRIORITY_CHOICES = (
        (0, '小'),
        (1, '中'),
        (2, '大'),
    )

    todo = models.CharField(
        verbose_name='やること'
        max_length=255
    )

    priority = models.IntegerField(
        verbose_name='優先度',
        choices=PRIORITY_CHOICES
    )

    complete_flag = models.BooleanField(
        verbose_name='完了フラグ',
        default=False
    )

    def __str__(self):
        return self.todo