# Generated by Django 5.1.3 on 2025-02-28 16:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usermoreinfo',
            name='SocialMediaLink',
            field=models.URLField(blank=True),
        ),
    ]
