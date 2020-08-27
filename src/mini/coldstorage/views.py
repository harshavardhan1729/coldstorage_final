from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from .models import Coldstorage
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