from django.urls import path
from account.views import  UserRegistrationView,UserLoginview
urlpatterns = [
    path('register/', UserRegistrationView.as_view(),name='register'),
    path('login/', UserLoginview.as_view(),name='login'),
  

]