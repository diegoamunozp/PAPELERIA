"""
URL configuration for PAPELERIA project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.Login,name = 'Login'),
    path('Inventario/',views.Inventario,name = 'Inventario'),

    path('Caja/',views.Caja,name = 'Caja'),

    path('Personal/',views.Personal,name = 'Personal'),
    path('Personal/Administrar_Personal/',views.Administrar_Personal,name = 'Administrar_Personal'),
    path('Personal/Consultar_Personal/',views.Consultar_Personal,name = 'Consultar_Personal'),

    path('Proveedores/',views.Proveedores,name = 'Proveedores'),
    path('Proveedores/Modificar_Proveedores/',views.Modificar_Proveedores,name = 'Modificar_Proveedores'),
    path('Proveedores/Devolucion_Proveedores/',views.Devolucion_Proveedores,name = 'Devolucion_Proveedores'),

    path('ModulosIndex/',views.ModulosIndex,name = 'ModulosIndex'),

    path('Menu_Principal/',views.Menu_Principal,name = 'Menu_Principal'),

    path('Ayuda/',views.Ayuda,name = 'Ayuda')]
