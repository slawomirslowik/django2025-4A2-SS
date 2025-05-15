from django.shortcuts import render
from django.http import HttpResponse

def landing_page(request):
    return render(request, 'polls/landing_page.html')
