# Generated by Django 3.2.4 on 2021-06-29 14:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Weblog_Blog', '0008_sidebar_socialmedias'),
    ]

    operations = [
        migrations.AlterField(
            model_name='socialmedias',
            name='color',
            field=models.CharField(choices=[('telegram', 'تلگرام'), ('twitter', 'توییتر'), ('instagram', 'اینستاگرام'), ('aparat', 'آپارات'), ('youtube', 'یوتیوب')], max_length=120, null=True, verbose_name='رنگ'),
        ),
    ]
