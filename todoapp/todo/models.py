# ToDo 아이템을 나타내는 모델을 설정합니다.
from django.db import models

class TodoItem(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return str(self.title)