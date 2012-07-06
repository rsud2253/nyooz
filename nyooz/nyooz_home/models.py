from django.db import models
from datetime import datetime

# Create your models here.

class Local(models.Model):
	source_paper=models.CharField(max_length=20)
        source_paper_date=models.DateField()
	headline=models.CharField(max_length=100)
	snapshot_of_news=models.CharField(max_length=500)
	news_url=models.URLField()
        news_image=models.ImageField(upload_to='photos/local')
        misc=models.CharField(max_length=20)
        enable_disable=models.BooleanField()

        
class City(models.Model):
	city_name=models.CharField(max_length=20)
	state=models.CharField(max_length=20)
	country=models.CharField(max_length=20)

class Home(models.Model):
	nyooz_title=models.CharField(max_length=20)
	current_date=models.DateField(auto_now_add=True)
	current_city = models.ForeignKey(City)
	
	
