from django.urls import path 
from register import views
from rest_framework import routers
from register import api

app_name="register"

route=routers.DefaultRouter()
route.register('api/station',api.StationViewset)
route.register('api/location',api.LocationViewset)
urlpatterns = route.urls
urlpatterns+= [
    path('accueil/',views.accueil,name="accueil"),
    path('deconect',views.deconect,name="logout"),
    path('options/',views.option,name="option"),
    path('location/',views.locations,name="location"),
    path('update_box/',views.update_box,name="update_box"),
]
