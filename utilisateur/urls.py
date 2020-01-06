from django.urls import path 
from utilisateur import views
app_name="utilisateur"
urlpatterns = [
    path('', views.home,name="home"),
    #path('admin-tolbi', views.admin,name="admin"),
    path('logout/',views.deconect,name="logout")
  
]
