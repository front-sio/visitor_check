
from django.urls import path
from .views import *
from customer.views import *
from avocado.views import *
from django.views.decorators.csrf import csrf_exempt


urlpatterns = [
    path('', reception_dashboard, name="rec_dashboard"),
    path('visitors/', reception_visitor, name="rec_visitors"),
    path('offices/', reception_office, name="rec_offices"),
    
]