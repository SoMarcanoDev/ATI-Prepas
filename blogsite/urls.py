from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_blogs, name='lista_blogs'),
    path('post/<int:blog_id>/', views.detalle_blog, name='detalle_blog'),
]