from django.db import models



class Tag(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name}"


class Task(models.Model):
    content = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    deadline = models.DateTimeField(null=True, blank=True, default=None)
    is_done = models.BooleanField(default=False)
    tags = models.ManyToManyField(Tag, related_name='tasks')

    class Meta:
        ordering = ['is_done', "-created"]

    def __str__(self):
        return f"{self.content}\n{self.is_done}\n{self.created}\n"





