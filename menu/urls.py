from django.urls import path, re_path

from menu.views import show_menu_items, index, MenuItemList, MenuList, MenuItemDetail

# from .views import index, test_func

app_name = "menu"

urlpatterns = [
    path("", index, name="index"),
    # path("", MenuList.as_view(), name="index"),
    # path(r'^menu_items/<slug:slug>$', show_menu_items),

    path('<str:url>/', MenuItemList.as_view(), name='menu_items'),
    path('/detail/<int:pk>', MenuItemDetail.as_view(), name='detail'),
    re_path(r'^menu_items/<int:id>$', show_menu_items),#/<slug:slug>
]
