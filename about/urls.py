from django.urls import path
import views


app_name = 'about'

urlpatterns[
    path('', views.about, name='about'),
]