from django.contrib import admin
from django.urls import path,include

# modelo = path('prefixo_da_URL/', arquivo de URL)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('catalogo.urls')),
    path('usuarios/', include('usuarios.urls')),
]
