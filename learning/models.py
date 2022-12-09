"""Define models for learning package"""
from django.db import models
from PIL import Image
from django.utils.timezone import now

# Create your models here.
class Material(models.Model):
    """Define data for Material model"""

    title = models.CharField(max_length=100)
    img = models.ImageField(default='diabetes.png', upload_to='card_images')
    description = models.TextField()
    created_date = models.DateTimeField(default=now, editable=False)



    def __str__(self):
        return self.title
    
    # # resizing images
    def save(self, *args, **kwargs):
        """save learning cards"""

        super().save()

        image = Image.open(self.img.path)
        
        if round(image.width/image.height, 1) > 1.2:
            new_width = round(image.height * 1.2)
            new_height = image.height
            crop_l_r = round((image.width - new_width) / 2)
            image.crop((crop_l_r, 0, image.width - crop_l_r, 0))

        else:
            new_height = round(image.width / 1.2)
            new_width = image.width
            crop_t_b = round((image.height - new_height) / 2)
            image.crop((0, crop_t_b, 0, image.height - crop_t_b))

        new_img = (500, round(new_width/round(new_height/500, 2)))
        image.thumbnail(new_img)
        rgb_im = image.convert('RGB')
        rgb_im.save(self.img.path)
