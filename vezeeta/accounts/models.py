from django.db import models
from django.contrib.auth.models import User
from django.db.models.base import Model
from django.db.models.fields import CharField, SlugField, TextField
from django.db.models.fields.related import OneToOneField
from django.utils.translation import ugettext_lazy as _
from django.db.models.signals import post_save
from django.db import migrations
from PIL import Image
from django.db.models.signals import post_save
from django.utils.text import slugify


# Create your models here.
TYPE_OF_PERSON=(
    ('M' , 'Male'),
    ('F', 'Female'),
)
class Profile(models.Model):

    DOCTOR_IN = ( 
    ("جلديه", "جلديه"), 
    ("اسنان", "اسنان"), 
    ("نفسي", "نفسي"), 
    ("اطفال حديثي الولاده", "اطفال حديثي الولاده"), 
    ("مخ واعصاب", "مخ واعصاب"), 
    ("عظام", "عظام"), 
    ("نسا وتوليد", "نساوتوليد"), 
    ("انف واذن وحنجره", "انف واذن وحنجره"), 
    ("قلب واوعيه دمويه", "قلب واوعيه دمويه"), 
    ("امراض دم", "امراض دم"), 
    ("اورام", "اورام"), 
    ("بطانه", "بطانه"), 
    ("تخسيس و تغذيه", "تخسيس و تغذيه"), 
    ("جراحه اطفال", "جراحه اطفال"), 
    ("جراحه اورام", "جراحه اورام"), 
    ("جراحه اوعيه دمويه", "جراحه اوعيه دمويه"),
    ("جراحه تجميل", "جراحه تجميل"),
    ("جراحه سمنه ومناظير", "جراحه سمنه ومناظير"),
) 


    user              =models.OneToOneField(User, verbose_name=_(" user "),on_delete=models.CASCADE)
    name              =models.CharField(("name : "),max_length=100,blank=True,null=True)
    subtitle          =models.CharField(("نبذه عنك  : ") , max_length=100,blank=True, null=True)
    address           =models.CharField(("المحافظه :"), max_length=100,blank=True, null=True)
    address_detail    =models.CharField(("العنوان بالتفصيل : "),max_length=100,blank=True, null=True)
    number_phone      =models.IntegerField(("الهاتف : "),blank=True, null=True)
    working_hours     =models.IntegerField(("عدد ساعات العمل :"),blank=True, null=True)
    wating_time       =models.IntegerField(("مده النتظار : "),blank=True, null=True)
    who_i             =models.TextField(("Who Iam : "), max_length=250,blank=True, null=True)
    price             =models.IntegerField(("Price : "),blank=True, null=True)
    facebook          =models.CharField(max_length=100,blank=True, null=True)
    twitter           =models.CharField(max_length=100,blank=True, null=True)
    google            =models.CharField(max_length=100,blank=True, null=True)
    join_new          =models.DateTimeField(("وقت الانضمام :"),auto_now_add=False,blank=True, null=True)
    type_of_person    =models.CharField(("النوع : "),choices=TYPE_OF_PERSON, max_length=50)
    doctor            =models.CharField(("دكتور ؟ "),choices=DOCTOR_IN, max_length=100,blank=True, null=True)
    image             =models.ImageField(("Image : "),upload_to='profile',blank=True,null=True)
    specialist_doctor =models.CharField(("التخصص : "),choices=DOCTOR_IN, max_length=100,blank=True, null=True)
    slug              =SlugField(("slug"),blank=True, null=True)
    
    

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug=slugify(self.user.username)
        super(Profile, self).save(*args, **kwargs)






    class Meta:
        verbose_name= _("Profile")
        verbose_name_plural = _("Profiles")


    def __str__(self):
        return '%s' %(self.user.username)


def create_profile(sender , **kwargs):
    if kwargs['created']:
        Profile.objects.create(user=kwargs['instance'])






    #     img = Image.open(self.image.path)

    #     if img.height > 300 or img.width > 300:
    #         output_size = (300,300)
    #         img.thumbnail(output_size)
    #         img.save(self.image.path)


post_save.connect(create_profile , sender=User)