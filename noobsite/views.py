from django.http import HttpResponse



def index_view(request):
    return HttpResponse("Olá n00b, esta é a página web mais básica do mundo!")
def index_view1(request):
    return HttpResponse("Olá n00b, esta é a segunda página web mais básica do mundo!")
def index_view2(request):
    return HttpResponse("Olá n00b, esta é a quartacera página web mais básica do mundo!")
def rocket(request):
    return HttpResponse("Welcome to my Django application!")

