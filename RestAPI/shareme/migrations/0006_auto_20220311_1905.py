# Generated by Django 3.2.4 on 2022-03-11 19:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shareme', '0005_auto_20220311_1226'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='username',
            field=models.CharField(blank=True, max_length=60, null=True),
        ),
        migrations.AlterField(
            model_name='comment',
            name='title',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]