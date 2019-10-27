from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, 'index.html')
    # return HttpResponse("Sta trebA DA PISE kad je Httpresponse")

def strana1(request):
    return HttpResponse("OVO JE STRANA ! POSLE GLAVNE INDEX")