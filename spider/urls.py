from django.urls import path
from .import views

urlpatterns = [
    path('', views.index, name='landing'),
    path('home/', views.home, name='home'),
    path('headphones/<str:brand>', views.headphones, name='headphones'),
    path('smart-watches/<str:brand>', views.smart_watches, name='smart_watches'),
    path('mice/<str:brand>', views.mice, name='mice'),
    path('keyboards/<str:brand>', views.keyboards, name='keyboards'),
    path('spectacles/<str:brand>', views.spectacles, name='spectacles')
]
