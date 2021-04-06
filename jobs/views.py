from django.shortcuts import render, redirect
from .models import Job
from django.contrib.auth import (
    authenticate,
    login as django_login,
    logout as django_logout,
)
from django.core.paginator import Paginator


# Create your views here.
def home(request):
    context = {
        "title": "Find your dream job with us",
    }
    return render(request, "home.html", context)


def jobs(request):
    jobs = Job.objects.all()
    paginator = Paginator(jobs, 30)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    available_jobs = len(jobs)
    context = {
        "title": "Jobs",
        "page_obj": page_obj,
        "available_jobs": available_jobs,
    }
    return render(request, "jobs.html", context)


def add_job(request):
    if not request.user.is_authenticated:
        return render(request, "401.html")
    if request.method == "POST":
        title = request.POST["title"]
        location = request.POST["location"]
        description = request.POST["description"]
        requirement = request.POST["requirement"]
        Job.objects.create(
            title=title,
            location=location,
            description=description,
            requirement=requirement,
        )
        return redirect("jobs")
    context = {
        "title": "Add Job",
    }
    return render(request, "add_job.html", context)


def login(request):
    context = {"title": "Login"}
    if request.user.is_authenticated:
        return redirect("jobs")
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            django_login(request, user)
            return redirect("jobs")
    return render(request, "login.html", context)


def logout(request):
    django_logout(request)
    return redirect("jobs")
