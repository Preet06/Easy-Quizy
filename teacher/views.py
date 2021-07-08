from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.views.generic.edit import CreateView
from django.shortcuts import render
from django.http import HttpResponse
from .models import test_create
from django.contrib.auth import logout
from django.views.generic import CreateView
from django.contrib.auth.forms import UserCreationForm


def home_page(request):
    return render(request, 'home.html')



class SignUpView(CreateView):
     form_class =  UserCreationForm
     success_url = reverse_lazy('login')
     template_name = 'registration/signup.html'


def home(request):
   if request.user.is_anonymous == True:
      return render('/login')
   else:
      return render(request,"index.html",{'nav':request.user})

def home2(request):
      return render(request,'home2.html')

class BlogCreateView(CreateView): # new
      model = test_create
      template_name = 'sett.html'
      fields = ['test_code', 'question', 'op1','op2','op3','op4','ans']