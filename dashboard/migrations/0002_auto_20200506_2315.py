# Generated by Django 2.2.7 on 2020-05-06 18:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='page',
            name='page_user',
        ),
        migrations.RemoveField(
            model_name='post',
            name='post_page',
        ),
        migrations.DeleteModel(
            name='Comment',
        ),
        migrations.DeleteModel(
            name='Page',
        ),
        migrations.DeleteModel(
            name='Post',
        ),
    ]