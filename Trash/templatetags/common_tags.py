from django import template
from menu.models import Menu
register = template.Library()


@register.inclusion_tag('../templatetags/../../menu/Trash/menu.html', takes_context=True)
def show_menu(context):
    menu_items = Menu.objects.filter(level=1)
    return {
        "menu_items": menu_items,
    }