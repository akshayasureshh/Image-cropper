from django.db import models
from PIL import Image


class CroppedImage(models.Model):
    file = models.ImageField(upload_to='images')
    uploaded = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.pk)
    
    def  save(self, *args,**kwargs):
        super().save(*args,**kwargs)
        img=Image.open(self.file.path)


        if img.height>850 or img.width>765:
            output_size = (850,765)
            img.thumbnail(output_size)
            img.save(self.file.path)