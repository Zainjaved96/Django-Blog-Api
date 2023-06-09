# Generated by Django 4.2.1 on 2023-06-09 07:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog_service', '0005_remove_publisher_reporter'),
    ]

    operations = [
        migrations.RenameField(
            model_name='publisher',
            old_name='company',
            new_name='company_name',
        ),
        migrations.AddField(
            model_name='publisher',
            name='phone_no',
            field=models.CharField(default='None', max_length=100),
        ),
    ]
