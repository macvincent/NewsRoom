# Generated by Django 2.2.3 on 2019-08-03 11:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_auto_20190802_2027'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newsroom',
            name='title',
            field=models.CharField(max_length=300),
        ),
    ]
