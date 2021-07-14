from django.contrib.auth import login, logout,authenticate
from django.shortcuts import redirect, render
from django.contrib import messages
from django.views.generic import CreateView
from django.views.decorators.csrf import csrf_exempt,csrf_protect #Add this
from accounts.forms import HandlerRegisterationForm, GeneratorRegisterationForm
from django.contrib.auth.forms import AuthenticationForm
from .models import User

def register(request):
    return render(request, '../templates/index.html')

class generator_register(CreateView):
    model = User
    form_class = GeneratorRegisterationForm
    template_name = '../templates/register.html'

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('index')

class handler_register(CreateView):
    model = User
    form_class = HandlerRegisterationForm
    template_name = '../templates/register.html'

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('index')
@csrf_protect
@csrf_exempt
def login_request(request):
    if request.method=='POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user.is_generator  == True:
                if user is not None :
                    login(request,user)
                    return render(request, '../templates/generator.html')
                else:
                    messages.error(request,"Invalid username or password")
            if user.is_handler  == True:
                if user is not None :
                    login(request,user)
                    return render(request, '../templates/handler.html')
                else:
                    messages.error(request,"Invalid username or password")
            
        else:
            messages.error(request,"Invalid username or password")
    return render(request, '../templates/login.html',
    context={'form':AuthenticationForm()})

def logout_view(request):
    logout(request)
    return redirect('/')