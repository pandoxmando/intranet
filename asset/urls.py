from django.urls import path

from .views import AssetListView, AssetCreateView, AssetUpdateView, AssetDetailsView, AssetDeleteView
urlpatterns = [
    path('', AssetListView.as_view(), name='asset_list'),
    path('create/', AssetCreateView.as_view(), name='asset_create'),
    path('update/<int:pk>/', AssetUpdateView.as_view(), name='asset_update'),
    path('delete/<int:pk>/', AssetDeleteView.as_view(), name='asset_delete'),
    path('details/<int:pk>/', AssetDetailsView.as_view(), name='asset_details'),
]
