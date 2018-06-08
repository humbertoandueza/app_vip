from django.shortcuts import render
from django.http import HttpResponse

from django.shortcuts import redirect

# Create your views here.
def index(request):
	return render(request,'landing_page/index.html')
def panel(request):
	return render(request,'panel_admin/index.html')
def muestra_1(request):
	return render(request,'panel_admin/muestra.html')
def muestra_2(request):
	return render(request,'panel_admin/muestra_2.html')