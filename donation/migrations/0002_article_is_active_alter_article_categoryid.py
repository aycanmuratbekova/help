# Generated by Django 4.1.1 on 2022-09-22 11:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('donation', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='is_active',
            field=models.BooleanField(default=False, verbose_name='Одобрено'),
        ),
        migrations.AlterField(
            model_name='article',
            name='categoryId',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='donation', to='donation.category', verbose_name='Категория'),
        ),
    ]