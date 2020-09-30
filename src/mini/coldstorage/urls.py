from django.urls import path
from . import views

from . views import StorageCreateView,StorageDetailView,StorageListView,StorageDeleteView,StorageUpdateView,StorageRequestView,UserRequestView,UserRequestDetailView,AcceptView,RejectView #,UserRequestRejectView #,StorageConfirmView
# app_name='coldstorage'
urlpatterns = [
    path('', StorageListView.as_view(),name='coldstorage-home'),
    path('about/',views.about,name='coldstorage-about'),
    path('coldstorage/requests/',UserRequestView.as_view(),name="user-requests"),
    path('coldstorage/requests/<int:pk>/',UserRequestDetailView.as_view(),name="user-requests-detail"),
    # path('coldstorage/requests/<int:pk>/reject',views.UserRequestRejectView,name="user-requests-reject"),
    path('coldstorage/new/',StorageCreateView.as_view(),name="coldstorage-create"),
    path('coldstorage/<int:pk>/update',StorageUpdateView.as_view(),name="coldstorage-update"),
    path('coldstorage/<int:pk>/delete',StorageDeleteView.as_view(),name="coldstorage-delete"),
    path('coldstorage/<int:pk>/request',StorageRequestView.as_view(),name="coldstorage-request"),
    path('coldstorage/<int:pk>/',StorageDetailView.as_view(),name="coldstorage-detail"),
    path('coldstorage/requests/<int:pk>/accept',AcceptView.as_view(),name="user-requests-accept"),
    path('coldstorage/requests/<int:pk>/reject',RejectView.as_view(),name="user-requests-reject"),
    
  
    
]