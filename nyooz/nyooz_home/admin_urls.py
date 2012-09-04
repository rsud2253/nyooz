from django.conf.urls import *
from nyooz_home.models import Local, Home, City
from nyooz_home import views


urlpatterns = patterns('',
    url(r'^orderedmove/(?P<direction>up|down)/(?P<model_type_id>\d+)/(?P<model_id>\d+)/$','nyooz_home.views.admin_move_ordered_model',name="nyooz_home-admin-move"),
)
