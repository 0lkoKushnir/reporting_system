'''
from django.shortcuts import render
from django.http import JsonResponse


def home(request, *args, **kwargs):
	data = {
		"sales":10,
		"customers":100,
	}
	return render(request, 'report/home.html')
	#return JsonResponse(data)

'''
from django.shortcuts import render
from django.views.generic import TemplateView
from .models import CountryModel, SalesRegionCategoryModel, SalesCountryMonthModel


def home(request):
	return render(request, 'report/home.html')


class CountryChartView(TemplateView):
	template_name = 'report/country.html'

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['qs'] = CountryModel.objects.all()
		return context


class SalesRegionCategoryChartView(TemplateView):
	template_name = 'report/salesRegionCategory.html'

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['qs'] = SalesRegionCategoryModel.objects.all()
		return context


class SalesUSACategoryChartView(TemplateView):
	template_name = 'report/salesUSACategory.html'

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['qs'] = SalesRegionCategoryModel.objects.all()
		return context


class SalesNONUSACategoryChartView(TemplateView):
	template_name = 'report/salesNONUSACategory.html'

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['qs'] = SalesRegionCategoryModel.objects.all()
		return context


class SalesCountryMonthChartView(TemplateView):
	template_name = 'report/countryMonth.html'

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['qs'] = SalesCountryMonthModel.objects.all()
		return context