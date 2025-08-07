from django.urls import path

from .views import assetHomePageView, assetDetailsView 
urlpatterns = [
    path('', assetHomePageView.as_view(), name='asset_home'),  
    path('details/', assetDetailsView.as_view(), name='asset_details'),
]
