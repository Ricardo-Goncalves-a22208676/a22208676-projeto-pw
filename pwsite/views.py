from django.shortcuts import render
from datetime import datetime

def index_view1(request):
    return render(request, "pwsite/sobre.html")
def index_view2(request):
    return render(request, "pwsite/interesses.html")
def index(request):
    return render(request, "pwsite/index.html", {
        'data': datetime.today()
        })

