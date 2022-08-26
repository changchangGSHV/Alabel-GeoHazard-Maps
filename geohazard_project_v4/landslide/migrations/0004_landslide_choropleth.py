# Generated by Django 3.2.7 on 2022-07-18 13:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import landslide.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('landslide', '0003_alter_landslide_guidelines_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='Landslide_Choropleth',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('low_risk_map', models.FileField(help_text="Note: Make sure you uploaded the correct 'Low Risk Map' file before confirming changed", storage=landslide.models.OverwriteStorage(location='choropleth_storage'), upload_to=landslide.models.rename_to_low, verbose_name='Low Risk Map')),
                ('mod_risk_map', models.FileField(help_text="Note: Make sure you uploaded the correct 'Moderate Risk Map' file before confirming changed", storage=landslide.models.OverwriteStorage(location='choropleth_storage'), upload_to=landslide.models.rename_to_mod, verbose_name='Moderate Risk Map')),
                ('high_risk_map', models.FileField(help_text="Note: Make sure you uploaded the correct 'High Risk Map' file before confirming changed", storage=landslide.models.OverwriteStorage(location='choropleth_storage'), upload_to=landslide.models.rename_to_high, verbose_name='High Risk Map')),
                ('confirm_map', models.BooleanField(default=False, help_text="(Click on Checkbox) We recommend to 'double-check' the uploaded file first, before confirming change.", verbose_name='Confirm Map Changes?')),
                ('admin_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='Admin')),
            ],
            options={
                'verbose_name': 'Landslide Choropleth',
                'verbose_name_plural': 'Landslide Choropleths',
            },
        ),
    ]
