# Generated by Django 4.0.4 on 2022-05-11 08:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shareme', '0039_products_activityscore'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='priority',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]