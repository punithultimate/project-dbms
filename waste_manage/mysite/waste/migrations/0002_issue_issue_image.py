# Generated by Django 3.1.4 on 2021-01-04 02:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('waste', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='issue',
            name='issue_image',
            field=models.CharField(default='https://www.economist.com/img/b/1280/720/90/sites/default/files/images/2019/06/articles/main/20190622_std001.jpg', max_length=500),
        ),
    ]
