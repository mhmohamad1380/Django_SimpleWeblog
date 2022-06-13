import os
import random

from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from django.db.models import Q
from django.http import request
from django.utils import timezone

from extensions.utils import jalali_datetime, jalali_date, jalali_date_without_day


class BlogManager(models.Manager):
    def get_active_blogs(self):
        return self.get_queryset().filter(active='1')

    def Search(self, query):
        lookup = (Q(title__icontains=query) |
                  Q(category__name__icontains=query))
        return self.get_queryset().filter(lookup, active='1').distinct()


def get_filename(basename):
    basename1 = os.path.basename(basename)
    name, ext = os.path.splitext(basename1)
    return name, ext


def image_path(instance, filename):
    new_name = random.randint(1, 1000000)
    name, ext = get_filename(filename)
    new_name1 = f'blog_{new_name}.{ext}'
    return f'blog/{new_name1}'


Choices = (
    (0, 'غیرفعال'),
    (1, 'فعال')
)


class Category(models.Model):
    name = models.CharField(max_length=50, null=True, blank=False, verbose_name='عنوان')

    class Meta:
        verbose_name_plural = 'دسته بندی ها'
        verbose_name = 'دسته بندی'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f"/blog/{self.name.replace(' ', '-')}"


class BlogContent(models.Model):
    title = models.CharField(blank=False, null=True, verbose_name='عنوان مطلب', max_length=120)
    description = models.TextField(blank=False, null=True, verbose_name='توضیحات')
    image = models.ImageField(null=True, blank=False, verbose_name='تصویر', upload_to=image_path)
    active = models.IntegerField(choices=Choices, verbose_name='فعال/غیر فعال')
    created_date = models.DateTimeField(default=timezone.now, verbose_name='تاریخ ایجاد')
    author = models.ForeignKey(User, verbose_name='نویسنده', on_delete=models.CASCADE)
    category = models.ManyToManyField(Category, blank=False,
                                      verbose_name='دسته بندی')
    object = BlogManager()

    class Meta:
        verbose_name = 'خبر'
        verbose_name_plural = 'خبرها'
        ordering = ['-created_date']

    def active_or_not(self):
        if self.active == 1:
            return True
        elif self.active == 0:
            return False

    active_or_not.boolean = True
    active_or_not.short_description = 'وضعیت خبر'

    def __str__(self):
        return self.title

    def datetime(self):
        return jalali_datetime(self.created_date)

    def date(self):
        return jalali_date(self.created_date)

    def datetime_without_day(self):
        return jalali_date_without_day(self.created_date)

    def get_absolute_url(self):
        return f'/blogs/{self.id}/{self.title.replace(" ", "-")}'


class Sidebar(models.Model):
    description = models.TextField(null=True, blank=False, verbose_name='توضیحات', max_length=500)

    class Meta:
        verbose_name = 'سایدبار'
        verbose_name_plural = 'سایدبار'

    def __str__(self):
        return self.description


Colors = (
    ('telegram', 'تلگرام'),
    ('twitter', 'توییتر'),
    ('instagram', 'اینستاگرام'),
    ('aparat', 'آپارات'),
    ('youtube', 'یوتیوب'),
)


class SocialMedias(models.Model):
    name = models.CharField(max_length=120, null=True, blank=False, verbose_name='نام')
    link = models.URLField(null=True, blank=False, verbose_name='لینک')
    color = models.CharField(choices=Colors, null=True, blank=False, verbose_name='رنگ', max_length=120)

    class Meta:
        verbose_name = 'شبکه اجتماعی'
        verbose_name_plural = 'شبکه های اجتماعی'

    def __str__(self):
        return self.name


class FooterInfo(models.Model):
    phone_number = models.CharField(max_length=11, blank=False, null=True, verbose_name='شماره ثابت')
    mobile_number = models.CharField(max_length=11, blank=False, null=True, verbose_name='شماره موبایل')
    address = models.CharField(max_length=250, blank=False, null=True, verbose_name='آدرس')
    email = models.EmailField(max_length=40, blank=True, null=True, verbose_name='ایمیل')

    class Meta:
        verbose_name = 'تنظیم فوتر'
        verbose_name_plural = 'تنظیمات فوتر'

    def __str__(self):
        return self.email
