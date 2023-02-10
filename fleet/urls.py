from django.urls import path
from .views import (FleetListView, FleetUpdateView, FleetDeleteView, DriverListView, DriverUpdateView, 
                    DriverDeleteView, )

add_name = 'fleet'

urlpatterns = [
    path('', FleetListView.as_view(), name="view_fleet"),
    path('create-fleet', FleetListView.as_view(), name="create_fleet"),
    path('edit-fleet/<int:pk>/', FleetUpdateView.as_view(), name='edit-fleet'),
    path('delete-fleet/<int:pk>/', FleetDeleteView.as_view(), name='delete-fleet'),
    path('drivers', DriverListView.as_view(), name="drivers"),
    path('edit-driver/<int:pk>/', DriverUpdateView.as_view(), name='edit_driver'),
    path('delete-driver/<int:pk>/', DriverDeleteView.as_view(), name='delete_driver'),
]
