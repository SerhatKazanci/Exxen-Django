# Generated by Django 3.2.12 on 2022-07-15 11:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('resim', models.FileField(blank=True, null=True, upload_to='movies', verbose_name='Film resmi')),
                ('title', models.CharField(max_length=200)),
            ],
        ),
    ]
