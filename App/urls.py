from . import views
from django.urls import path

urlpatterns = [
    path('',views.HomePage,name="HomePage"),
    path('result/',views.Sum,name="Sum"),
]