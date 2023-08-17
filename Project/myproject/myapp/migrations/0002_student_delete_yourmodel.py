# Generated by Django 4.2.4 on 2023-08-15 20:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('branch', models.CharField(max_length=50)),
                ('roll', models.IntegerField()),
                ('section', models.CharField(max_length=5)),
                ('age', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.DeleteModel(
            name='YourModel',
        ),
    ]
