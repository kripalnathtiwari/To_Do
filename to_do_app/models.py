from django.db import models

class List(models.Model):
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.title


class ListItem(models.Model):
    list = models.ForeignKey(
        List,
        on_delete=models.CASCADE,
        related_name="items"
    )
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name
