from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('', include('biblioteca.urls')),
    path('auth/', include('usuarios.urls')),   #adicione essa linha aqui
    path('admin/', admin.site.urls),
]