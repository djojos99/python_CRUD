# Generated by Django 5.0.2 on 2024-02-28 15:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('EmpId', models.CharField(max_length=3)),
                ('EmpName', models.CharField(max_length=100)),
                ('EmpGender', models.CharField(max_length=10)),
                ('EmpEmail', models.EmailField(max_length=200)),
                ('EmpDesignation', models.CharField(max_length=130)),
            ],
            options={
                'db_table': 'Employee',
            },
        ),
    ]
