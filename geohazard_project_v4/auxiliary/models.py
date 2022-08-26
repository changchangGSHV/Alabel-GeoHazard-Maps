from django.db import models
from landslide.models import MDRRMO
from django.utils import timezone
from PIL import Image


class Announcements(MDRRMO):
	announ_id = models.BigAutoField(primary_key=True)
	title = models.CharField(max_length=30, verbose_name='Title')
	announ_image = models.ImageField(upload_to='announ_images',verbose_name='Image (Optional)',null=True,blank=True)
	content = models.TextField(verbose_name='Content',help_text="Please make sure to keep the content 'concise' as possible.")
	date_posted = models.DateTimeField(verbose_name='Date Published',default=timezone.now)

	def __str__(self):
		return self.title

	class Meta:
		verbose_name_plural = 'Announcements'
		ordering = ['-date_posted']
		unique_together = ['title','content']


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

	barangay_name = models.CharField(max_length=100,choices=BARANGAY,default='Alegria',verbose_name='Barangay Name')
	barangay_img = models.ImageField(upload_to='history_imgs',blank=True,verbose_name='Image',default='default.jpg')
	barangay_info = models.TextField(verbose_name="History",blank=True)

	def __str__(self):
		return f"{self.barangay_name} - GeoHazard History"
	
	def save(self,*args,**kwargs):
		super().save(*args,**kwargs)

		img = Image.open(self.barangay_img.path)

		if img.height > 300 or img.width > 300:
			output_size = (200,200)
			img.thumbnail(output_size)
			img.save(self.barangay_img.path)

	class Meta:
		ordering = ['barangay_name']
		verbose_name = 'History'
		verbose_name_plural = 'Histories'
	
class GeoHazard(models.Model):
	history = models.ForeignKey(History, related_name='geohazards', on_delete=models.CASCADE)
	geohazard_img = models.ImageField(upload_to='history_imgs',blank=True, verbose_name='Image',default='default.jpg')
	date_published = models.CharField(max_length=50,null=True,blank=True)
	geohazard_info = models.TextField(verbose_name='Description')

	def __str__(self):
		return f"GeoHazard Details"

	def save(self,*args,**kwargs):
		super().save(*args,**kwargs)

		img = Image.open(self.geohazard_img.path)

		if img.height > 300 or img.width > 300:
			output_size = (300,300)
			img.thumbnail(output_size)
			img.save(self.geohazard_img.path)

	class Meta:
		verbose_name = 'GeoHazard'
		verbose_name_plural = 'GeoHazards'


class Assessment(models.Model):
	RATINGS = (
		('LOW','LOW'),
		('MODERATE','MODERATE'),
	    ('HIGH','HIGH'),
	    ('MODERATE (Mitigated)','MODERATE (Mitigated)'),
 	    ('HIGH (Mitigated)','HIGH (Mitigated)'),
 	    ('LOW-MODERATE','LOW-MODERATE'),
 	    ('MODERATE-HIGH','MODERATE-HIGH'),
 	    ('LOW(High Near Rivers)','LOW(High Near Rivers)'),
 	    ('LOW(H/M Near Rivers)','LOW(H/M Near Rivers)'),
 	    ('MODERATE(High Near Rivers)','MODERATE(High Near Rivers)'),
 	    ('LOW(High On Slopes)','LOW(High On Slopes)'),
 	    ('MODERATE(High On Slopes)','MODERATE(High On Slopes)'),
 	    ('LOW(H/M On Slopes)','LOW(H/M On Slopes)'),
 	    ('LOW(High Near Creeks)','LOW(High Near Creeks)'),
 	    ('LOW(Moderate Near Creeks)','LOW(Moderate Near Creeks)'),
 	    ('MODERATE(High Near Creeks)','MODERATE(High Near Creeks)'),
	    ('UNKNOWN','UNKNOWN'),
	)

	history = models.ForeignKey(History, related_name='assessment', on_delete=models.CASCADE)
	purok_name = models.CharField(max_length=50, verbose_name='Purok Name')
	purok_coordinates = models.CharField(max_length=100,default='Not Specified', verbose_name='Coordinates')
	landslide_rating = models.CharField(max_length=100,choices=RATINGS,default='UNKNOWN', verbose_name='Landslide Rating')
	flood_rating = models.CharField(max_length=100,choices=RATINGS,default='UNKNOWN', verbose_name='Flood Rating')
	
	
	def __str__(self):
		return f"GeoHazard Assessment"

	class Meta:
		verbose_name = 'Assessment'
		verbose_name_plural = 'Assessments'
		ordering = ['id']
	

class Contacts(models.Model):
	office_name = models.CharField(max_length=100,null=True,blank=True)
	
	def __str__(self):
		return self.office_name

	class Meta:
		verbose_name = 'Contact'
		verbose_name_plural = 'Contacts'


class Hotlines(models.Model):
	contacts = models.ForeignKey(Contacts,on_delete=models.CASCADE)
	channel_type = models.CharField(
		max_length=20,
		null=True,
		blank=True,
		verbose_name='Channel - Medium Type',
		help_text='TeleComm Companies (i.e., Smart, Globe) Channel Type (i.e., Radio Frequencies,Landline,Department)'
		)
	contact_num = models.CharField(max_length=15,null=True,blank=True,verbose_name='Number')

	def __str__(self):
		return f"{self.channel_type} - {self.contact_num} ({self.contacts})"

	class Meta:
		verbose_name = 'Hotline'
		verbose_name_plural = 'Hotlines'
		ordering = ['-contacts']