# Generated by Django 4.2.1 on 2023-05-31 09:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='aboutUs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descriptionTitle', models.CharField(max_length=100)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='courseIndex',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('courseName', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='partners',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('productName', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('partnerName', models.CharField(max_length=100)),
                ('partnerLink', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='testimonials',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('feedback', models.TextField()),
                ('studentName', models.CharField(max_length=100)),
                ('ratings', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='subCourseIndex',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subCourseName', models.CharField(max_length=100)),
                ('superCourseId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='caddWebsiteMain.courseindex')),
            ],
        ),
        migrations.CreateModel(
            name='subCourseDescription',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descriptionTitle', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('subCourseId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='caddWebsiteMain.subcourseindex')),
            ],
        ),
        migrations.CreateModel(
            name='projects',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('projectTitle', models.CharField(max_length=100)),
                ('projectDescription', models.TextField()),
                ('superCourseId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='caddWebsiteMain.courseindex')),
            ],
        ),
        migrations.CreateModel(
            name='courseDescription',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descriptionTitle', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('courseId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='caddWebsiteMain.courseindex')),
            ],
        ),
    ]
