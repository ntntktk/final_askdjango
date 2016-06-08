from django.shortcuts import redirect, render
from django.conf import settings
from django.contrib.auth.forms import UserCreationForm
from blog import views

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('blog:index')
    else:
        form = UserCreationForm()
    return render(request, 'accounts/signup_form.html',{
        'form': form,
        })