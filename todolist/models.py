from django.db import models

# Create your models here.
class Todo(models.Model):
    
    thing = models.CharField(max_length=50)
    done = models.BooleanField(default=False)
    def __str__(self):
        #输出的时候会显示成XX
        return self.thing 

    def get_absolute_url(self):
        return reverse("Todo_detail", kwargs={"pk": self.pk})
