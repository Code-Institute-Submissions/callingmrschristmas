# Generated by Django 2.2.9 on 2020-01-20 18:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0002_auto_20200112_1453'),
    ]

    operations = [
        migrations.AddField(
            model_name='contactdetails',
            name='full_name',
            field=models.CharField(default='Cassie Smith', max_length=50),
            preserve_default=False,
        ),
    ]
