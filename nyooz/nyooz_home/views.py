# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render_to_response,render
from django.template import Template, Context
#from django.template import RequestContext
import datetime
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.contenttypes.models import ContentType
from django.http import HttpResponseRedirect
from django.db import transaction
from nyooz_home.models import Local
from nyooz_home.admin import LocalAdmin

def get_local(request,template_name):
	#news=Local.objects.all().order_by('priority')[:5]
        news_by_date=Local.objects.all().order_by('source_paper_date')
	news_by_priority=Local.objects.all().order_by('priority')[:20]
        today=datetime.datetime.now()
 	#return	render_to_response(template_name,{'news':news},context_instance=RequestContext(request))
	return render(request, template_name,{'news_by_priority':news_by_priority,'news_by_date':news_by_date,'today':today})
	

@staff_member_required
@transaction.commit_on_success
def admin_move_ordered_model(request, direction, model_type_id, model_id):
	if direction == "up":
		LocalAdmin.move_up(model_type_id, model_id)
	else:
		LocalAdmin.move_down(model_type_id, model_id)

	ModelClass = ContentType.objects.get(id=model_type_id).model_class()

	app_label = ModelClass._meta.app_label
	model_name = ModelClass.__name__.lower()

	redirect_url = request.META.get('HTTP_REFERER')
	if redirect_url is None:
		redirect_url = "/admin/%s/%s/" % (app_label, model_name)

	return HttpResponseRedirect(redirect_url)

