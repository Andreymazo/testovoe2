import generics as generics
from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView

from menu.models import Menu, MenuItem


def index(request):
    template = "menu.html"
    # header = 'Главная страница'
    # for i in Menu.objects.all():
    #     print(MenuItem.objects.filter(parent_id=i.pk))
    # print(MenuItem.objects.filter(parent_id=Menu.objects.root_node))#################################
    context = {
        # 'header': header
        'menu_items': Menu.objects.all(),
        'menu_item_item': MenuItem.objects.all(),
    }

    return render(request, template, context)


def show_menu_items(request, id):
    menu_items = MenuItem.objects.filter(parent_id=id)
    return HttpResponse(menu_items)
    # render(request, "menu.html", {'menu_items': Menu.objects.all()})


class MenuList(ListView):
    model = Menu
    template_name = 'menu.html'
   # MenuItem.objects.filter(parent_id=Menu.objects.get(pk=1).get_descendants(include_self=True))


class MenuItemList(ListView):
    context_object_name = 'items'
    template_name = 'menu_item.html'
    model = MenuItem

    def get_queryset(self, **kwargs):
        print(self.kwargs['url'])  # kwargs['menu']
        # if isinstance(self.model, Menu):

        self.parent = Menu.objects.all().get(url=self.kwargs['url'])  # id=delf.menu_id
        queryset = MenuItem.objects.filter(parent=self.parent)
        # self.parent = MenuItem.objects.all().get(url=self.kwargs['url'])  # id=delf.menu_id
        # queryset = MenuItem.objects.filter(parent=self.parent)

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['name'] = self.parent
        return context


class MenuItemCreate(CreateView):
    model = MenuItem
    success_url = reverse_lazy('menu: detail')

class MenuItemUpdate(UpdateView):
    model = MenuItem
    template = 'menu_item.html'

class MenuItemDetail(DetailView):
    print('+++++++=======================++++')
    model = MenuItem
    template = 'menu_item_detail.html'

