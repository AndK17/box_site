from django.shortcuts import render

from .models import DB

def index(request):
    data = DB.objects.all()
    print(data)
    return render(request, 'db/main.html', {'data':data})