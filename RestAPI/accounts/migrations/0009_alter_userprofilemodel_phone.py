# Generated by Django 3.2.4 on 2022-03-27 09:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0008_alter_userprofilemodel_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofilemodel',
            name='phone',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
    ]