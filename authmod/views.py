from django.shortcuts import render
from django.http import HttpResponse
def ld_login(request):
    return render(request,"login.html")
def login_check(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')

        print(email)
        print(password)

    return HttpResponse("Login submitted") 
def ld_register(request):
    return HttpResponse("Registration")
