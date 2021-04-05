from django.shortcuts import render

# Create your views here.
def home(request):
    context = {"title": "Welcome to Golden Arrow official job listing"}
    return render(request, "home.html", context)
