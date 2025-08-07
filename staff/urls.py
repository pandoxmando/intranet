from django.urls import path

from .views import StaffHomePageView, StaffDetailsView

urlpatterns = [
    path('', StaffHomePageView.as_view(), name='staff_home'),
    path('details/', StaffDetailsView.as_view(), name='staff_details'),
]