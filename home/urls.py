from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name = 'lohi'),
    path('lohi/',views.lohi,name = 'lohi2')
]