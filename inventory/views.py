from cmath import log
from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect

from .models import Item
from .forms import ItemForm, RegisterForm, LoginForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate

from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
import datetime


@login_required
def item_list(request):
    #分两个表

    #items = Item.objects.all()
    #return render(request, 'item_list.html', {'items': items})
    today =datetime.date.today()
    expired_items = Item.objects.filter(expiration_date__lt=today).order_by('expiration_date')
    non_expired_items = Item.objects.filter(expiration_date__gte=today).order_by('expiration_date')

    context = {
        'expired_items': expired_items,
        'non_expired_items': non_expired_items,
        'today':today
    }

    return render(request, 'item_list.html', context)

@login_required
def add_item(request):
    if request.method == 'POST':
        form = ItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('item_list')
    else:
        form = ItemForm()
    return render(request, 'add_item.html', {'form': form})


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('/')
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form})
    

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect('/')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})




class ItemUpdateView(UpdateView):
    model = Item
    fields = ['name', 'quantity', 'expiration_date', 'description']
    template_name = 'inventory/item_form.html'
    success_url = reverse_lazy('item_list')


class ItemDeleteView(DeleteView):
    model = Item
    template_name = 'inventory/item_confirm_delete.html'
    success_url = reverse_lazy('item_list')



class ItemListView(ListView):
    model = Item
    template_name = 'inventory/item_list.html'
    context_object_name = 'items'

    def get_queryset(self):
        queryset = super().get_queryset()
        sort = self.request.GET.get('sort')
        if sort:
            queryset = queryset.order_by(sort)
        return queryset


