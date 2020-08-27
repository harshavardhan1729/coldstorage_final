from django.urls import path
from . import views

from . views import StorageCreateView,StorageDetailView,StorageListView
urlpatterns = [
    path('', StorageListView.as_view(),name='coldstorage-home'),
    path('about/',views.about,name='coldstorage-about'),
    path('coldstorage/new/',StorageCreateView.as_view(),name="coldstorage-create"),
    path('coldstorage/<int:pk>/',StorageDetailView.as_view(),name="coldstorage-detail"),
]