from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from .models import Coldstorage,Requests
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
# Create your views here.



def home(request):
    context={
        'storages':Coldstorage.objects.all()
    }
    return render(request, 'coldstorage/home.html',context)

class StorageListView(ListView):
    model=Coldstorage
    template_name='coldstorage/home.html'     
    context_object_name='storages'
    ordering=['-date_modified']
class StorageDetailView(DetailView):
    model=Coldstorage

class StorageCreateView(LoginRequiredMixin,CreateView):
    model=Coldstorage
    fields=['name','description','phone','total_storage','storage_left','email']


    def form_valid(self,form):
        form.instance.author=self.request.user
        return super().form_valid(form) 
class StorageUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model=Coldstorage
    fields=['description','storage_left','email']
    def form_valid(self,form):
        form.instance.author=self.request.user.email
        return super().form_valid(form)
    def test_func(self):
        storage=self.get_object()
        if(self.request.user.email==storage.email):
            return True
        return False
class StorageDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model=Coldstorage
    success_url='/'
    def test_func(self):
        storage=self.get_object()
        if(self.request.user.email==storage.email):
            return True
        return False

class StorageRequestView(CreateView):
    model=Requests
    # storage=Coldstorage.objects.get(pk=id)
    # model.email=storage.email
    fields=['farmer_name','phone','crop_type','duration','address','quantity']
    success_url='/'

def about(request):
    return render(request, 'coldstorage/about.html', {'title': 'About'})
# class UsersView(TemplateView):
#     template_name='users.html'
# class UsersView(TemplateView):
#     template_name = 'users.html'

#     def get_context_data(self, **kwargs):
#         context = super(UsersView, self).get_context_data(**kwargs)
#         context['object_list'] = UserList.objects.all()
#         return context