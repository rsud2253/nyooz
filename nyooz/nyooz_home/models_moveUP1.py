from django.db import models
from datetime import datetime
from django import forms
from django.contrib import admin

# Create your models here.

class Local(models.Model):
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
	# added on 2nd Sept (moveUP)
	priority=models.IntegerField(verbose_name='PRIORITY',editable=False)

	def __unicode__(self):
		return '%i - %s- %s - %s' %(self.priority,self.source_paper_date,self.source_paper,self.headline)

        # added on 2nd sept (moveUP)
	def move(self,move):
		if move == 'UP':
			mm = Local.objects.get(priority=self.priority-1)
			mm.priority +=1
			mm.save()
			self.priority -=1
			self.save()

class LocalAdminForm(forms.ModelForm):
	move=forms.CharField(widget=forms.Select)
	move.required=False
	move.widget.choices=(
			(models.BLANK_CHOICE_DASH[0]),
			('FIRST','First'),
			('UP','up'),
			('DOWN', 'Down'),
			('LAST', 'Last'),
			    )
	class Meta:
		model = Local
			   
class LocalAdmin(admin.ModelAdmin):
	form=LocalAdminForm

	def save_model(self,request,obj,form,change):
		obj.save()
		move=form.cleaned_data['move']
		obj.move(move)

	

        
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
	
admin.site.register(Local,LocalAdmin)
