from django.shortcuts import render

def home(request):
    return render(request, 'home.html')
def login(request):
    return render(request, 'login.html')
def register(request):
    return render(request, 'register.html')
def uhome(request):
    return render(request,'uhome.html')
def about(request):
    return render(request,'about.html')
def watchdetails(request):
    return render(request,'watchdetails.html')
def bikedetails(request):
    return render(request, 'bikedetails.html')
def cardetails(request):
    return render(request,'cardetails.html')
def thar(request):
    return render(request,'thar.html')
def rolex(request):
    return render(request,'rolex.html')