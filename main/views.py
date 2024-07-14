from django.shortcuts import render

# Create your views here.
def success(req):
    return render(req,'exito.html')

def index(req):
    return render (req, 'index.html')

def form_test(req):
    return render (req,'form_test')

