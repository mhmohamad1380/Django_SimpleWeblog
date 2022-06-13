# Generated by Django 3.2.4 on 2021-06-30 11:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Weblog_Blog', '0010_alter_sidebar_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='FooterInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone_number', models.CharField(max_length=11, null=True, verbose_name='شماره ثابت')),
                ('mobile_number', models.CharField(max_length=11, null=True, verbose_name='شماره موبایل')),
                ('Address', models.CharField(max_length=250, null=True, verbose_name='آدرس')),
                ('email', models.EmailField(blank=True, max_length=40, null=True, verbose_name='ایمیل')),
            ],
            options={
                'verbose_name': 'تنظیم فوتر',
                'verbose_name_plural': 'تنظیمات فوتر',
            },
        ),
    ]