from django.core.files.storage import FileSystemStorage
from landslide.models import MDRRMO
from datetime import date as dt
from django.db import models
import os


class Flood(MDRRMO):
	RESPONSE_LEVEL = (
		('N/A', 'N/A'),
		('Level 1', 'Level 1'),
		('Level 2', 'Level 2'),
		('Level 3', 'Level 3')
	)
	
	flood_id = models.BigAutoField(primary_key=True, unique=True)
	suscep_level = models.CharField(max_length=50, unique=True,choices=RESPONSE_LEVEL, verbose_name='Response Level',default='N/A')
	suscep_info = models.TextField(verbose_name='Response Level Description')

	def __str__(self):
		return self.suscep_level

# Flood(Base)
class Flood_Base(models.Model):
	flood = models.ForeignKey(Flood,verbose_name="Response Levels",on_delete=models.CASCADE)


	class Meta:
		abstract = True



class Flood_Markers(models.Model):
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

	flood_marker_id = models.BigAutoField(primary_key=True)
	barangay_name = models.CharField(max_length=50,default='Alegria',choices=BARANGAY, unique=True)
	barangay_suscep_level = models.CharField(max_length=50,choices=FLOOD_LEVELS, verbose_name="Risk Level")
	latitude = models.FloatField(null=False,blank=False)
	longitude = models.FloatField(null=False,blank=False)
	map_marker_img = models.ImageField(default='default.jpg',upload_to='flood_marker_imgs',blank=True)
	map_marker_info = models.TextField()

	def __str__(self):
		return self.barangay_name

	class Meta:
		verbose_name = "Flood Marker"
		verbose_name_plural = 'Flood Markers'
		ordering = ['barangay_name']


class Flood_Guidelines(Flood_Base):
	guide_id = models.BigAutoField(primary_key=True)
	alert_level = models.CharField(max_length=50, unique=True, verbose_name="Title")
	alert_level_guide = models.TextField(verbose_name="Content")
	date_published = models.DateField(default=dt.today)

	def __str__(self):
		return self.alert_level

	class Meta:
		verbose_name = "'Flood Guidelines'"
		verbose_name_plural = 'Flood Guidelines'
		ordering = ['guide_id'] 


class Flood_Procedures(Flood_Base):
	procedure_id = models.BigAutoField(primary_key=True)
	procedure_name = models.CharField(max_length=50, unique=True)
	procedure_content = models.TextField()

	def __str__(self):
		return self.procedure_name

	class Meta:
		verbose_name = 'Flood Procedure'
		verbose_name_plural = 'Flood Procedures'
		ordering = ['procedure_id']


# Code for Choropleth Section
class OverwriteStorage(FileSystemStorage):
	CHOROPLETH_PATH = "choropleth_storage"

	def get_available_name(self, name, max_length=None):
		if self.exists(name):
			os.remove(os.path.join(self.CHOROPLETH_PATH, name))
		return name 

choropleth_storage = OverwriteStorage(location="choropleth_storage")


def rename_to_low(instance, filename):
	ext = filename.split('.')[-1]
	filename = "low_lvl.%s" % (ext)
	return os.path.join('dynamic/flood_map',filename)

def rename_to_mod(instance, filename):
	ext = filename.split('.')[-1]
	filename = "mod_lvl.%s" % (ext)
	return os.path.join('dynamic/flood_map',filename)

def rename_to_high(instance, filename):
	ext = filename.split('.')[-1]
	filename = "high_lvl.%s" % (ext)
	return os.path.join('dynamic/flood_map',filename)


class Flood_Choropleth(MDRRMO):
	low_risk_map = models.FileField(
		storage=choropleth_storage,
		upload_to=rename_to_low,
		verbose_name="Low Risk Map",
		help_text="Note: Make sure you uploaded the correct 'Low Risk Map' file before confirming changed")

	mod_risk_map = models.FileField(
		storage=choropleth_storage,
		upload_to=rename_to_mod,
		verbose_name="Moderate Risk Map",
		help_text="Note: Make sure you uploaded the correct 'Moderate Risk Map' file before confirming changed")

	high_risk_map = models.FileField(
		storage=choropleth_storage,
		upload_to=rename_to_high,
		verbose_name="High Risk Map",
		help_text="Note: Make sure you uploaded the correct 'High Risk Map' file before confirming changed")

	confirm_map = models.BooleanField(
		default=False,
		verbose_name="Confirm Map Changes?",
		help_text="(Click on Checkbox) We recommend to 'double-check' the uploaded file first, before confirming change.")


	date_changed = models.DateTimeField(default=dt.today)

	def __str__(self):
		DATE_FORMAT = "{:%B %d, %Y (%A)}".format(self.date_changed) 

		return f"Choropleth Maps was edited by: '{self.admin_id}' on '{DATE_FORMAT}'"

	class Meta:
		verbose_name = "Flood Choropleth"
		verbose_name_plural = "Flood Choropleths"


