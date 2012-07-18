# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render_to_response

from nyooz_home.models import Local

def get_local(request,template_name):
	news=Local.objects.all().order_by('priority')[:5]
 	return	render_to_response(template_name,{'news':news})

	
