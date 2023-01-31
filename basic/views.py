from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Publication
from django.shortcuts import get_object_or_404
from django.views import generic
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required

def index(request):
    publication_list = Publication.objects.all()
    if not request.user.is_authenticated:
        return render(request, 'basic/error.html')
    else:
        return render(request, "basic/index.html", {
            "users_list": publication_list
        })

# class IndexListView(generic.ListView):
#     template_name = "basic/index.html"
#     context_object_name = "users_list"

#     def get_queryset(self):
#         users_list = Publication.objects.all()
#         return users_list

#@login_required(login_url='home/error/')
def presentation(request):
    return render(request, "basic/presentation.html")


def signUp(request):
    return render(request, "basic/signup.html")


def response(request):  
    select_username = request.POST["username"]
    select_password = request.POST["password"]
    select_email = request.POST["email"]
    u = User.objects.create_user(username=select_username, password=select_password, email=select_email)
    u.save()
    return HttpResponse("correcto")


def error_401(request):
    return HttpResponse("NO ESTAS AUTORIZADO A INGRESAR")


def change_password(request):
    pass


def user_login(request):
    return render(request, "basic/login.html")


def response_login(request):
    user = authenticate(username=request.POST["username"], password=request.POST["password"])
    if user is not None:
        login(request, user)
        return redirect("/home/")
    else:
        #return redirect("/home/error-401")
        return HttpResponse(status=401)


def profile(request):
    if not request.user.is_authenticated:
        return HttpResponse("incorrecto")
    #u = get_object_or_404(User, pk=user_id)
    return render(request, "basic/profile.html", {
        "user": request.user
    })


