from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm

# Create your views here.
def signup(request):
    if request.method == "POST":
        try:
            form = UserRegisterForm(request.POST)
            if form.is_valid():
                form.save()
                username = form.cleaned_data['username']
                messages.success(request, f'Account created for {username}')
                return redirect('pejuma_app-categories')
        except:
            messages.error(request, f'Something went wrong. Please try again later')
    else:
        form = UserRegisterForm()
    return render(request, 'pejuma_app/signup.html', {'form':form})