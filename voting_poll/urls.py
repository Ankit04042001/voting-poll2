
from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.index, name='index'),
    path('index/', views.index, name='index'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('vote/', views.vote, name='vote'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)