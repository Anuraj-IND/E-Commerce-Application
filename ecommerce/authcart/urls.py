from django.urls import path
from authcart import views

urlpatterns = [
    path('signup/',views.signup,name='signup'),
    # path('login/', views.login, name='signin'),
    # path('logout/', views.logout, name='logout'),
    path('login/', views.handlelogin, name='handlelogin'),
    path('logout/', views.handlelogout, name='handlelogout'),
]
