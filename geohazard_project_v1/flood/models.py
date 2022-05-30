from django.db import models
from landslide.models import MDRRMO
import jinja2


class Flood(MDRRMO):
	flood_id = models.BigAutoField(primary_key=True, unique=True)
	suscep_level = models.CharField(max_length=50, unique=True)
	suscep_info = models.TextField()

	def __str__(self):
		return self.suscep_level

# Flood(Base)
class Flood_Base(models.Model):
	flood_id = models.ForeignKey(Flood,on_delete=models.CASCADE)


	class Meta:
		abstract = True


class Flood_Evac_Procedures(Flood_Base):
	evac_id = models.BigAutoField(primary_key=True)
	procedure_name = models.CharField(max_length=50, unique=True)
	procedure_content = models.TextField()

	def __str__(self):
		return self.procedure_name

	class Meta:
		verbose_name = 'Evacuation Procedure'
		verbose_name_plural = 'Flood Evacuation Procedures'


class Flood_Dropdown(models.Model):
	FLOOD_LEVELS = (
			('Low','Low'),
			('Moderate','Moderate'),
			('High','High'),
			('Very High','Very High'),
		)

	BARANGAY = (
			('Alegria','Alegria'),
			('Bagacay','Bagacay'),
			('Baluntay','Baluntay'),
			('Datal Anggas','Datal Anggas'),
			('Domolok','Domolok'),
			('Kawas','Kawas'),
			('Ladol','Ladol'),
			('Maribulan','Maribulan'),
			('Pag-Asa','Pag-Asa'),
			('Paraiso','Paraiso'),
			('Poblacion','Poblacion'),
			('Spring','Spring'),
			('Tokawal','Tokawal')
		)

	flood_drop_id = models.BigAutoField(primary_key=True)
	barangay_name = models.CharField(max_length=50,default='Alegria',choices=BARANGAY, unique=True)
	barangay_suscep_level = models.CharField(max_length=50,choices=FLOOD_LEVELS)
	latitude = models.FloatField(blank=True,default=None)
	longitude = models.FloatField(blank=True,default=None)
	map_marker_img = models.ImageField(default='default.jpg',upload_to='flood_marker_imgs',blank=True)
	map_marker_info = models.TextField()

	def __str__(self):
		return self.barangay_name

	class Meta:
		verbose_name = "'Barangay'"
		verbose_name_plural = 'Flood Dropdown'
		ordering = ['barangay_name']


class Flood_Guidelines(Flood_Base):
	from datetime import date as dt

	guide_id = models.BigAutoField(primary_key=True)
	alert_level = models.CharField(max_length=50, unique=True)
	alert_level_guide = models.TextField()
	date_published = models.DateField(default=dt.today)

	def __str__(self):
		return self.alert_level

	class Meta:
		verbose_name = "'Flood Guidelines'"
		verbose_name_plural = 'Flood Guidelines'
		ordering = ['-date_published'] 




