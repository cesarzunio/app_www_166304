from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path('osoby/', views.osoba_list, name='osoba-list'),
    path('osoby/<int:pk>/', views.osoba_detail, name='osoba-detail'),
    path('stanowiska/', views.stanowisko_list, name='stanowisko-list'),
    path('stanowiska/<int:pk>/', views.stanowisko_detail, name='stanowisko-detail'),
    path('persons/', views.person_list),
    path('persons/<int:pk>/', views.person_detail),
    path('persons/<int:pk>/update/', views.person_update, name='person-update'),
    path('persons/<int:pk>/delete/', views.person_delete, name='person-delete'),
    path('stanowisko/<int:id>/members/', views.stanowisko_members, name='stanowisko-members'),
]