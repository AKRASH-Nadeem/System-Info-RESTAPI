from django.urls import path
from authapi.views import UserLoginView

urlpatterns = [
    path('login/', UserLoginView.as_view(), name='login_api'),
]