from django.db import models
from PIL import Image

class Warning_Devices(models.Model):
	device_name = models.CharField(max_length=50, verbose_name='Device Name',unique=True)
	location = models.CharField(max_length=50, help_text="Places/Sites (i.e., Street Name,Purok,Barangay,Land Marks)")
	latitude = models.FloatField(null=False,blank=False)
	longitude = models.FloatField(null=False,blank=False)
	device_info = models.TextField(verbose_name='Description')
	device_img = models.ImageField(default='default.jpg',upload_to='device_imgs',verbose_name='Image')

	def __str__(self):
		return self.device_name
	
	def save(self,*args,**kwargs):
		super().save(*args,**kwargs)

		img = Image.open(self.device_img.path)

		if img.height > 200 or img.width > 200:
			output_size = (200,200)
			img.thumbnail(output_size)
			img.save(self.device_img.path)

	class Meta:
		verbose_name = "Warning Device"
		verbose_name_plural = "Warning Devices"


class Evac_Centers(models.Model):
	building_name = models.CharField(max_length=50, verbose_name='Building Name',unique=True)
	location = models.CharField(max_length=50, help_text="Places/Sites (i.e., Street Name,Purok,Barangay,Land Marks)")
	latitude = models.FloatField(null=False,blank=False)
	longitude = models.FloatField(null=False,blank=False)
	building_img = models.ImageField(default='default.jpg',upload_to='evac_center_imgs', verbose_name='Image')

	def __str__(self):
		return self.building_name
	
	def save(self,*args,**kwargs):
		super().save(*args,**kwargs)

		img = Image.open(self.building_img.path)

		if img.height > 200 or img.width > 200:
			output_size = (200,200)
			img.thumbnail(output_size)
			img.save(self.building_img.path)

	class Meta:
		verbose_name = "Evacuation Center"
		verbose_name_plural = "Evacuation Centers"


class Warning_Signs(models.Model):
	sign_name = models.CharField(max_length=50, verbose_name='Sign Name',unique=True)
	location = models.CharField(max_length=50, help_text="Places/Sites (i.e., Street Name,Purok,Barangay,Land Marks)")
	latitude = models.FloatField(null=False,blank=False)
	longitude = models.FloatField(null=False,blank=False)
	sign_img = models.ImageField(default='default.jpg',upload_to='sign_imgs', verbose_name='Image')


	def __str__(self):
		return self.sign_name

	def save(self,*args,**kwargs):
		super().save(*args,**kwargs)

		img = Image.open(self.sign_img.path)

		if img.height > 200 or img.width > 200:
			output_size = (200,200)
			img.thumbnail(output_size)
			img.save(self.sign_img.path)

	class Meta:
		verbose_name = "Warning Sign"
		verbose_name_plural = "Warning Signs"