# Generated by Django 4.0.4 on 2022-04-29 05:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shareme', '0028_remove_post_category_remove_post_likes_and_more'),
        ('sales', '0008_alter_orders_product'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Post',
        ),
    ]