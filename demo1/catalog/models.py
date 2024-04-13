from django.db import models

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=200)

class SubCategory(models.Model):
    name = models.CharField(max_length=200)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

class Item(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    sub_category = models.ForeignKey(SubCategory, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='item_images/')
    
    likes = models.ManyToManyField('auth.User', related_name='liked_items', blank=True)

    
    def like_count(self):
        return self.likes.count() if self.likes.exists() else 0