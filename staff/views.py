from django.views.generic import TemplateView

class StaffHomePageView(TemplateView):
    template_name = "staff/home.html"

class StaffDetailsView(TemplateView):
    template_name = "staff/details.html"