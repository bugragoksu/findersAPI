# Generated by Django 3.0.3 on 2020-03-02 20:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('account', '0002_delete_account'),
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=100, verbose_name='Email')),
                ('pasword', models.CharField(max_length=100, verbose_name='Password')),
                ('name', models.CharField(max_length=100, verbose_name='Name')),
                ('surname', models.CharField(max_length=100, verbose_name='Surname')),
                ('city', models.CharField(max_length=100, verbose_name='City')),
                ('image', models.CharField(blank=True, max_length=500, verbose_name='ImageUrl')),
            ],
        ),
    ]