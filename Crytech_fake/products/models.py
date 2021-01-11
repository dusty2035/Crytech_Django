from django.db import models

# Create your models here.

class Product(models.Model):
    main_img = models.ImageField(upload_to='images/')
    name_img = models.ImageField(upload_to='images/')
    alt_text = models.CharField(max_length=50)
    game_title = models.CharField(max_length=50)
    game_description_top = models.CharField(max_length=200)
    game_description_bottom = models.TextField()
    game_system_requirements = models.TextField()
    price = models.DecimalField(decimal_places=2 , max_digits=8)
    awards_img = models.ImageField(upload_to='images/' , blank=True)
    slide_img_1 = models.ImageField(upload_to='images/')
    slide_img_2 = models.ImageField(upload_to='images/')
    slide_img_3 = models.ImageField(upload_to='images/')
    slide_img_4 = models.ImageField(upload_to='images/')
    slide_img_5 = models.ImageField(upload_to='images/')
    slide_img_6 = models.ImageField(upload_to='images/')



    def __str__(self):
        return self.game_title