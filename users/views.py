from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages




def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            
            username = form.cleaned_data['username']
            messages.success(request, f"Account created for {username} !")
            return redirect('blog-home')


    else:
        form = UserCreationForm()

    return render(request, 'users/register.html', context={'form': form})


"""
    message.debug
    message.info
    message.success
    message.warning
    message.error
"""
