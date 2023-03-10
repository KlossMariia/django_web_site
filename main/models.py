from django.db import models

# Create your models here.

class Task(models.Model):
    title = models.CharField('Task Name', max_length=50)
    task = models.TextField('Task Description')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Task'
        verbose_name_plural = 'Tasks'
