from . import views
from django.urls import path

urlpatterns = [
    path('', views.EntryList.as_view(), name='home'),
    path('<slug:slug>/', views.EntryDetail.as_view(),  name='entry_detail'),
]