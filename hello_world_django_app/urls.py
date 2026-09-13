from django.contrib import admin
from django.urls import path
from hello_world_django_app.views import home, hello_world, health_check

urlpatterns = [
    path('', home),
    path('admin/', admin.site.urls),
    path('hello/', hello_world),
    path('health/', health_check),
]
