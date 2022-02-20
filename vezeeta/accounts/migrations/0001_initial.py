# Generated by Django 3.1.4 on 2021-01-02 19:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, null=True, verbose_name='name : ')),
                ('subtitle', models.CharField(blank=True, max_length=100, null=True, verbose_name='نبذه عنك  : ')),
                ('address', models.CharField(blank=True, max_length=100, null=True, verbose_name='المحافظه :')),
                ('address_detail', models.CharField(blank=True, max_length=100, null=True, verbose_name='العنوان بالتفصيل : ')),
                ('number_phone', models.IntegerField(blank=True, null=True, verbose_name='الهاتف : ')),
                ('working_hours', models.IntegerField(blank=True, null=True, verbose_name='عدد ساعات العمل :')),
                ('wating_time', models.IntegerField(blank=True, null=True, verbose_name='مده النتظار : ')),
                ('doctor', models.CharField(blank=True, max_length=100, null=True, verbose_name='دكتور ؟ ')),
                ('who_i', models.TextField(blank=True, max_length=250, null=True, verbose_name='Who Iam : ')),
                ('price', models.IntegerField(blank=True, null=True, verbose_name='Price : ')),
                ('facebook', models.CharField(blank=True, max_length=100, null=True)),
                ('twitter', models.CharField(blank=True, max_length=100, null=True)),
                ('google', models.CharField(blank=True, max_length=100, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='profile', verbose_name='Image : ')),
                ('specialist_doctor', models.CharField(blank=True, max_length=100, null=True, verbose_name='التخصص : ')),
                ('slug', models.SlugField(blank=True, null=True, verbose_name='slug')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name=' user ')),
            ],
            options={
                'verbose_name': 'Profile',
                'verbose_name_plural': 'Profiles',
            },
        ),
    ]