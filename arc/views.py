from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from datetime import datetime

def homepage(request):
	return render(request, 'landing_page.html')
