# Generated by Django 3.1.4 on 2021-01-03 13:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0010_merge_20210103_1520'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='join_new',
            field=models.DateTimeField(blank=True, null=True, verbose_name='وقت الانضمام :'),
        ),
    ]