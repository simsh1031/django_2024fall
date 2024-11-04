# Generated by Django 4.2 on 2024-11-04 03:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': '학과',
                'db_table': 'department',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
                ('email', models.CharField(max_length=50)),
                ('phone_number', models.CharField(max_length=10)),
                ('student_id', models.CharField(max_length=10, verbose_name='학번')),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='example_app.department')),
            ],
            options={
                'verbose_name': '학생',
                'db_table': 'student',
            },
        ),
        migrations.CreateModel(
            name='Professor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
                ('email', models.CharField(max_length=50)),
                ('phone_number', models.CharField(max_length=10)),
                ('employee_id', models.CharField(max_length=10)),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='example_app.department')),
            ],
            options={
                'verbose_name': '교직원',
                'db_table': 'professor',
            },
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_name', models.CharField(max_length=100)),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='example_app.department')),
                ('professor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='example_app.professor')),
            ],
            options={
                'verbose_name': '강의',
                'db_table': 'course',
            },
        ),
    ]
