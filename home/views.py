from django.shortcuts import render
from datetime import datetime

def home(request):
    return render(request=request, template_name="home/welcome.html", context={'today': datetime.today()})
