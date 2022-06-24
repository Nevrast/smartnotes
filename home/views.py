from django.shortcuts import render
from datetime import datetime

from django.contrib.auth.decorators import login_required

def home(request):
    return render(request=request, template_name="home/welcome.html", context={'today': datetime.today()})

@login_required(login_url='/admin')
def authorized(request):
    return render(request=request, template_name='home/authorized.html', context={})
