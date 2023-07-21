from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'pejuma_app/Landingpage.html')

def about(request):
    return render(request, 'pejuma_app/about.html')

def contact(request):
    return render(request, 'pejuma_app/contactUs.html')

def terms(request):
    return render(request, 'pejuma_app/Terms&Condition.html')

def categories(request):
    return render(request, 'pejuma_app/categoriesList.html')