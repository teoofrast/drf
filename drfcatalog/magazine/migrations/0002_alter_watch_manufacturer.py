# Generated by Django 4.2.13 on 2024-06-11 15:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('magazine', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='watch',
            name='manufacturer',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='watches', to='magazine.manufacturer'),
        ),
    ]
