from django.db import models
from django.contrib.auth import get_user_model

class Task(models.Model):

    STATUS = (
        ('1', 'doing'),
        ('2', 'done')
    )

    title = models.CharField(max_length=255)
    description = models.TextField()
    done = models.CharField(
        max_length=1,
        choices=STATUS
    )
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add= True)
    updated_at = models.DateTimeField(auto_now= True)

    def __str__(self):
        return self.title
# Create your models here.
