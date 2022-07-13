from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('cards/', views.cards_index, name='index'),
    path('cards/<int:card_id>/', views.cards_detail, name='detail'),
    path('cards/create/', views.CardCreate.as_view(), name='cards_create'),
    path('cards/<int:pk>/update/', views.CardUpdate.as_view(), name='cards_update'),
    path('cards/<int:pk>/delete/', views.CardDelete.as_view(), name='cards_delete'),
    path('cards/<int:card_id>/add_feeding/', views.add_feeding, name='add_feeding'),
    path('resources/', views.ResourceList.as_view(), name='resources_index'),
    path('resources/<int:pk>/', views.ResourceDetail.as_view(), name='resources_detail'),
    path('resources/create/', views.ResourceCreate.as_view(), name='resources_create'),
    path('resources/<int:pk>/update/', views.ResourceUpdate.as_view(), name='resources_update'),
    path('resources/<int:pk>/delete/', views.ResourceDelete.as_view(), name='resources_delete'),
    path('cards/<int:card_id>/assoc_resource/<int:resource_id>/', views.assoc_resource, name='assoc_resource'),
    path('cards/<int:card_id>/assoc_resource/<int:resource_id>/delete/', views.assoc_resource_delete, name='assoc_resource_delete'),
    # new users
    path('accounts/signup/', views.signup, name='signup'),
  
]

