from django.db import models


class BaseModel(models.Model):
    """
    全model共通のフィールドを記述
    """

    class Meta:
        abstract = True

    created_at = models.DateTimeField(
        verbose_name='登録日時',
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        verbose_name='更新日時',
        auto_now=True
    )