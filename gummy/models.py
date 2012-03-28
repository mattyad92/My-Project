from django.db import models

# Create your models here.

class Shape(models.Model):
    shape =  models.CharField(max_length = 100)
    def __unicode__(self):
        return self.shape

class Color(models.Model):
    color =  models.CharField(max_length = 100)
    def __unicode__(self):
        return self.color

class Gummy(models.Model):
    shape =  models.ForeignKey(Shape)
    color =  models.ManyToManyField(Color)
    def __unicode__(self):
	return self.shape.shape
