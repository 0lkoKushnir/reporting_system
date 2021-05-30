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




def home(request):
	return render(request, 'report/home.html')