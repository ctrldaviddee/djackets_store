# handle images ans resizing
# import datetime
from io import BytesIO
from PIL import Image

from django.core.files import File
from django.db import models

class Category(models.Model):
    """
    Represents a product category.

    Categories are used to group related products and provide a hierarchical structure for navigation.
    """
    name = models.CharField(max_length=255)
    slug = models.SlugField()
    
    # change the behvior of model fields
    class Meta:
        verbose_name_plural = 'Categories'
        ordering = 'name',
       
    def __str__(self):
        """
        Return the string representation of the category.

        This method returns the category's name as its string representation.

        Returns:
            str: The category's name.
        """
        return self.name
    
    def get_absolute_url(self):
        """
        Return the absolute URL of the category.

        Constructs and returns the absolute URL for the category detail page.

        Returns:
            str: The absolute URL of the category.
        """
        # address of the category
        return f'/{self.slug}/'
    
class Product(models.Model):
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    slug = models.SlugField()
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    image = models.ImageField(upload_to='uploads/', blank=False, null=False)
    thumbnail = models.ImageField(upload_to='uploads/', blank=True, null=True)
    date_added = models.DateTimeField(auto_now_add=True)
    # date_added = models.DateTimeField(datetime.now)
    
    class Meta:
        ordering = '-date_added',
       
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        # address of the category
        return f'/{self.category.slug}/{self.slug}/'
    
    def get_image(self):
        return f'http://localhost:8000{self.image.url}' if self.image else ''

    def get_thumbnail(self):
        if self.thumbnail:
            return f'http://localhost:8000{self.thumbnail.url}'

        if self.image:
            self.thumbnail = self.make_thumbnail(self.image)
            self.save()
            return f'http://localhost:8000{self.image.url}'

        else:
            return ''
            
    def make_thumbnail(self, image, size=(300, 200)):
        img = Image.open(image)
        img.convert('RGB'),
        img.thumbnail(size)
        
        thumb_io = BytesIO()
        img.save(thumb_io, 'JPEG', quality=85),
        
        thumbnail = File(thumb_io, name=image.name)
        
        return thumbnail
    