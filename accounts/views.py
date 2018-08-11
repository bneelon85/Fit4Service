from django.shortcuts import render
from accounts.forms import HomeForm
from django.views.generic import TemplateView

# Create your views here.
def home(request):
    numbers = [1,2,3,4,5]
    name = 'Julian Se'

    args = {'my_name' : name, 'numbers': numbers, 'form':HomeForm}
    return render(request, 'accounts/home.html', args)
