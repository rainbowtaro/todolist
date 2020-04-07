from django.db import models

# Create your models here.

PRIORITY =(('danger','hight'),('info','nomal'),('success','low')) #タプルを用いている

class TodoModel(models.Model):
    title = models.CharField(max_length=100)
    priority = models.CharField(
        max_length =50,
        choices = PRIORITY
    )
    duedate = models.DateField()
    memo = models.TextField()
    def __str__(self):
        return self.title