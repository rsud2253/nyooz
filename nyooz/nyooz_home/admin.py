from django.contrib import admin
from nyooz_home.models import Local,Home,City
from django.contrib.contenttypes.models import ContentType
from django.core.urlresolvers import reverse

class LocalAdmin(admin.ModelAdmin):
	pass
	list_display=['priority','misc','headline','source_paper_date','order_link']
	search_fields=('headline','snapshot_of_news')
	date_hierarchy='source_paper_date'
	ordering=('priority',)

	def order_link(self, obj):
    		model_type_id = ContentType.objects.get_for_model(obj.__class__).id
    		model_id = obj.id
    		kwargs = {
       		"direction": "up", 
       		"model_type_id": model_type_id, 
       		"model_id": model_id,
   		}
    		url_up = reverse("nyooz_home-admin-move", kwargs=kwargs)
    		kwargs["direction"] = "down"
    		url_down = reverse("nyooz_home-admin-move", kwargs=kwargs)
    		return '<a href="%s" class="up">%s</a><a href="%s" class="down">%s</a>' % ( url_up, 'UP', url_down, 'down')
	order_link.allow_tags = True
	order_link.short_description = 'Move'
	order_link.admin_order_field = 'priority'

	@staticmethod
	def move_down(model_type_id, model_id):
    		try:
        		ModelClass = ContentType.objects.get(id=model_type_id).model_class()

        		lower_model = ModelClass.objects.get(id=model_id)
        		filters = ModelClass.extra_filters(lower_model)
        		filters['priority__gt'] = lower_model.priority
        		higher_model = ModelClass.objects.filter(**filters)[0]

        		lower_model.priority, higher_model.priority=higher_model.priority, lower_model.priority

        		higher_model.save()
        		lower_model.save()
    		except IndexError:
         		pass
                except ModelClass.DoesNotExist:
        		pass

	@staticmethod
	def move_up(model_type_id, model_id):
    		try:
        		ModelClass = ContentType.objects.get(id=model_type_id).model_class()
        		higher_model = ModelClass.objects.get(id=model_id)

        		filters = ModelClass.extra_filters(higher_model)
        		filters['priority__lt'] = higher_model.priority
        		lower_model = ModelClass.objects.filter(**filters).reverse()[0]

        		lower_model.priority, higher_model.priority=higher_model.priority, lower_model.priority

        		higher_model.save()
        		lower_model.save()
    		except IndexError:
       			pass
        	except ModelClass.DoesNotExist:
        		pass

admin.site.register(Local,LocalAdmin)

admin.site.register(Home)
admin.site.register(City)
