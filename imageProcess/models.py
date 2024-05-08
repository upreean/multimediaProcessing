from django.db import models
from .resize import get_filter
from PIL import Image
import numpy as np
from io import BytesIO
from django.core.files.base import ContentFile

# Create your models here.
class ImageModel(models.Model):
    imageFile = models.ImageField()

    def __str__(self):
        return str(self.id)
    
    def save(self, *arg, **kwargs):
        # open image
        pil_image = Image.open(self.imageFile)

        # convert the image to array
        cv_img = np.array(pil_image)
        img  = get_filter(cv_img)

        # convert back to pil
        img_pil = Image.fromarray(img)

        # save
        buffer = BytesIO()
        img_pil.save(buffer, format='png')
        image_png = buffer.getvalue()

        self.imageFile.save(str(self.imageFile), ContentFile(image_png), save=False)
        super().save(*arg, **kwargs)

