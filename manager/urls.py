from . import views
from django.urls import path

app_name = 'manager'
urlpatterns = [
    path('', views.LastEntryList.as_view(), name='index'),
    path('wszystkie/', views.EntryList.as_view(), name='all-entries'),
    path('najpopularniejsze/', views.PopularEntryList.as_view(), name='popular-entries'),
    path('dodaj-haslo/', views.EntryCreate.as_view(),  name='entry-create'),
    path('<slug:slug>/', views.EntryDetail.as_view(),  name='entry-detail'),
]