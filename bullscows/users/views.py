from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.views import View
# Create your views here.


class Register(View):
    template_name = 'users/registration.html'

    def get(self, request):
        context = {'form': UserCreationForm()}

        return render(request, self.template_name, context)

    def post(self, request):
        form = UserCreationForm(request.POST)
        print('post')
        if form.is_valid():
            user = form.save()
            # username = form.cleaned_data.get('username')
            # password = form.cleaned_data.get('password')
            # user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('/')
        else:
            context = {'form': form}

        return render(request, self.template_name, context)

def logout_user(request):
    logout(request)
    return redirect('/')

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        print(user)
        if user is not None:
            login(request, user)
            print('login')
            return redirect('/')
        else:
            messages.success(request, ('Ошибка при вводе логина или пароля. Попробуйте еще раз'))
            return redirect('/users/login_user/')
    return render(request, 'users/login.html', {})