from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from .models import Coldstorage,Requests
# from twilio.rest import Client
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from django.views import View
from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.core.mail import send_mail
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
    fields=['farmer_name','email','phone','crop_type','duration','address','quantity','storage_name']
    success_url='/'


class UserRequestView(LoginRequiredMixin,ListView):
    def dispatch(self, *args, **kwargs):
        return super(UserRequestView, self).dispatch(*args, **kwargs)

    def get_queryset(self):
        email=self.request.user.email
        cold=Coldstorage.objects.get(email=email)
        req=Requests.objects.filter(storage_name=cold.name)
        model=req
        return model
    context_object_name = 'request_list'
    template_name = 'coldstorage/requests.html'
class UserRequestDetailView(DetailView):
    def get_queryset(self):
        email=self.request.user.email
        cold=Coldstorage.objects.get(email=email)
        req=Requests.objects.filter(storage_name=cold.name)
        model=req
        return model


class AcceptView(View):
    def get(self, request, pk, *args, **kwargs):
  	    # email=request.user.email
        # cold=Coldstorage.objects.get(email=email)
        # req=Requests.objects.filter(storage_name=cold.name)
        # model=req
        # email=model.email
        entry = Requests.objects.get(pk=pk)
        Requests.objects.get(pk=pk).delete()
        send_mail('Accepted',
        'Your Request has been accepted by owner.',
        'harshaattuluri1729@gmail.com',
        [entry.email])
        success_url='coldstorage-home'
        return render(request,"coldstorage/status.html",{})

class RejectView(View):
    def get(self, request, pk, *args, **kwargs):
  	    # email=request.user.email
        # cold=Coldstorage.objects.get(email=email)
        # req=Requests.objects.filter(storage_name=cold.name)
        # model=req
        # email=model.email
        entry = Requests.objects.get(pk=pk)
        Requests.objects.get(pk=pk).delete()
        send_mail('SORRY,Rejected',
        'Sorry,Your Request has been rejected by owner.Try requesting other',
        'harshaattuluri1729@gmail.com',
        [entry.email])
        success_url='coldstorage-home'
        return render(request,"coldstorage/rejectstatus.html",{})


             
# def UserRequestRejectView(request):
#     def save(self,*args,**kwargs):
#         account_sid = 'ACc3568779151ff2b8e243bd6504779c46'
#         auth_token = '86443c454bb9e2b67d3ea0f7eb83e5ed'
#         client = Client(account_sid, auth_token)

#         message = client.messages.create(
#                               body='sorry owner rejected your request',
#                               from_='+12566855742',
#                               to='+919182375839'
#                           )

#         print(message.sid)
#         return super.save(*args,**kwargs)
#     return render(request)




    # context={
    #     'requests':req,
    # }
   
    # return render(request,'coldstorage/requests.html',context)


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



# def add_request(request, slug):
#     item = get_object_or_404(Requests, slug=slug)
#     order_item, created = OrderItem.objects.get_or_create(
#         item=item,
#         ordered=False
#     )
#     order_qs = Order.objects.filter(user=request.user, ordered=False)
#     # if order_qs.exists():
#     #     order = order_qs[0]
#     #     # check if the order item is in the order
#     #     if order.items.filter(item__slug=item.slug).exists():
#     #         order_item.quantity += 1
#     #         order_item.save()
#     #         messages.info(request, "This item quantity was updated.")
#     #         return redirect("core:order-summary")
#     #     else:
#     #         order.items.add(order_item)
#     #         messages.info(request, "This item was added to your cart.")
#     #         return redirect("core:order-summary")
#     else:
        
#         order = Order.objects.create(
#             user=request.user, ordered_date=ordered_date)
#         order.items.add(order_item)
#         messages.info(request, "This item was added to your cart.")
#         return redirect("")
# def request_to(request):
#     context={
#         'storages':Requests.objects.values_list(request.user.email)
#     }
#     return render(request, 'coldstorage/requests.html',context)