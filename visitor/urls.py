from django.urls import path
from .views import *
from django.views.decorators.csrf import csrf_exempt
from reception.views import *

urlpatterns = [
    path('', dashboard, name="customer_dashboard"),
    path('visitors/', visitors_view, name="visitors"),
    path('offices/', offices_view, name="offices"),
    path('visitors/save/', save_visitor, name="save_visitor"),
    path('visitor_form/', visitor_form, name="visitor_form"),
    path('visitorform/', saveForm, name="saveForm"),
    # path('search_result/', search_view, name="search_result"),
    path('check/', kyc, name="check"),
    path('search_office/', search_office_view, name="search_office"),
    path('search_form/<int:pk>', search_form, name="search_form"),
    path('delete/visitor/<int:pk>', delete_visitor, name="delete_visitor"),

    # office data
    path('office_form/', office_form, name="office_form"),
    path('save_office/', save_office, name="save_office"),
    path('delete/office/<int:pk>', delete_office, name="delete_office"),


     # live data display
    path('visitors/live_session/', live_visitor, name="customer_live_session_visitors"),
    path('visitors/dashboard/live_session/', live_customer_dashboard, name="customer_d_live_session_visitors"),
    path('offices/live_session/', customer_offices_live, name="customer_live_session_offices"),
    path('offices/dashboard/live_session/', customer_offices_live_dashboard, name="customer_d_live_session_offices"),
 
]
