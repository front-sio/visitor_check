from django.urls import path
from .views import office_reception_save,offices_view,office_reception,office_reception_add, officeUpdate, office_visitors, office_visitor_live, office_visitors_dashboard_live

urlpatterns = [
    path('dashboard/', offices_view, name="office_dashboard"),
    path('dashboard/my_visitors/', office_visitors, name="office_visitors"),
    path('dashboard/reception/', office_reception, name="office_reception"),
    path('dashboard/reception/add/', office_reception_add, name="office_reception_add"),
    path('dashboard/reception/add/', office_reception_save, name="save_receptionist"),
    path('dashboard/update/office/<int:pk>', officeUpdate, name="update_office"),


    # live data
    path('dashboard/my_visitors/live/', office_visitor_live, name="office_visitors_live"),
    path('dashboard/live/', office_visitors_dashboard_live, name="office_dashboard_live"),
]