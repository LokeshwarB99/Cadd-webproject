# Generated by Django 4.2.1 on 2023-06-24 09:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('caddWebsiteMain', '0024_alter_module_cores'),
    ]

    operations = [
        migrations.AlterField(
            model_name='module',
            name='cores',
            field=models.ManyToManyField(blank=True, related_name='contains', to='caddWebsiteMain.core'),
        ),
    ]
