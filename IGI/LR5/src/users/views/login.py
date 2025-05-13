from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect

from users.forms.login import LoginForm


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(request, email=email, password=password)

            if user is not None:
                login(request, user)
                return redirect('dashboard')
            else:
                form.add_error(None, "Неверный email или пароль")
    else:
        form = LoginForm()

    return render(request, 'users/login.html', {'form': form})
