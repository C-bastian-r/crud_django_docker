from django.urls import path
from . import views
urlpatterns = [
    path("/pito", views.pitos, name="pitos")
]