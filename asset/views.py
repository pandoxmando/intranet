from django.views.generic import TemplateView, ListView, CreateView, UpdateView
from django.urls import reverse_lazy
from django.shortcuts import render
from .models import Asset
from .forms import CreateAsset


class assetHomePageView(TemplateView):
    template_name = "asset/asset_list.html"

class assetDetailsView(TemplateView):
    template_name = "asset/asset_details.html"


class AssetListView(ListView):
    template_name = "asset/asset_list.html"

    def get_queryset(self):
        return Asset.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['assets'] = self.get_queryset()
        return context

class AssetCreateView(CreateView):
    model = Asset
    template_name = "asset/asset_form.html"
    form_class = CreateAsset

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.fields['code'].widget.attrs.update({'class': 'form-control'})
        form.fields['serial_number'].widget.attrs.update({'class': 'form-control'})
        form.fields['specs'].widget.attrs.update({'class': 'form-control'})
        form.fields['category'].widget.attrs.update({'class': 'form-control'})
        return form

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = self.get_form()
        return context

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

    def get_success_url(self):
        return '/asset/'

class AssetUpdateView(UpdateView):
    model = Asset
    template_name = "asset/asset_form.html"

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

    def get_success_url(self):
        return 'asset_list'

class AssetDetailsView(TemplateView):
    template_name = "asset/asset_details.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        asset_id = self.kwargs.get('pk')
        context['asset'] = Asset.objects.get(pk=asset_id)
        return context 

class AssetDeleteView(UpdateView):
    model = Asset
    template_name = "asset/asset_confirm_delete.html"

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

    def get_success_url(self):
        return 'asset_list'