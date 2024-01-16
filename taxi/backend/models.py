from django.db import models
  

class Category(models.Model):
    name = models.CharField(max_length=255)
    
    def __str__(self) -> str:
        return self.name
       
    
class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    description = models.TextField()
    category = models.ForeignKey(Category, related_name='category', on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name
    
    
class Image(models.Model):
    product = models.ForeignKey(Product, related_name='product_image', on_delete=models.CASCADE)
    image = models.FileField(upload_to='images', null=True, blank=True)
    
    def __str__(self) -> str:
        return f'{self.product} - {self.image}'