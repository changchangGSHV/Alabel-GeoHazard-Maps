from django.db import models
from django.contrib.auth.models import User


#Admin(Base)
class MDRRMO(models.Model):
	admin_id = models.ForeignKey(User,on_delete=models.PROTECT)

	class Meta:
		abstract = True


class Landslide(MDRRMO):
	lands_id = models.BigAutoField(primary_key=True)
	suscep_level = models.CharField(max_length=50,unique=True,default='None')
	suscep_info = models.TextField()

	def __str__(self):
		return self.suscep_level


# Landslide(Base)
class Lands_Base(models.Model):
	lands_id = models.ForeignKey(Landslide,on_delete=models.CASCADE)

	class Meta:
		abstract = True

class Landslide_Evac_Procedures(Lands_Base):
	evac_id = models.BigAutoField(primary_key=True)
	procedure_name = models.CharField(max_length=50, unique=True)
	procedure_content = models.TextField()

	def __str__(self):
		return self.procedure_name

	class Meta:
		verbose_name = 'Evacuation Procedure'
		verbose_name_plural = 'Landslide Evacuation Procedures'


class Landslide_Dropdown(models.Model):
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

	lands_drop_id = models.BigAutoField(primary_key=True)
	barangay_name = models.CharField(max_length=50,default='Alegria',choices=BARANGAY, unique=True)
	barangay_suscep_level = models.CharField(max_length=50,choices=LANDSLIDE_LEVELS)
	latitude = models.FloatField(blank=True,default=None)
	longitude = models.FloatField(blank=True,default=None)
	map_marker_img = models.ImageField(default='default.jpg',upload_to='landslide_marker_imgs',blank=True)
	map_marker_info = models.TextField()
	

	def __str__(self):
		return self.barangay_name

	class Meta:
		verbose_name = 'Landslide Dropdown'
		verbose_name_plural = 'Landslide Dropdown'
		ordering = ['barangay_name']


class Landslide_Guidelines(Lands_Base):
	guide_id = models.BigAutoField(primary_key=True)
	alert_level = models.CharField(max_length=50,unique=True)
	alert_level_guide = models.TextField()

	def __str__(self):
		return self.alert_level

	class Meta:
		verbose_name = 'Landslide Guidelines'
		verbose_name_plural = 'Landslide Guidelines'





# class Announcements(MDRRMO):
# 	announ_id = models.BigAutoField(primary_key=True)
# 	title = models.CharField(max_length=30)
# 	content = models.TextField()

# 	def __str__(self):
# 		return self.title

# 	class Meta:
# 		verbose_name_plural = 'Announcements'



# class Likes(models.Model):
# 	from django.core.validators import MinValueValidator, MaxValueValidator

# 	like_id = models.BigAutoField(primary_key=True)
# 	user_id = models.ForeignKey(User,on_delete=models.CASCADE)
# 	like_count = models.PositiveIntegerField(validators=[MinValueValidator(0), MaxValueValidator(1)])

# 	def __str__(self):
# 		return self.user_id.username

# 	class Meta:
# 		verbose_name_plural = 'User Likes'










