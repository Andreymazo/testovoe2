# Generated by Django 4.2 on 2023-04-13 08:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0004_alter_menuitem_menu'),
    ]

    operations = [
        migrations.RenameField(
            model_name='menuitem',
            old_name='menu',
            new_name='parent',
        ),
    ]