# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render_to_response,render
#from django.template import RequestContext

from nyooz_home.models import Local

def get_local(request,template_name):
	news=Local.objects.all().order_by('priority')[:5]
 	#return	render_to_response(template_name,{'news':news},context_instance=RequestContext(request))
	return render(request, template_name,{'news':news})

	
	
