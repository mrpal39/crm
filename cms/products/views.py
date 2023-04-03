# Create your views here.
from django.core.management import call_command
from django.shortcuts import render


def get_product_name_modile(request):

    if request.method == "GET":
        # data=request.POST['search']
        # c = RequestContext(request.POST, {
        response = call_command("amzone_product")

        print(response)

    return render(request, "base.html")
