# Generated by Django 2.2.3 on 2019-08-02 19:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_auto_20190802_1914'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newsroom',
            name='title',
            field=models.CharField(max_length=300, unique=True),
        ),
    ]
