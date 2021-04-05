from django.urls import path
from .views import home, jobs, add_job, login, logout


urlpatterns = [
    path("", home, name="home"),
    path("jobs/", jobs, name="jobs"),
    path("add_job/", add_job, name="add_job"),
    path("login/", login, name="login"),
    path("logout/", logout, name="logout"),
]
