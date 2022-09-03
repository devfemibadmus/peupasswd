from django.http import HttpResponse
from django.shortcuts import render
from .pencryptor import pencryptor

# Create your views here.
# HANDLING LOST URLS LOLZ...
def home(request):
    return render(request, "peupasswd.html")

def peupasswd(request):
    if request.method == "POST":
      master_passwd = request.POST["password"]
      service_name = request.POST["service"]
      pswd_length = request.POST["plength"]
      peupasswd = pencryptor(master_passwd, service_name, pswd_length)
      peupasswd = peupasswd
    else:
      peupasswd = ""
    return HttpResponse(peupasswd)
