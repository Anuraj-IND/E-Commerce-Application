from django.urls import path
from auth import views

urlpatterns = [
    path('signup/',views.signup,name='signup'),
    path('signin/', views.signin, name='signin'),
    path('logout/', views.logout, name='logout'),
]
