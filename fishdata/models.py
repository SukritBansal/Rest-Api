from django.db import models
from PIL import Image

class fish(models.Model):
    fishname = models.CharField(max_length=20)
    species = models.CharField(max_length=20)
    weight = models.FloatField()
    length = models.FloatField()
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)
    timestamp = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(null=False,upload_to='pictures')

    def __str__(self):
        return self.fishname

    def save(self,*args,**kwargs):
        super().save(*args,**kwargs)

        img = Image.open(self.image.path)

        if img.height > 140 or img.width >140:
            output_size = (140,140)
            img.thumbnail(output_size)
            img.save(self.image.path) 