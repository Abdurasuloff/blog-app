from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

# Create your models here.


class Blog(models.Model):
    avtor = models.ForeignKey(User, on_delete=models.CASCADE)
    sarlavha = models.CharField(max_length=250, help_text="Bu yerga maqola sarlavhasini kiritasiz.")
    tanasi = models.TextField(help_text="Maqolaning matni.")
    vaqt = models.DateTimeField(help_text="Maqolaning vaqti", default=datetime.now())
    rasm = models.ImageField(upload_to="blog_rasmlari/", help_text="Maqola uchun rasm", blank=True, null=True)
    
    def __str__(self):
        return self.sarlavha
    
    class Meta:
        verbose_name = "Maqola"
        verbose_name_plural = "Maqolalar"
        
        
    