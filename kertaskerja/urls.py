from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('kertaskerja/daftarsasaran', views.daftarsasaran, name='daftarsasaran'),
    path('kertaskerja/formdaftarsasaran', views.formdaftarsasaran, name='formdaftarsasaran'),
]