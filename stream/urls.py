from . import views
from django.contrib.auth import views as auth_views
from . views import (
    GeneralVideoListView, 
    VideoCreateView
)
from django.urls import path 


app_name = "stream"

urlpatterns = [
    path('',GeneralVideoListView.as_view(), name="video-list"),   
    path('video/new/',VideoCreateView.as_view(), name="video-create"),
    path('search',views.search,name="search"),
    # path('login', auth_views.LoginView.as_view(template_name='admin/login/'), name="login"),
    # path('logout',auth_views.LogoutView.as_view(template_name='admin/logout/'), name="logout"),
     # Login and Logout
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]


