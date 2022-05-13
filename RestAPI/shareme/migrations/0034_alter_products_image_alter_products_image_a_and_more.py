# Generated by Django 4.0.4 on 2022-05-04 19:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shareme', '0033_alter_products_image_alter_products_image_a_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='image',
            field=models.ImageField(blank=True, default='products/def_post.jpeg', null=True, upload_to='products'),
        ),
        migrations.AlterField(
            model_name='products',
            name='image_a',
            field=models.ImageField(blank=True, default='products/def_post.jpeg', null=True, upload_to='products'),
        ),
        migrations.AlterField(
            model_name='products',
            name='image_b',
            field=models.ImageField(blank=True, default='products/def_post.jpeg', null=True, upload_to='products'),
        ),
        migrations.AlterField(
            model_name='products',
            name='image_c',
            field=models.ImageField(blank=True, default='products/def_post.jpeg', null=True, upload_to='products'),
        ),
        migrations.AlterField(
            model_name='products',
            name='review_likes',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='products',
            name='stars',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='products',
            name='total_reviews',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='products',
            name='units_sold',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]