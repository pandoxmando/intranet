from django.views.generic import TemplateView
from django.shortcuts import render
from .models import Asset


class assetHomePageView(TemplateView):
    template_name = "asset/home.html"

class assetDetailsView(TemplateView):
    template_name = "asset/details.html"

class AssetList(request):
    assets = Asset.objects.all()
    # return render(request, 'assets/asset_list.html', {'assets': assets})

# class AssetDetailView(request, serial_number):
#     asset = Asset.objects.get(serial_number=serial_number)
#     return render(request, 'assets/asset_details.html', {'asset': asset})
