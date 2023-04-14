import mptt
from django.db import models
# from mptt.models import MPTTModel, TreeForeignKey
from django.db import models
from django.urls import reverse
from mptt.models import MPTTModel, TreeForeignKey


class Menu(MPTTModel):
    name = models.CharField('Название', max_length=100)
    url = models.CharField('Ссылка', max_length=255)
    position = models.PositiveIntegerField('Позиция', default=1)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, db_index=True, related_name='children')
    slug = models.SlugField()
    # def __str__(self):
    #     full_path = [self.name]  ### Cherez slash vidim podkategorii menu_item
    #     k = self.parent
    #     while k is not None:
    #         full_path.append(k.name)
    #         k = k.parent
    #     return ' / '.join(full_path[::-1])  # return str(self.name)

    class MPTTMeta:
        order_insertion_by = ['name']
        verbose_name = 'Меню'
        verbose_name_plural = 'Меню'

    def get_absolute_url(self):
        return reverse('menu_items', args=[str(self.slug)])##{{node.get_absolute_url}}

    class Meta:

        verbose_name = 'Меню'
        verbose_name_plural = 'Меню'


# mptt.register(Menu, order_insertion_by=['name'])
# {% for category in categories %}
#             {{ category }}
#             {% for article in category.article_set.all %}
#                 {{ article }}
#             {% endfor %}
#         {% endfor %}

class MenuItem(models.Model):
    name = models.CharField(max_length=100, unique=True)
    url = models.CharField('Ссылка', max_length=255)
    position = models.PositiveIntegerField('Позиция', default=1)
    # parent = TreeForeignKey('menu.Menu', on_delete=models.CASCADE, null=True, blank=True, related_name='children')
    parent = TreeForeignKey(Menu, on_delete=models.CASCADE, null=True, blank=True, related_name='sss')

    def get_absolute_url(self):
        print(';;;;;;;;;;;;;;;;;')
        return reverse('detail', args=[str(self.url)])

    class Meta:
        verbose_name = 'Пункт меню'
        verbose_name_plural = 'Пункты меню'

    def __str__(self):
        return str(self.name)
#################
# class Category(MPTTModel):
#     title = models.CharField(max_length=50, unique=True, verbose_name='Название')
#     parent = TreeForeignKey('self', on_delete=models.PROTECT, null=True, blank=True, related_name='children',
#                             db_index=True, verbose_name='Родительская категория')
#     slug = models.SlugField()
#
#     class MPTTMeta:
#         order_insertion_by = ['title']
#
#     class Meta:
#         unique_together = [['parent', 'slug']]
#         verbose_name = 'Категория'
#         verbose_name_plural = 'Категории'
#
#     def get_absolute_url(self):
#         return reverse('post-by-category', args=[str(self.slug)])
#
#     def __str__(self):
#         return self.title
############################################################
