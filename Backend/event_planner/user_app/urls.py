from django.urls import path
from knox.views import LogoutView, LogoutAllView
from .views import login_view, register_view ,get_user_data, Event_view

urlpatterns = [
    path('login/', login_view, name='login view'),
    path('register/', register_view, name='login view'),
    path('user/', get_user_data, name="user data"),
    path('logout/', LogoutView.as_view(), name="logout view"),
    path('logallout/', LogoutAllView.as_view(), name="logout all view"),
    path('Event/', Event.as_view())

]
