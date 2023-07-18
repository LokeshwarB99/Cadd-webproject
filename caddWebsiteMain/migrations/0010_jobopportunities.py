# Generated by Django 4.2.1 on 2023-06-11 15:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('caddWebsiteMain', '0009_contactus'),
    ]

    operations = [
        migrations.CreateModel(
            name='jobOpportunities',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('jobRole', models.CharField(max_length=100)),
                ('companyName', models.CharField(max_length=100)),
                ('location', models.TextField(blank=True)),
                ('companyLogo', models.ImageField(upload_to='images/placements/')),
                ('companyWebsiteLink', models.CharField(blank=True, max_length=200, null=True)),
                ('category', models.CharField(max_length=100)),
                ('salary', models.IntegerField()),
                ('education', models.CharField(max_length=200)),
                ('experience', models.CharField(blank=True, max_length=100, null=True)),
                ('keyFeatures', models.TextField(blank=True)),
                ('lastDate', models.DateField(null=True)),
            ],
        ),
    ]