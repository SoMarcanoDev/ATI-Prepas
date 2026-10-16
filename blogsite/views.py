from django.shortcuts import render, get_object_or_404
from .models import Blog

# Create your views here.
def lista_blogs(request):
    blogs = Blog.objects.all().order_by('-fecha_publicacion')
    return render(request, 'lista.html', {'blogs': blogs})

def detalle_blog(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'detalle.html', {'blog': blog})