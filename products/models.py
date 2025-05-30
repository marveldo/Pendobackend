from django.db import models
import uuid
# Create your models here.

class Products(models.Model) :
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    name = models.CharField(max_length=200, blank = True , null=True)
    description = models.TextField(blank=True, null = True)
    product_img = models.ImageField(blank=True , null = True , upload_to='product_images')
    current_price = models.IntegerField(default=0 , blank=True , null=True)


    def __str__(self):
        return self.name


