from django.db import models
from django.contrib import admin


class Warning_Devices(models.Model):
	device_name = models.CharField(max_length=50)
	location = models.CharField(max_length=50)
	latitude = models.FloatField(default=None)
	longitude = models.FloatField(default=None)
	device_info = models.TextField()
	device_img = models.ImageField(
		default='default.jpg',
		upload_to='device_imgs',
		null=True,
		blank=True)

	def __str__(self):
		return self.device_name


	class Meta:
		verbose_name = "Early Warning Device"
		verbose_name_plural = "Early Warning Devices"



class Evac_Centers(models.Model):
	building_name = models.CharField(max_length=50)
	location = models.CharField(max_length=50)
	latitude = models.FloatField(default=None)
	longitude = models.FloatField(default=None)
	building_img = models.ImageField(
		default='default.jpg',
		upload_to='evac_center_imgs',
		null=True,
		blank=True)

	def __str__(self):
		return self.building_name

	class Meta:
		verbose_name = "Evacuation Center"
		verbose_name_plural = "Evacuation Centers"


class Warning_Signs(models.Model):
	sign_name = models.CharField(max_length=50)
	location = models.CharField(max_length=50)
	latitude = models.FloatField(default=None)
	longitude = models.FloatField(default=None)
	sign_img = models.ImageField(
		default='default.jpg',
		upload_to='sign_imgs',
		null=True,
		blank=True)


	def __str__(self):
		return self.sign_name

	class Meta:
		verbose_name = "Warning Sign"
		verbose_name_plural = "Warning Signs"




class History(models.Model):
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

	barangay_name = models.CharField(max_length=100,choices=BARANGAY,default='Alegria')
	barangay_img = models.ImageField(upload_to='history_imgs',blank=True)
	barangay_info = models.TextField()

	def __str__(self):
		return f"{self.barangay_name} - GeoHazard History"
	
class GeoHazard(models.Model):
	history = models.ForeignKey(History, related_name='geohazards', on_delete=models.CASCADE)
	geohazard_img = models.ImageField(upload_to='history_imgs',blank=True)
	geohazard_info = models.TextField()

	def __str__(self):
		return f"GeoHazard Details - {self.id}"
	


class GeoHazardInline(admin.StackedInline):
	model = GeoHazard


class HistoryAdmin(admin.ModelAdmin):
	inlines = [
		GeoHazardInline,
	]






























# class Disaster_History(models.Model):
# 	BARANGAY = (
# 		('Alegria','Alegria'),
# 		('Bagacay','Bagacay'),
# 		('Baluntay','Baluntay'),
# 		('Datal Anggas','Datal Anggas'),
# 		('Domolok','Domolok'),
# 		('Kawas','Kawas'),
# 		('Ladol','Ladol'),
# 		('Maribulan','Maribulan'),
# 		('Pag-Asa','Pag-Asa'),
# 		('Paraiso','Paraiso'),
# 		('Poblacion','Poblacion'),
# 		('Spring','Spring'),
# 		('Tokawal','Tokawal')
# 	)
# 	barangay_name = models.CharField(max_length=100,choices=BARANGAY,default='Alegria')
# 	barangay_img = models.ImageField(default='default.jpg',upload_to='disaster_imgs',blank=True)
# 	barangay_info = models.TextField(null=True,blank=True)
# 	disaster_img = models.ImageField(default='default.jpg',upload_to='disaster_imgs',blank=True)
# 	disaster_info = models.TextField()
	
# 	def __str__(self):
# 		return f"{self.barangay_name} - Disaster History"


# 	class Meta:
# 		verbose_name = 'Disaster History'
# 		verbose_name_plural = 'Disaster Histories'
# 		ordering = ['barangay_name']




# class Disaster_Assessment(models.Model):
# 	BARANGAY = (
# 		('Alegria','Alegria'),
# 		('Bagacay','Bagacay'),
# 		('Baluntay','Baluntay'),
# 		('Datal Anggas','Datal Anggas'),
# 		('Domolok','Domolok'),
# 		('Kawas','Kawas'),
# 		('Ladol','Ladol'),
# 		('Maribulan','Maribulan'),
# 		('Pag-Asa','Pag-Asa'),
# 		('Paraiso','Paraiso'),
# 		('Poblacion','Poblacion'),
# 		('Spring','Spring'),
# 		('Tokawal','Tokawal')
# 	)

# 	RATINGS = (
# 	    ('HIGH','HIGH'),
#  	    ('HIGH (Mitigated)','HIGH (Mitigated)'),
# 	    ('MODERATE','MODERATE'),
#  	    ('MODERATE (Mitigated)','MODERATE (Mitigated)'),
# 	    ('LOW','LOW'),
# 	    ('UNKNOWN','UNKNOWN'),
# 	)
	
# 	barangay_name = models.CharField(max_length=100,choices=BARANGAY,default='Alegria')
# 	purok_name = models.CharField(max_length=100)
# 	purok_coordinates = models.CharField(max_length=200,blank=True,null=True)
# 	flood_rating = models.CharField(max_length=100,choices=RATINGS,default='UNKNOWN')
# 	landslide_rating = models.CharField(max_length=100,choices=RATINGS,default='UNKNOWN')

# 	def __str__(self):
# 		return f"{self.barangay_name} - Disaster Assessment"