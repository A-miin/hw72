from django.db import models

# Create your models here.
class Quote(models.Model):
    text = models.TextField(max_length=2048)
    name = models.CharField(max_length=120)
    email = models.EmailField()
    rate = models.IntegerField(default=0)
    is_moderated = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.name}: {self.text}'


