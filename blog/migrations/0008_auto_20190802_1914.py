# Generated by Django 2.2.3 on 2019-08-02 19:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_auto_20190802_1912'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newsroom',
            name='post',
            field=models.TextField(default='posts', null=True),
        ),
    ]
