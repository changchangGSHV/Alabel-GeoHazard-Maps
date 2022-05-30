# Generated by Django 3.2.7 on 2022-05-28 08:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auxiliary', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Disaster_Assessment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('purok_name', models.CharField(max_length=100)),
                ('purok_coordinates', models.CharField(blank=True, max_length=200, null=True)),
                ('flood_rating', models.CharField(choices=[('HIGH', 'HIGH'), ('HIGH (Mitigated)', 'HIGH (Mitigated)'), ('MODERATE', 'MODERATE'), ('MODERATE (Mitigated)', 'MODERATE (Mitigated)'), ('LOW', 'LOW'), ('UNKNOWN', 'UNKNOWN')], default='UNKNOWN', max_length=100)),
                ('landslide_rating', models.CharField(choices=[('HIGH', 'HIGH'), ('HIGH (Mitigated)', 'HIGH (Mitigated)'), ('MODERATE', 'MODERATE'), ('MODERATE (Mitigated)', 'MODERATE (Mitigated)'), ('LOW', 'LOW'), ('UNKNOWN', 'UNKNOWN')], default='UNKNOWN', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Disaster_History',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('barangay_name', models.CharField(choices=[('Alegria', 'Alegria'), ('Bagacay', 'Bagacay'), ('Baluntay', 'Baluntay'), ('Datal Anggas', 'Datal Anggas'), ('Domolok', 'Domolok'), ('Kawas', 'Kawas'), ('Ladol', 'Ladol'), ('Maribulan', 'Maribulan'), ('Pag-Asa', 'Pag-Asa'), ('Paraiso', 'Paraiso'), ('Poblacion', 'Poblacion'), ('Spring', 'Spring'), ('Tokawal', 'Tokawal')], default='Alegria', max_length=100)),
                ('barangay_img', models.ImageField(blank=True, default='default.jpg', upload_to='disaster_imgs')),
                ('disaster_img', models.ImageField(blank=True, default='default.jpg', upload_to='disaster_imgs')),
                ('disaster_info', models.TextField()),
                ('purok_assessments', models.ManyToManyField(to='auxiliary.Disaster_Assessment')),
            ],
            options={
                'verbose_name': 'Disaster History',
                'verbose_name_plural': 'Disaster Histories',
            },
        ),
    ]
