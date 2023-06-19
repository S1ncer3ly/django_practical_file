# Generated by Django 4.2 on 2023-06-19 08:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Auth_first_name', models.CharField(max_length=30)),
                ('Auth_email', models.EmailField(max_length=254)),
                ('Title', models.CharField(max_length=100)),
                ('Publisher', models.CharField(max_length=100)),
                ('Publication_Year', models.IntegerField(default=0)),
                ('Issue_Status', models.BooleanField(default=False)),
                ('Issued_Roll_No', models.IntegerField(default=0)),
            ],
            options={
                'verbose_name_plural': 'Book',
            },
        ),
    ]
