# Generated by Django 2.2.5 on 2019-11-24 09:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0019_userprofile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newsroom',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='media/'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='media/'),
        ),
    ]
