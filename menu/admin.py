from mptt.admin import DraggableMPTTAdmin
from .models import Menu, MenuItem
from django.contrib import admin
from mptt.admin import MPTTModelAdmin
from menu.models import Menu, MenuItem

# from django.contrib import admin
# from mptt.admin import MPTTModelAdmin
# from menu.models import MenuItem
# from menu.models import Menu
#
#################################################Adminka i tak i tak pokazivaet#########################
class MenuMPTTModelAdmin(MPTTModelAdmin):
    mptt_level_indent = 20


admin.site.register(Menu, MenuMPTTModelAdmin )

admin.site.register(MenuItem, )

###########################################################################

# from django.contrib import admin
#
# from .models import Menu, MenuItem
#
#
# class MenuInline(admin.TabularInline):
#     model = MenuItem
#
#
# class MenuAdmin(admin.ModelAdmin):
#     inlines = [
#         MenuInline,
#     ]
#     """Отображение меню."""
#     list_display = (
#         'name',
#         'url'
#     )
#     search_fields = ('name', 'url')
#     list_filter = ('name', 'url')
#
#
# admin.site.register(Menu, MenuAdmin)
# admin.site.register(MenuItem)

#############################################################################
# class MenuAdmin(DraggableMPTTAdmin):
#     mptt_indent_field = "name"
#     list_display = ('tree_actions', 'indented_title',
#                     'related_products_count', 'related_products_cumulative_count')
#     list_display_links = ('indented_title',)
#
#     def get_queryset(self, request):
#         qs = super().get_queryset(request)
#
#         # Add cumulative product count
#         qs = Menu.objects.add_related_count(
#                 qs,
#                 MenuItem,
#                 'category',
#                 'products_cumulative_count',
#                 cumulative=True)
#
#         # Add non cumulative product count
#         qs = Menu.objects.add_related_count(qs,
#                  MenuItem,
#                  'categories',
#                  'products_count',
#                  cumulative=False)
#         return qs
#
#     def related_products_count(self, instance):
#         return instance.products_count
#     related_products_count.short_description = 'Related products (for this specific category)'
#
#     def related_products_cumulative_count(self, instance):
#         return instance.products_cumulative_count
#     related_products_cumulative_count.short_description = 'Related products (in tree)'
