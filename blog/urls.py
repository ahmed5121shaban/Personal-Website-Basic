from django.urls import path
import views


app_name = 'blog'

urlpatterns[
    path('', views.post, name='post'),
    path('<int:id>/', views.post_details, name='post_details'),
]