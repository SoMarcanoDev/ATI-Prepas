from django.urls import path
from .views import LoginView, LogoutView, vista_protegida

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('protegida/', vista_protegida, name='protegida')
]
