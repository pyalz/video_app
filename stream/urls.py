from . import views
from . views import (
    GeneralVideoListView, 
)
from django.urls import path 


app_name = "stream"

urlpatterns = [
    path('',GeneralVideoListView.as_view(), name="video-list"),   
    path('search',views.search,name="search"),
]


