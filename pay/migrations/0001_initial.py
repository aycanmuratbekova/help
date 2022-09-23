# Generated by Django 4.0.7 on 2022-09-23 07:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.IntegerField(default=0)),
                ('description', models.TextField(verbose_name='description')),
                ('salt', models.CharField(max_length=25, verbose_name='salt')),
            ],
        ),
    ]
