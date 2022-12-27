"""Define urls for dashboard package"""
from django.urls import path

from . import views

app_name = 'dashboard'

urlpatterns = [
    # path('', views.home, name="users-home"),
    path('show-health-data/<data_id>', views.show_health_data, name='show-health-data'),
    path('add-health-data/', views.add_health_data, name='add-health-data'),
    path('edit_health-data/<data_id>', views.edit_health_data, name="edit-health-data"),
    path('del_health-data/<data_id>', views.del_health_data, name="del-health-data"),
    path('print_home_page/', views.print_home_page, name="print-home-page"),

]

