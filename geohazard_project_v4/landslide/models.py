from django.core.files.storage import FileSystemStorage
from django.contrib.auth.models import User
from django.conf import settings
from datetime import date as dt
from django.db import models
import os


#Admin(Base)
class MDRRMO(models.Model):
	admin_id = models.ForeignKey(User,on_delete=models.PROTECT,verbose_name="Admin")

	class Meta:
		abstract = True


class Landslide(MDRRMO):
	RESPONSE_LEVEL = (
		('N/A', 'N/A'),
		('Level 1', 'Level 1'),
		('Level 2', 'Level 2'),
		('Level 3', 'Level 3')
	)

	lands_id = models.BigAutoField(primary_key=True)
	suscep_level = models.CharField(max_length=50, unique=True,choices=RESPONSE_LEVEL, verbose_name='Response Level',default='N/A')
	suscep_info = models.TextField(verbose_name='Response Level Description')

	def __str__(self):
		return self.suscep_level


# Landslide(Base)
class Lands_Base(models.Model):
	landslide = models.ForeignKey(Landslide,verbose_name="Response Levels",on_delete=models.CASCADE)

	class Meta:
		abstract = True


class Landslide_Markers(models.Model):
	LANDSLIDE_LEVELS = (
			('Low','Low'),
			('Moderate','Moderate'),
			('High','High'),
			('Very High','Very High'),
		)

	# 13 Barangays
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

	lands_marker_id = models.BigAutoField(primary_key=True)
	barangay_name = models.CharField(max_length=50,default='Alegria',choices=BARANGAY, unique=True)
	barangay_suscep_level = models.CharField(max_length=50,choices=LANDSLIDE_LEVELS, verbose_name="Risk Level")
	latitude = models.FloatField(null=False,blank=False)
	longitude = models.FloatField(null=False,blank=False)
	map_marker_img = models.ImageField(default='default.jpg',upload_to='landslide_marker_imgs',blank=True)
	map_marker_info = models.TextField()
	

	def __str__(self):
		return self.barangay_name

	class Meta:
		verbose_name = 'Landslide Marker'
		verbose_name_plural = 'Landslide Markers'
		ordering = ['barangay_name']


class Landslide_Guidelines(Lands_Base):
	guide_id = models.BigAutoField(primary_key=True)
	alert_level = models.CharField(max_length=50,unique=True, verbose_name="Title")
	alert_level_guide = models.TextField(verbose_name="Content")
	date_published = models.DateField(default=dt.today)

	def __str__(self):
		return self.alert_level

	class Meta:
		verbose_name = 'Landslide Guidelines'
		verbose_name_plural = 'Landslide Guidelines'
		ordering = ['guide_id'] 



class Landslide_Procedures(Lands_Base):
	procedure_id = models.BigAutoField(primary_key=True)
	procedure_name = models.CharField(max_length=50, unique=True)
	procedure_content = models.TextField()

	def __str__(self):
		return self.procedure_name

	class Meta:
		verbose_name = 'Landslide Procedure'
		verbose_name_plural = 'Landslide Procedures'


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
	return os.path.join('dynamic/landslide_map',filename)

def rename_to_mod(instance, filename):
	ext = filename.split('.')[-1]
	filename = "mod_lvl.%s" % (ext)
	return os.path.join('dynamic/landslide_map',filename)

def rename_to_high(instance, filename):
	ext = filename.split('.')[-1]
	filename = "high_lvl.%s" % (ext)
	return os.path.join('dynamic/landslide_map',filename)


class Landslide_Choropleth(MDRRMO):
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
		verbose_name = "Landslide Choropleth"
		verbose_name_plural = "Landslide Choropleths"



