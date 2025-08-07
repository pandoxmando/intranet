from django.views.generic import TemplateView


class assetHomePageView(TemplateView):
    template_name = "asset/home.html"

class assetDetailsView(TemplateView):
    template_name = "asset/details.html"
