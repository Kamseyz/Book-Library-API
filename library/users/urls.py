from django.urls import path
from .views import RegisterView,LoginView
from rest_framework_simplejwt.views import TokenRefreshView
urlpatterns = [
    #registration urls
    path('register/', RegisterView.as_view(), name= 'register'),
    #login urls
    path('login/', LoginView.as_view(), name= 'login'),
   
   
]

