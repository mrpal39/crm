from django.shortcuts import render
from django.shortcuts import redirect

# Create your views here.
from django.core.management import call_command
from crm.quotes.models  import Quotes
def qoutes(request):

    call_command('digitalocean_all_post')
    
    
    return redirect("/")