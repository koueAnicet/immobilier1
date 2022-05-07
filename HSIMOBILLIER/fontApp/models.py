from django.db import models
from django.forms import URLField

# Create your models here.

class SiteInfo(models.Model):
    titre = models.CharField()
    main_full = models.CharField()
    full_site_color = models.CharField()
    default_mode = models.CharField()

    create_at = models.CharField()
    delete_at = models.DateField( auto_now=False, auto_now_add=False)
    updated_at = models.DateTimeField(auto_now=True)

class Contact(models.Model):
    fac_link = models.URLField( max_length=200)
    twitter_link = models.URLField( max_length=200)
    what_link = models.URLField( max_length=200)
    linked_link = models.URLField( max_length=200)
    insta_link = models.URLField()
    email = models.EmailField( max_length=254)
    mainPhone = models.IntegerField(max_length=10)
    lat = models.FloatField()
    longi = models.FloatField()

    created_at = models.DateTimeField()
    delete_at = models.DateTimeField()
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.customer

class House(models.Model):
    rooms_number = models.IntegerField()
    main_image =
    garage_number =
    house_type = 
    house_image =
    toilette =
    adresse = 
    prix =
    lat = 
    longi = 
    agent =
