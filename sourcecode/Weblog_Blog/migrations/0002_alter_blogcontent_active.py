# Generated by Django 3.2.4 on 2021-06-27 16:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Weblog_Blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogcontent',
            name='active',
            field=models.IntegerField(choices=[(0, 'غیرفعال'), (1, 'فعال')], verbose_name='فعال/غیر فعال'),
        ),
    ]
