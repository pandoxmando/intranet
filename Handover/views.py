from django.views.generic import TemplateView

class handoverHomePageView(TemplateView):
    template_name = "handover/home.html"

class handoverDetailsView(TemplateView):
    template_name = "handover/details.html"
