from django.shortcuts import render

# Create your views here.

def usdf(request):
    d={'name':'AKash','abc':'HAi Harry How Are You','xyz':'ha ha ha hx ha hx hx'}
    return render(request,'usdf.html',d)