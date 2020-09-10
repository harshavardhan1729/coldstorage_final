from django.urls import path
from . import views

from . views import StorageCreateView,StorageDetailView,StorageListView,StorageDeleteView,StorageUpdateView,StorageRequestView
urlpatterns = [
    path('', StorageListView.as_view(),name='coldstorage-home'),
    path('about/',views.about,name='coldstorage-about'),
    path('coldstorage/new/',StorageCreateView.as_view(),name="coldstorage-create"),
    path('coldstorage/<int:pk>/update',StorageUpdateView.as_view(),name="coldstorage-update"),
    path('coldstorage/<int:pk>/delete',StorageDeleteView.as_view(),name="coldstorage-delete"),
    path('coldstorage/<int:pk>/request',StorageRequestView.as_view(),name="coldstorage-request"),
    path('coldstorage/<int:pk>/',StorageDetailView.as_view(),name="coldstorage-detail"),
]