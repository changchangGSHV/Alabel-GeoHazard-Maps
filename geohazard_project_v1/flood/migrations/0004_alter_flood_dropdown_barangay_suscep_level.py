# Generated by Django 3.2.7 on 2022-04-24 11:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('flood', '0003_alter_flood_dropdown_barangay_suscep_level'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flood_dropdown',
            name='barangay_suscep_level',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='flood.flood', to_field='suscep_level'),
        ),
    ]
