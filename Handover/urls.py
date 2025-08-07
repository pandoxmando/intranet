from django.urls import path

from .views import handoverDetailsView, handoverHomePageView

urlpatterns = [
    path('', handoverHomePageView.as_view(), name='handover_home'),
    path('details/', handoverDetailsView.as_view(), name='handover_details'),
]