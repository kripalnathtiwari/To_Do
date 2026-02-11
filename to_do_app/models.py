from django.db import models

# Create your models here.
class To_do_task(models.Model):
  task = models.CharField(max_length=255)
  task_time = models.DateField(null=True, auto_now_add=True)

  def __str__(self):
    return f"{self.task} "
class Deleted_task(models.Model):
  deleted_task = models.CharField(max_length=255)
  task_time = models.DateField(null=True, auto_now_add=True)
class compleated_task(models.Model):
  compleated_task=models.CharField
  task_time=models.DateField(null=True, auto_now_add=True)

class ListItem(models.Model):
    name = models.CharField(max_length=200)
    

    def __str__(self):
        return self.name