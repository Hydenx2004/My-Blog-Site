# Generated by Django 5.0.2 on 2024-04-12 18:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_remove_blog_date'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blog',
            old_name='Author_Id',
            new_name='Blog_Id',
        ),
    ]
