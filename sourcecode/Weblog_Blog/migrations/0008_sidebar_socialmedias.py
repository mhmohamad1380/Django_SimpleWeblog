# Generated by Django 3.2.4 on 2021-06-29 14:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Weblog_Blog', '0007_alter_blogcontent_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sidebar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(null=True, verbose_name='توضیحات')),
            ],
            options={
                'verbose_name': 'سایدبار',
                'verbose_name_plural': 'سایدبار',
            },
        ),
        migrations.CreateModel(
            name='SocialMedias',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120, null=True, verbose_name='نام')),
                ('link', models.URLField(null=True, verbose_name='لینک')),
                ('color', models.CharField(choices=[('red', 'قرمز'), ('black', 'مشکی'), ('blue', 'آبی'), ('grey', 'نقره ای'), ('white', 'سفید'), ('yellow', 'زرد'), ('green', 'سبز'), ('orange', 'نارنجی'), ('brown', 'قهوه ای'), ('purple', 'بنفش'), ('pink', 'صورتی'), ('lightblue', 'آبی روشن')], max_length=120, null=True, verbose_name='رنگ')),
            ],
            options={
                'verbose_name': 'شبکه اجتماعی',
                'verbose_name_plural': 'شبکه های اجتماعی',
            },
        ),
    ]