from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm

# Create your views here.


def register(request):
    """Register new user"""
    if request.method != 'POST':
        form = UserCreationForm()

    else:
        form =  UserCreationForm(data=request.POST)

        if form.is_valid():
            new_user =  form.save()
            # log new user in and redirect them to the  homepage
            login(request, new_user)
            return redirect('learnin_logs:index')

    context = {'form': form}
    return render(request, 'registration/register.html', context)
