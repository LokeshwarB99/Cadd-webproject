# Generated by Django 4.2.1 on 2023-06-22 14:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('caddWebsiteMain', '0018_courseindex_coursegroupid'),
    ]

    operations = [
        migrations.CreateModel(
            name='core',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('corename', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='module',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('modulename', models.TextField()),
                ('cores', models.ManyToManyField(related_name='contains', to='caddWebsiteMain.core')),
            ],
        ),
    ]
