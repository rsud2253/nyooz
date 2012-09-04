from django.db import models
from datetime import datetime

# Create your models here.

class Local(models.Model):
	parent=models.ForeignKey('self',null=True,blank=True,related_name='children')
	source_paper=models.CharField(max_length=20,verbose_name='PAPER')
        source_paper_url=models.URLField(verbose_name='PAPER URL')
        source_paper_date=models.DateField(verbose_name='DATE OF PUBLICATION')
	headline=models.CharField(max_length=100)
	snapshot_of_news=models.CharField(max_length=500)
	news_url=models.URLField(verbose_name='URL')
        news_image=models.ImageField(upload_to='photos/local',blank=True,verbose_name='IMAGE')
        misc=models.CharField(max_length=20,blank=True,null=True,verbose_name='LOCALITY (LOCAL/NATIONAL/WORLD')
        enable_disable=models.BooleanField(verbose_name='ENABLE')
	#priority=models.IntegerField(verbose_name='PRIORITY')
	# added on 2nd Sept
	priority=models.IntegerField(verbose_name='PRIORITY')

	def __unicode__(self):
		return '%i - %s- %s - %s' %(self.priority,self.source_paper_date,self.source_paper,self.headline)

	class Meta:
		ordering = ["priority"]

	@staticmethod
	def extra_filters(obj):
    		if not obj.parent:
        		return {'parent__isnull': True}
    		return {'parent__id': obj.parent.id }

	def save(self):
    		if not self.id:
        		try:
        			filters = self.__class__.extra_filters(self)
            			self.priority = self.__class__.objects.filter(**filters).order_by("-priority")[0].priority + 1

        		except IndexError:
            			self.priority = 0
    		super(Local, self).save()


        
class City(models.Model):
	city_name=models.CharField(max_length=20)
	state=models.CharField(max_length=20)
	country=models.CharField(max_length=20)

	def __unicode__(self):
		return self.city_name

class Home(models.Model):
	nyooz_title=models.CharField(max_length=20)
	current_date=models.DateField(auto_now_add=True)
	current_city = models.ForeignKey(City)
	
        def __unicode__(self):
		return self.nyooz_title
	
