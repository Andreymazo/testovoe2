# Generated by Django 4.2 on 2023-04-13 13:18

from django.db import migrations, models
import django.db.models.deletion
import mptt.fields


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0006_alter_menuitem_parent'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='menu',
            options={'ordering': [['tree_id', 'level']], 'verbose_name': 'Меню', 'verbose_name_plural': 'Меню'},
        ),
        migrations.AddField(
            model_name='menu',
            name='slug',
            field=models.SlugField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='menuitem',
            name='parent',
            field=mptt.fields.TreeForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='sss', to='menu.menu'),
        ),
    ]
