# Generated by Django 4.2.1 on 2023-06-26 06:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('caddWebsiteMain', '0032_alter_coursegroup_coursegroupslug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coursegroup',
            name='courseGroupSlug',
            field=models.SlugField(blank=True, max_length=255, null=True, unique=True),
        ),
    ]