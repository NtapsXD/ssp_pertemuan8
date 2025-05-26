from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'index.html')

def berita(request):
    return render(request,'berita.html')

def temp(request):
    return render(request,'temp.html')

def about(request):
    return render(request,'about.html')