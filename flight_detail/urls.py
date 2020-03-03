from django.urls import path

from flight_detail import views

urlpatterns = [
    path('', views.Index.as_view(), name='index'),
    path('search/', views.Search.as_view(), name='search'),
]
