from django.shortcuts import render
from django.http import HttpResponse
from .models import Image

# Create your views here.
def index( request):
    query=request.GET.get('q')
    results=Image.objects.filter(keywords__icontains=query) if query else []
    return render (request,'HomePage/main.html',{'results':results,"query":query})