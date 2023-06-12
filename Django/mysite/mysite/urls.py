from django.contrib import admin
from django.urls import include, path
import authentication.views

urlpatterns = [
    path("polls/", include("polls.urls")),
    path("admin/", admin.site.urls),
    path('', authentication.views.login_page, name='login'),
]