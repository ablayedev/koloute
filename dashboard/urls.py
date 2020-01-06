from django.urls import path 
from dashboard import views
app_name="dashboard"
urlpatterns = [
    path('', views.index,name="index"),
    path('rapport/', views.rapport,name="rapport"),
  
]
