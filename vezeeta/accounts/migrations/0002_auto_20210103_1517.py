# Generated by Django 3.1.4 on 2021-01-03 13:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='join_new',
            field=models.DateTimeField(default=1, verbose_name='وقت الانضمام :'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='profile',
            name='type_of_person',
            field=models.CharField(choices=[('M', 'Male'), ('F', 'Female')], default=1, max_length=50, verbose_name='النوع : '),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='profile',
            name='doctor',
            field=models.CharField(blank=True, choices=[('جلديه', 'جلديه'), ('اسنان', 'اسنان'), ('نفسي', 'نفسي'), ('اطفال حديثي الولاده', 'اطفال حديثي الولاده'), ('مخ واعصاب', 'مخ واعصاب'), ('عظام', 'عظام'), ('نسا وتوليد', 'نساوتوليد'), ('انف واذن وحنجره', 'انف واذن وحنجره'), ('قلب واوعيه دمويه', 'قلب واوعيه دمويه'), ('امراض دم', 'امراض دم'), ('اورام', 'اورام'), ('بطانه', 'بطانه'), ('تخسيس و تغذيه', 'تخسيس و تغذيه'), ('جراحه اطفال', 'جراحه اطفال'), ('جراحه اورام', 'جراحه اورام'), ('جراحه اوعيه دمويه', 'جراحه اوعيه دمويه'), ('جراحه تجميل', 'جراحه تجميل'), ('جراحه سمنه ومناظير', 'جراحه سمنه ومناظير')], max_length=100, null=True, verbose_name='دكتور ؟ '),
        ),
        migrations.AlterField(
            model_name='profile',
            name='specialist_doctor',
            field=models.CharField(blank=True, choices=[('جلديه', 'جلديه'), ('اسنان', 'اسنان'), ('نفسي', 'نفسي'), ('اطفال حديثي الولاده', 'اطفال حديثي الولاده'), ('مخ واعصاب', 'مخ واعصاب'), ('عظام', 'عظام'), ('نسا وتوليد', 'نساوتوليد'), ('انف واذن وحنجره', 'انف واذن وحنجره'), ('قلب واوعيه دمويه', 'قلب واوعيه دمويه'), ('امراض دم', 'امراض دم'), ('اورام', 'اورام'), ('بطانه', 'بطانه'), ('تخسيس و تغذيه', 'تخسيس و تغذيه'), ('جراحه اطفال', 'جراحه اطفال'), ('جراحه اورام', 'جراحه اورام'), ('جراحه اوعيه دمويه', 'جراحه اوعيه دمويه'), ('جراحه تجميل', 'جراحه تجميل'), ('جراحه سمنه ومناظير', 'جراحه سمنه ومناظير')], max_length=100, null=True, verbose_name='التخصص : '),
        ),
    ]
