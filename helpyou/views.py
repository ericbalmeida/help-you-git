from django.shortcuts import render
def home(request):
    return render(request, 'helpyou/home.html')
# Create your views here.
