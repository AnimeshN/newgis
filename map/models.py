from django.db import models

# Create your models here.


def user_directory_path(instance, filename):
    return 'user_{0}/{1}'.format(instance.user.id, filename)



class Layers(models.Model):
	name_of_layer = models.CharField(max_length=50)
	description = models.TextField(max_length=200)
	select_themes_CHOICES  = (
			('CEN','Census'),
			('EDU','Education'),
			('RUL','Rural'),
			('WAT','Water'),
			('HEL','Health'),
			('OTH','Other'),
		)
	select_theme = models.CharField(max_length=6,choices=select_themes_CHOICES,default='Census')
	if_other = models.CharField(max_length=50)
	source = models.CharField(max_length=50)
	types_CHOICES = (
			('GJ','GeoJSON'),
			('EL','Excel'),
			('CV','CSV'),
			('GL','GML'),
			('ZS','Zipped Shapefile'),
			('KL','KML'),
			('PF','PDF'),
			('TF','TIF'),
			('PG','PNG'),
			('JG','JPEG'),
		)
	types = models.CharField(max_length=6,choices=types_CHOICES,default='Zipped Shapefile')

	style_file_available_CHOICES = (
			('Y','Yes'),
			('N','No'),
		)
	style_file_available = models.CharField(max_length=2,choices=style_file_available_CHOICES,default='Yes')


	tool_used = models.CharField(max_length=50)

	layer = models.FileField(upload_to=user_directory_path)



